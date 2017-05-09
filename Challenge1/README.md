<h><b>Challenge 1</b><h><br>
<b>http://66.108.241.23/messages</b><br>
<b>Dependencies:</b>
  1. Python3.x
  2. asyncio
  3. aiohttp
  4. hashlib


For this challenge I chose to use python because of its quickness and simplicity in creating a web service. From my research on how to best design a web service, I discovered that with python 3 came a new module called asyncio which provides infrastructure for Asynchronous I/O and a pluggable event loop. I decided to implement this in my solution since it would serve best for a scalable web service.

For the data store I chose to use a dictionary within the same server class. I wanted to keep my solution simple, but looking forward if this were to be a real web service I would run a key/value store cache on a separate process. Something 
along the lines of redis or memcached.

<b>Optional Bonus Question:</b>

The current bottlenecks of this program is having a single process running for the web service and having a data store in that same process. By changing to a separate key/value store process, we could utilize a load balancer to increase/decrease
the number of web service process running while being able to acess the same data.
