'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.D=1
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"VanneD\",\"State\":" + str(M.D)+"}\n\n"
print(html)