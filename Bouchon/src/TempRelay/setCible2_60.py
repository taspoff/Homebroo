'''
Created on 4 janv. 2016

@author: YFGI7251
'''

import libMock

M = libMock.Mock("data")
M.Load()
M.Cible2=60.0
M.Compute()
M.Close()


html="Content-type: application/json\n\n{\"Sensor\":\"Ebu\",\"Cible\":" + str(M.Cible2)+"}\n\n"
print(html)