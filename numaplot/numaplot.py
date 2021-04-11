# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:06:23 2021
@author: Kurt Pagani <nilqed@gmail.com>

Requirements:
    
-- pip install web.py
-- import web      https://webpy.org/ (public domain)
-- import json     https://www.json.org/json-en.html
-- import requests https://pypi.org/project/requests/

-- pip install py-gnuplot (NOT pygnuplot !!!) 
-- import pygnuplot https://pypi.org/project/py-gnuplot/


PlotServer V 0.1 (pyfamus)
Press Ctrl-C to terminate.

http://0.0.0.0:8080/
dict_keys(['myvar', 'code', 'id'])
dict_values(['12', 'D(x^n,x,4)', 'kfp/asdf'])
D(x^n,x,4)
?myvar=12
127.0.0.1:50714 - - [03/Apr/2021 22:17:46] "HTTP/1.1 POST /gnuplot" - 200 OK

GET: firefox http://localhost:8080/gnuplot/zzz333?myvar=123
-> {'uid': '/zzz333', 'data': dict_values(['123'])}

********************************
pip install .
python -m numaplot.numaplot
python -m numaplot.test_gnuplot
********************************

$ pip show numaplot  (use -f to see files)
Name: numaplot
Version: 0.1.0
Summary: Numerics- and plot server.
Home-page: http://github.com/nilqed/numaplot
Author: Kurt Pagani
Author-email: nilqed@gmail.com
License: BSD
Location: c:\python38\lib\site-packages
Requires: web.py, requests, pygnuplot
Required-by:

"""

try:
    import __devel__
    _release_ = False
except:
    _release_ = True



import web
from uuid import uuid4

if not _release_:
    import han_gnuplot
    from storage import STORAGE
else:
    import numaplot.han_gnuplot as han_gnuplot
    from numaplot.storage import STORAGE
    

urls = (
    '/', 'Index',
    '/gnuplot(.*)', 'GnuPlot',
    '/storage(.*)', 'Storage'
)

app = web.application(urls, globals())

class Index:
    
    def GET(self):
        return 'INDEX\n'


class Storage:
    def GET(self,uid):
        if not uid:
            return STORAGE
        else:
            uid = uid.lstrip('/')
            if STORAGE.__contains__(uid):
                return(STORAGE[uid])
            else:
                return('ERROR')

class GnuPlot:
           
    def GET(self, uid):
        if not uid:
            return('ERROR')
        else:
            uid = uid.lstrip('/')
            if STORAGE.__contains__(uid):
                return(STORAGE[uid])
            else:
                return('ERROR')
        
    
    def POST(self,cmd):
        data = web.input()
        uid = str(uuid4())
        save = dict()
        save.update({'post': data})
        STORAGE.update({uid: save})
        han_gnuplot.perform(uid)
        return(uid)
    

        
    


def main():
    print("numaplot V 0.1")
    print("Press Ctrl-C to terminate.\n")
    app = web.application(urls, globals())
    app.run()    

if __name__ == "__main__": main()
