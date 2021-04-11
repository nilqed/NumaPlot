# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:17:28 2021

@author: kfp


$ python test_gnuplot.py
65cd7aeb-1d49-4988-b480-61a97e608c3c
{'post': <Storage {'terminal': 'qt', 'style': 'increment default', 'title': '"Si
mple Plots" font ",20" norotate', 'samples': '50, 50', 'plot': "'[-10:10] sin(x)
', 'atan(x)', 'cos(atan(x))'"}>}

-- if we use key 'plots' instead of 'plot' =>
$python test_gnuplot.py
200596e7-cd22-4b8c-862c-0aa9b9d631a0
{'error': 'check_minreq failed'}


How:
Start server: python numaplot.py
Open cmd: $ python test_gnuplot.py


"""
import requests

url = 'http://localhost:8080/gnuplot'

payload1 = {'terminal': 'qt', 
            'method'  : 'plot',
            'plot'    : '[-10:10] sin(x), atan(x), cos(atan(x)),x**2/20',
            'style'   : 'increment default',
            'samples' : '50, 50',
            'title'   : '"Simple Plots" font ",20" norotate',
            'key'     : 'fixed left top vertical Right noreverse enhanced\
                         autotitle box lt black linewidth 1.000 dashtype \
                         solid',
           }
    


s1 = 'cos(u)+.5*cos(u)*cos(v),sin(u)+.5*sin(u)*cos(v),.5*sin(v) with lines,'
s2 = '1+cos(u)+.5*cos(u)*cos(v),.5*sin(v),sin(u)+.5*sin(u)*cos(v) with lines'    
    
payload2 = {'terminal'   : 'qt',
            'method'     : 'splot',
            'splot'      : s1+s2,
            'output'     : '',
            'dummy'      : 'u, v',
            'key'        : 'bmargin center horizontal Right noreverse \
                            enhanced autotitle nobox',
            'style'      : "['increment default','data lines']",
            'parametric' : '',
            'view'       : '50, 30, 1, 1',
            'isosamples' : '50, 20',
            'hidden3d'   : 'back offset 1 trianglepattern 3 \
                            undefined 1 altdiagonal bentover',
            'xyplane'    : 'relative 0',
            'title'      : '"Interlocking Tori"',
            'urange'     : '[ -3.14159 : 3.14159 ] noreverse nowriteback',
            'vrange'     : '[ -3.14159 : 3.14159 ] noreverse nowriteback'
            }    
    
    
payload3 = {'terminal'   : 'wxt',
            'method'     : 'splot',
            'splot'      : s1+s2,
            'output'     : '',
            'dummy'      : 'u, v',
            'key'        : 'bmargin center horizontal Right noreverse \
                            enhanced autotitle nobox',
            'style'      : "['increment default','data lines']",
            'parametric' : '',
            'view'       : '50, 30, 1, 1',
            'isosamples' : '50, 20',
            'hidden3d'   : 'back offset 1 trianglepattern 3 \
                            undefined 1 altdiagonal bentover',
            'xyplane'    : 'relative 0',
            'title'      : '"Interlocking Tori"',
            'urange'     : '[ -3.14159 : 3.14159 ] noreverse nowriteback',
            'vrange'     : '[ -3.14159 : 3.14159 ] noreverse nowriteback'
            }        

#r = requests.post(url, data=payload)
#print(r)
#uid = r.content.decode('UTF-8')
#print(uid)
#print(r.text)
#g = requests.get(url + "/" + uid)
#print(g.content.decode('UTF-8'))

def test(url,payload):
    r = requests.post(url, data=payload)
    uid = r.content.decode('UTF-8')
    g = requests.get(url + "/" + uid)
    print(g.content.decode('UTF-8'))
    
# 2d plot
test(url, payload1)

# 3d plot, terminal = qt
test(url, payload2)

# 3d plot, terminal = wxt
test(url, payload3)








