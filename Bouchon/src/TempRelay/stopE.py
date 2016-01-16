'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.E=0
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"VanneE\",\"State\":" + str(M.E)+"}\n\n"
print(html)