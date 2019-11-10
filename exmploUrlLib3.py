# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:30:38 2019

@author: Igori
"""

import urllib3

http = urllib3.PoolManager()
pagina = http.request('GET', 'http://www.iaexpert.com.br')
pagina.status
pagina.data[0:50]