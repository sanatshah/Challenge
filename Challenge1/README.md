<h><b>Challenge 1</b></h>

<b>Dependencies:</b></br>
  Python3.x</br>
  asyncio</br>
  aiohttp</br>
  hashlib</br>


For this challenge I chose to use python because of its quickness and simplicity of creating a web service. Keeping scalability in mind I began doing research on how to best design the web service. I discovered that python 3 brought a new module called asyncio which provides infrastructure for Asynchronous I/O and a pluggable event loop. I programmed the microservice to take advantage of these features

For the data store I chose to use a dictionary within the same server class. I chose this because I wanted to keep my solution simple, but looking forward if this was a real web service I would run a key/value store cache on a separate process. Something along the lines of redis or memcached.


<b>Optional Bonus Question:</b>

The current bottlenecks of this program is having a single process for the web service and having a data store in that same process. By changing to a separate key/value store process, we could utilize a load balancer to increase/decrease the number of web service process running and they would be able to share data.
