'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.A=0
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"VanneA\",\"State\":" + str(M.A)+"}\n\n"
print(html)