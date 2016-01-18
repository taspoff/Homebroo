Bouchons

Necessite Python3

Lancer avec la commande : 
  nohup python3 MonMain.py >~/Bouchon.log &
  
Fichiers:
libMock.py : librairie d'objet "base de donnée" pour le bouchon, gerant le fichier plat "data" local en lecture ecriture pour passage du contexte. Gere egalement la simulation de temperature
MonMain.py: Serveur HTTP simple
data : Contient les variables d'etat des vannes, pompes, bruleurs, resistance, PID et cibles, et le dernier timestamp (calcule des tempêratures)

URLs
(par standard : 0 = OFF (flux Ferme), 1 = ON (flux Ouvert))
http://vps220792.ovh.net:8890/Reset.py
  mets les données de la base par defaut (vannes a Off, temperatures ambiantes, PIDs a Off, et cibles d'empatage)




http://vps220792.ovh.net:8890/getA.py
http://vps220792.ovh.net:8890/getB.py
http://vps220792.ovh.net:8890/getC.py
http://vps220792.ovh.net:8890/getD.py
http://vps220792.ovh.net:8890/getE.py
http://vps220792.ovh.net:8890/getF.py
http://vps220792.ovh.net:8890/getG.py
http://vps220792.ovh.net:8890/getH.py
http://vps220792.ovh.net:8890/getI.py
http://vps220792.ovh.net:8890/getJ.py
    Recupere l'etat sans les modifier 
      des vannes de A à J : Retour JSON de type {"Sensor":"VanneA","State":1}
      
http://vps220792.ovh.net:8890/getR1.py --> {"Sensor":"Resistance1","State":1}
http://vps220792.ovh.net:8890/getB1.py --> {"Sensor":"Bruleur1","State":1}
http://vps220792.ovh.net:8890/getB2.py --> {"Sensor":"Bruleur2","State":1}
http://vps220792.ovh.net:8890/getP1.py --> {"Sensor":"Pompe1","State":0}
http://vps220792.ovh.net:8890/getP2.py --> {"Sensor":"Pompe2","State":0}
http://vps220792.ovh.net:8890/getP3.py --> {"Sensor":"Pompe3","State":0}

  recupere l'etat courant (modifiable si les PIDs sont a ON) 
    des bruleurs et resistance 
    des Pompes
    
http://vps220792.ovh.net:8890/getCible1.py --> {"Sensor":"HotTank","Cible":78.0}
http://vps220792.ovh.net:8890/getCible2.py --> {"Sensor":"Ebu","Cible":50}
http://vps220792.ovh.net:8890/getCible3.py --> {"Sensor":"Mashtun","Cible":50}
http://vps220792.ovh.net:8890/getPID1.py --> {"Sensor":"HotTank","PID":0}
http://vps220792.ovh.net:8890/getPID2.py --> {"Sensor":"Ebu","PID":0}
http://vps220792.ovh.net:8890/getPID3.py --> {"Sensor":"Mashtun","PID":1}
  retourne la cible de T° des PIDs 1 2 ou 3 ou l'etat des PIDs
  
http://vps220792.ovh.net:8890/getTemp1.py --> {"Sensor":"HotTank","Temp":411.0128946425888}
http://vps220792.ovh.net:8890/getTemp2.py --> {"Sensor":"Ebu","Temp":5111.634516098446}
http://vps220792.ovh.net:8890/getTemp3.py --> {"Sensor":"Mashtun","Temp":23.714728171904255}
  Retourne la temperature a l'instant des sondes Temp1, Temp2 et Temp3. l'emulation est basé sur le temps
  
  
http://vps220792.ovh.net:8890/setCible1_78.py --> {"Sensor":"HotTank","Cible":78.0}
http://vps220792.ovh.net:8890/setCible2_52.py --> {"Sensor":"Ebu","Cible":52.0}
http://vps220792.ovh.net:8890/setCible2_60.py --> {"Sensor":"Ebu","Cible":60.0}
http://vps220792.ovh.net:8890/setCible2_72.py --> {"Sensor":"Ebu","Cible":72.0}
http://vps220792.ovh.net:8890/setCible2_78.py --> {"Sensor":"Ebu","Cible":78.0}
http://vps220792.ovh.net:8890/setCible3_52.py --> {"Sensor":"Ebu","Cible":52.0}
http://vps220792.ovh.net:8890/setCible3_60.py --> {"Sensor":"Ebu","Cible":60.0}
http://vps220792.ovh.net:8890/setCible3_72.py --> {"Sensor":"Ebu","Cible":72.0}
http://vps220792.ovh.net:8890/setCible3_78.py --> {"Sensor":"Ebu","Cible":78.0}
  Definit la cible en terme de temperature (pas d'url avec parametre dans cette version de bouchon...)
  
http://vps220792.ovh.net:8890/startA.py --> {"Sensor":"VanneA","State":1}
http://vps220792.ovh.net:8890/startB.py --> {"Sensor":"VanneB","State":1}
http://vps220792.ovh.net:8890/startC.py --> {"Sensor":"VanneC","State":1}
http://vps220792.ovh.net:8890/startD.py --> {"Sensor":"VanneD","State":1}
http://vps220792.ovh.net:8890/startE.py --> {"Sensor":"VanneE","State":1}
http://vps220792.ovh.net:8890/startF.py --> {"Sensor":"VanneF","State":1}
http://vps220792.ovh.net:8890/startG.py --> {"Sensor":"VanneG","State":1}
http://vps220792.ovh.net:8890/startH.py --> {"Sensor":"VanneH","State":1}
http://vps220792.ovh.net:8890/startI.py --> {"Sensor":"VanneI","State":1}
http://vps220792.ovh.net:8890/startJ.py --> {"Sensor":"VanneJ","State":1}
http://vps220792.ovh.net:8890/stopA.py --> {"Sensor":"VanneA","State":0}
http://vps220792.ovh.net:8890/stopB.py --> {"Sensor":"VanneB","State":0}
http://vps220792.ovh.net:8890/stopC.py --> {"Sensor":"VanneC","State":0}
http://vps220792.ovh.net:8890/stopD.py --> {"Sensor":"VanneD","State":0}
http://vps220792.ovh.net:8890/stopE.py --> {"Sensor":"VanneE","State":0}
http://vps220792.ovh.net:8890/stopF.py --> {"Sensor":"VanneF","State":0}
http://vps220792.ovh.net:8890/stopG.py --> {"Sensor":"VanneG","State":0}
http://vps220792.ovh.net:8890/stopH.py --> {"Sensor":"VanneH","State":0}
http://vps220792.ovh.net:8890/stopI.py --> {"Sensor":"VanneI","State":0}
http://vps220792.ovh.net:8890/stopJ.py --> {"Sensor":"VanneJ","State":0}
  Active ou desactive les vannes a A a J
  

http://vps220792.ovh.net:8890/startR1.py --> {"Sensor":"Resistance1","State":1}
http://vps220792.ovh.net:8890/startB1.py --> {"Sensor":"Bruleur1","State":1}
http://vps220792.ovh.net:8890/startB2.py --> {"Sensor":"Bruleur2","State":1} 
http://vps220792.ovh.net:8890/stopR1.py --> {"Sensor":"Resistance1","State":0}
http://vps220792.ovh.net:8890/stopB1.py --> {"Sensor":"Bruleur1","State":0}
http://vps220792.ovh.net:8890/stopB2.py --> {"Sensor":"Bruleur2","State":0} 
  Active ou desactive les resistances R1 et bruleurs B1 et B2

http://vps220792.ovh.net:8890/startP1.py -->{"Sensor":"Pompe1","State":1}
http://vps220792.ovh.net:8890/startP2.py -->{"Sensor":"Pompe2","State":1}
http://vps220792.ovh.net:8890/startP3.py -->{"Sensor":"Pompe3","State":1}
http://vps220792.ovh.net:8890/stopP1.py -->{"Sensor":"Pompe1","State":0}
http://vps220792.ovh.net:8890/stopP2.py -->{"Sensor":"Pompe2","State":0}
http://vps220792.ovh.net:8890/stopP3.py -->{"Sensor":"Pompe3","State":0}
  Active ou desactive les pompes 1 a 3

http://vps220792.ovh.net:8890/startPID1.py --> {"Sensor":"HotTank","PID":1}
http://vps220792.ovh.net:8890/startPID2.py --> {"Sensor":"Ebu","PID":1}
http://vps220792.ovh.net:8890/startPID3.py --> {"Sensor":"Mashtun","PID":1}
http://vps220792.ovh.net:8890/stopPID1.py --> {"Sensor":"HotTank","PID":0}
http://vps220792.ovh.net:8890/stopPID2.py --> {"Sensor":"Ebu","PID":0}
http://vps220792.ovh.net:8890/stopPID3.py --> {"Sensor":"Mashtun","PID":0}  
  Active ou desactive l'algorithmre de controle de la temperature PID1, 2 ou 3. L'activation de ces dernier amene le demarrage ou l'arret des elements chauffants et des pompes jusqu'a atteinte des temperatures cible au niveau des sondes.
  

  



    
