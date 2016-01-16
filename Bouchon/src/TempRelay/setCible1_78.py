'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.Cible1=78.0
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"HotTank\",\"Cible\":" + str(M.Cible1)+"}\n\n"
print(html)