#!/usr/bin/python3
'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.B1=0
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"Bruleur1\",\"State\":" + str(M.B1)+"}\n\n"
print(html)