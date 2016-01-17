#!/usr/bin/python3
'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.H=1
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"VanneH\",\"State\":" + str(M.H)+"}\n\n"
print(html)