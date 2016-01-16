'''
Created on 15 janv. 2016

@author: yfgi7251
'''

import time

class Mock:
    '''
    Bouchon pour la demo de FridayGeekLab HomeBroo
    '''
    Temperature1 = 15.0
    Temperature2 = 15.0
    Temperature3 = 15.0
    
    Cible1 = 78.0
    Cible2 = 50
    Cible3 = 50
    
    Pid1 = 0
    Pid2 = 0
    Pid3 = 0
    
    R1 = 0
    B1 = 0
    B2 = 0
    
    P1 = 0
    P2 = 0
    P3 = 0
    
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    F = 0
    G = 0
    H = 0
    I = 0
    J = 0
    
    lastmytime = time.time()
    file = ""

    def __init__(self,name):
        '''
        Constructor
        '''
        self.file = name
        #print("Bouchon cree sur fichier "+self.file)
        
    def Load(self):
        fichier = open(self.file, "r")
        self.Temperature1 = eval(fichier.readline().rstrip('\n'))
        self.Temperature2 = eval(fichier.readline().rstrip('\n'))
        self.Temperature3 = eval(fichier.readline().rstrip('\n'))
        
        self.Cible1 = eval(fichier.readline().rstrip('\n'))
        self.Cible2 = eval(fichier.readline().rstrip('\n'))
        self.Cible3 = eval(fichier.readline().rstrip('\n'))
        
        self.Pid1 = eval(fichier.readline().rstrip('\n'))
        self.Pid2 = eval(fichier.readline().rstrip('\n'))
        self.Pid3 = eval(fichier.readline().rstrip('\n'))
        
        self.R1 = eval(fichier.readline().rstrip('\n'))
        self.B1 = eval(fichier.readline().rstrip('\n'))
        self.B2 = eval(fichier.readline().rstrip('\n'))
        
        self.P1 = eval(fichier.readline().rstrip('\n'))
        self.P2 = eval(fichier.readline().rstrip('\n'))
        self.P3 = eval(fichier.readline().rstrip('\n'))
        
        self.A = eval(fichier.readline().rstrip('\n'))
        self.B = eval(fichier.readline().rstrip('\n')) 
        self.C = eval(fichier.readline().rstrip('\n'))
        self.D = eval(fichier.readline().rstrip('\n'))
        self.E = eval(fichier.readline().rstrip('\n'))
        self.F = eval(fichier.readline().rstrip('\n'))
        self.G = eval(fichier.readline().rstrip('\n'))
        self.H = eval(fichier.readline().rstrip('\n'))
        self.I = eval(fichier.readline().rstrip('\n'))
        self.J = eval(fichier.readline().rstrip('\n'))

                
        self.lastmytime = eval(fichier.readline().rstrip('\n'))
        fichier.close()
        
        
        
    def Test(self):
        print("test ["+str(self.Temperature1)+"]")
        
    def Reset(self):
        
        self.Temperature1 = 15.0
        self.Temperature2 = 15.0
        self.Temperature3 = 15.0
        
        self.Cible1 = 78.0
        self.Cible2 = 50
        self.Cible3 = 50
        
        self.Pid1 = 0
        self.Pid2 = 0
        self.Pid3 = 0
        
        self.R1 = 0
        self.B1 = 0
        self.B2 = 0
        
        self.P1 = 0
        self.P2 = 0
        self.P3 = 0
        
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.F = 0
        self.G = 0
        self.H = 0
        self.I = 0
        self.J = 0
        
     
        
        
    def Compute(self):
        deltatime=time.time() - self.lastmytime
        if self.R1 > 0 :
            self.Temperature1+=(1/10)*deltatime;
        else:
            self.Temperature1-=((self.Temperature1 - 20)/50)*deltatime;
            
        if self.B1 > 0 :
            self.Temperature2+=(1/10)*deltatime;
        else:
            self.Temperature2-=((self.Temperature2 - 20)/50)*deltatime;
            
        if self.B2 > 0 :
            self.Temperature3+=(1/10)*deltatime;
        else:
            self.Temperature3-=((self.Temperature3 - 20)/50)*deltatime;
            
            
        if self.Pid1 >0:
            if self.Temperature1 > self.Cible1:
                self.R1 = 0
                self.Temperature1 = self.Cible1
            else:
                self.R1 = 1
                
        if self.Pid2 >0:
            if self.Temperature2 > self.Cible2:
                self.P1 = 0
                self.Temperature2 = self.Cible2
            else:
                self.P1 = 1
                self.Temperature1-=((self.Temperature1-self.Temperature2)/100)*deltatime;
                self.Temperature2+=((self.Temperature1-self.Temperature2)/110)*deltatime;

        if self.Pid3 >0:        
            if self.Temperature3 > self.Cible3:
                self.P2 = 0
                self.Temperature3 = self.Cible3
            else:
                self.P2 = 1
                self.Temperature2-=((self.Temperature2-self.Temperature3)/100)*deltatime;
                self.Temperature3+=((self.Temperature3-self.Temperature3)/110)*deltatime;

                
    def Close(self):
        fichier = open(self.file,"w")
        fichier.write(str(self.Temperature1)+"\n")
        fichier.write(str(self.Temperature2)+"\n")
        fichier.write(str(self.Temperature3)+"\n")
                
        fichier.write(str(self.Cible1)+"\n")
        fichier.write(str(self.Cible2)+"\n")
        fichier.write(str(self.Cible3)+"\n")
  
        fichier.write(str(self.Pid1)+"\n")
        fichier.write(str(self.Pid2)+"\n")
        fichier.write(str(self.Pid3)+"\n")
     
        
        fichier.write(str(self.R1)+"\n")
        fichier.write(str(self.B1)+"\n")
        fichier.write(str(self.B2)+"\n")
        
       
        fichier.write(str(self.P1)+"\n")
        fichier.write(str(self.P2)+"\n")
        fichier.write(str(self.P3)+"\n")
     
       
        
        fichier.write(str(self.A)+"\n")
        fichier.write(str(self.B)+"\n")
        fichier.write(str(self.C)+"\n")
        fichier.write(str(self.D)+"\n")  
        fichier.write(str(self.E)+"\n")
        fichier.write(str(self.F)+"\n")
        fichier.write(str(self.G)+"\n")
        fichier.write(str(self.H)+"\n")
        fichier.write(str(self.I)+"\n")       
        fichier.write(str(self.J)+"\n")       
             
        fichier.write(str(time.time())+"\n\n")
        
        fichier.close()