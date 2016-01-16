'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.P2=1
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"Pompe2\",\"State\":" + str(M.P2)+"}\n\n"
print(html)