'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.P1=1
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"Pompe1\",\"State\":" + str(M.P1)+"}\n\n"
print(html)