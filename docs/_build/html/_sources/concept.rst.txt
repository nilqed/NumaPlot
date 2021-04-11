The concept
-----------

The principle is quite simple. The client sends a `POST`_ request, whereby
the data is some `JSON`_ record, depending on what `numaplot` is required
to do. The `post` method of the class (handling the request) will return 
a unique id (`uuid4`_) to the client and delegates the task to a corresponding
handler (e.g. py-gnuplot). The client may then get the results by using
the `uid` in a `GET`_ request (e.g. using a web-browser or by a request
library, whatever). 

For the implementation of the `HTTP`_ server we will use the excellent 
`web.py`_:
   
   web.py is a web framework for Python that is as simple as it is powerful. 
   web.py is in the public domain, you can use it for whatever purpose with 
   absolutely no restrictions.

Instead of tiresome explanations we will show the mechanisms by commenting
the skeleton module below. Although, most lines are self-explaining. 

.. code-block:: python
   
	import web
	from uuid import uuid4
	
	
	STORAGE = dict()         # global storage
	
	urls = (                 # pairs, meaning 'URL', 'CLASS called'
	    '/', 'Index',
	    '/gnuplot(.*)', 'GnuPlot'
	)
	
	app = web.application(urls, globals())
	
	class Index:             # just returns the string 'INDEX\n'
	    
	    def GET(self):
	        return 'INDEX\n'
	
	
	class GnuPlot:           # fake class; called when requested 
	                         #  http://localhost:8080/gnuplot/xyz
	           
	    def GET(self, uid):  # uid = /xyz from example url above
	        if not uid:
	            return('ERROR')
	        else:
	            if STORAGE.__contains__(uid):  # if POST generated key=uid
	                                           # then return the value
	                return(STORAGE[uid])
	            else:
	                return('ERROR')
	      
	    
	    def POST(self,cmd):
	        data = web.input()                 # data submitted
	        uid = str(uuid4())                 # generate uid
	        save = dict()
	        save.update({'post': data})        # save 'data' with key 'post'
	        STORAGE.update({'/'+uid: save})    # update global storage
	        return(uid)                        # return uid to the calller
	    
	
	
	def main():
	    print("numaplot V 0.1")
	    print("Press Ctrl-C to terminate.\n")
	    app = web.application(urls, globals())
	    app.run()    
	
	if __name__ == "__main__": main()



Before starting the server we need a client. In `Python`_ we canuse the
`requests`_ library: 

.. code-block:: python

    import requests

    url = 'http://localhost:8182/gnuplot?myvar=12'

    payload = {'code': 'lorem', 'id':'ipsum'}

    r = requests.post(url, data=payload)

    print(r.content)


Now we start the server ::

    python numaplot.py 8182
    numaplot V 0.1
    Press Ctrl-C to terminate.
    http://0.0.0.0:8182/
     
Note that we have chosen the port ``8182``. Default (i.e if omitted) 
is ``8080``.

Starting the client ::

    python reqcli.py
    b'93de627a-cac1-44f1-8915-74c0e2b39e22'

returns the ``uid``. With this we can get the ``output`` by a `GET`_ 
request (in this case firefox):   

::
   
   http://localhost:8182/gnuplot/ef58741d-60f8-4f17-8774-8d56a6260884

and you will/should see ::

   <Storage {'myvar': '12', 'id': 'ipsum', 'code': 'lorem'}>
   
in a webpage. Notice that the variable `myvar` from the URL suffix
``?myvar=12`` will be stored as well.

 


.. _JSON: https://www.json.org/json-en.html
.. _POST: https://en.wikipedia.org/wiki/POST_(HTTP)
.. _GET: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods
.. _uuid4: https://en.wikipedia.org/wiki/Universally_unique_identifier
.. _HTTP: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
.. _web.py : https://webpy.org/
.. _requests: https://docs.python-requests.org/en/master/
.. _Python: https://www.python.org/