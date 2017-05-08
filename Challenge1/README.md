Challenge 1

Dependencies:
  Python3.x
  asyncio
  aiohttp
  hashlib


For this challenge I chose to use python because of the quickness and simplicity of creating a web service. Keeping scalability in mind I began doing research on how
to best design the web service. From my research I discovered that with python 3 came a new module called asyncio which provides infrastructure for Asynchronous I/O
and a pluggable event loop.   

For the data store I chose to use a dictionary within the same server class. I
wanted to keep my solution simple, but looking forward if this was a real web
service I would run a key/value store cache on a separate process. Something 
along the lines of redis or memcached.


Optional Bonus Question:

The current bottlenecks of this program is having a single process running for
the web service and having a data store in the same process. By changing to a separate
key/value store process, we could utilize a load balancer to increase/decrease
the number of web service process running.
