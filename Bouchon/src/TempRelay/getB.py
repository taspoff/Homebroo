'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"VanneB\",\"State\":" + str(M.B)+"}\n\n"
print(html)