# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 01:30:10 2021

@author: kfp
"""

try:
    import __devel__
    _release_ = False
except:
    _release_ = True
    

from functools import reduce
from pygnuplot import gnuplot

if not _release_:
    from storage import STORAGE
else:
    from numaplot.storage import STORAGE


keys2d = ['styles', 'samples', 'key', 'title']
keys3d = keys2d + ['dummy', 'urange', 'vrange', 'xyplane', 'hidden3d',\
                   'isosamples', 'parametric', 'output']  


def check_minreq(data):
    """ Minimal requirements: if data is admissible then it shall
    be forwarded to the gnuplot handler, otherwise an error message
    should be returned. Return type is <boolean>.
    """
    minkeys = ['terminal','method']
    b = [data.keys().__contains__(s) for s in minkeys]
    f=lambda x,y: x & y
    return reduce(f,b)
   

def check_key(data, key):
    """ Check if key in data. If so, then return the value, otherwise
    return the empty string.
    """
    if data.keys().__contains__(key):
        return data[key]
    else:
        return ''


def make_kw(keys,data):
    """ Create the **kw for gnuplot.set() -- unpack operator ** """
    d = dict()
    for x in keys:
      d.update({x : check_key(data,x)})
    return d
         

def perform(uid):
    """ With the argument='uid' get the the data from STORAGE and
    perform the method requested. 
    """
    
    try:
        data = STORAGE[uid]['post'] 
    except Exception:
        STORAGE.update({uid: {'error' : KeyError("xyz") }})
        return False
    
    if not check_minreq(data):
        STORAGE.update({uid: {'error' : "check_minreq failed" }})
        return False
    
    g = gnuplot.Gnuplot(terminal = data['terminal'])
    
    
    if data['method'] == 'plot':
        g.set(**make_kw(keys2d, data))
        g.plot(data['plot'])
        
    elif data['method'] == 'splot':
        g.set(**make_kw(keys3d, data))
        g.splot(data['splot'])
    
    else:
         pass
        
    print(data['terminal']) #debug