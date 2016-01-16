'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.I=1
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"VanneI\",\"State\":" + str(M.I)+"}\n\n"
print(html)