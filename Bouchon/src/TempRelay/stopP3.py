#!/usr/bin/python3
'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.P3=0
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"Pompe3\",\"State\":" + str(M.P3)+"}\n\n"
print(html)