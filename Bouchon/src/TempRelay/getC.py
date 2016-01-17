#!/usr/bin/python3
'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"VanneC\",\"State\":" + str(M.C)+"}\n\n"
print(html)