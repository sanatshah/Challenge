from aiohttp import web
import asyncio
from aiohttp.log import access_logger
import hashlib
import json

'''
Routes:

    POST @ /messages
        PARAMS: {message}
        RETVAL: {digest}

    GET @ /messages/{digestID}
        RETVAL: {message}
'''

class Server:

    def __init__(self, address, port, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.address = address
        self.port = port
        self.loop = loop
        self._server = None
        self._map = {};

    # POST @ /messages
    async def setHashFromString(self, request):

        data = await request.json()
        message = data['message'];
        messageEncoded = message.encode('utf-8')
        hashValue = hashlib.sha256(messageEncoded).hexdigest()

        #store mesesage with given hashValue
        self._map[hashValue] = message;
        print ("Hashing '" + self._map[hashValue] +"' and with SHA256 digest of : " + hashValue)

        retVal = "{ 'digest' : " + hashValue + "}"
        retVal_JSON = json.dumps(retVal)

        return web.Response(
            content_type="application/json",
            body = retVal_JSON
        )

    # GET @ /messages/{hashID}
    async def getStringFromHash(self, request):
        data = await request.post()
        hashValue = request.match_info['hashID']

        #grab hash value or throw a 404
        if ( hashValue in self._map):
            message = self._map[hashValue]
        else:
            return web.HTTPNotFound()

        #return hashed message as a JSON
        print ("Found message: " + message + " with hash: " + hashValue)
        retVal = "{ 'message' : " + message + "}"
        retVal_JSON = json.dumps(retVal)

        return web.Response(
            content_type="application/json",
            body=retVal_JSON
        )


    async def start(self):
        loop = self.loop
        app = web.Application(loop=loop)
        app.router.add_post('/messages', self.setHashFromString, expect_handler = web.Request.json)
        app.router.add_get('/messages/{hashID}', self.getStringFromHash)
        print ("Starting Web Server")

        self._server = await loop.create_server(
            app.make_handler(access_log=access_logger),
            self.address,
            self.port
        )



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    server = Server('0.0.0.0', '3000', loop=loop)

    loop.run_until_complete(server.start())
    loop.run_forever()
