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
      
http://vps220792.ovh.net:8890/getR1.py
http://vps220792.ovh.net:8890/getB1.py
http://vps220792.ovh.net:8890/getB2.py
  recupere l'etat courant (modifiable si les PIDs sont a ON) 
    des bruleurs et resistance : Retour JSON de type {"Sensor":"Bruleur1","State":1}
    
http://vps220792.ovh.net:8890/getCible1.py --> {"Sensor":"HotTank","Cible":78.0}
http://vps220792.ovh.net:8890/getCible2.py --> {"Sensor":"Ebu","Cible":50}
http://vps220792.ovh.net:8890/getCible3.py --> {"Sensor":"Mashtun","Cible":50}
  retourne la cible de T° des PIDs 1 2 ou 3
  



    
