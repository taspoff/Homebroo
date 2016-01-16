'''
Created on 4 janv. 2016

@author: YFGI7251
'''

fichier = open("data", "r")
Temperature1 = eval(fichier.readline().rstrip('\n'))
Relais1 = eval(fichier.readline().rstrip('\n'))
Temperature2 = eval(fichier.readline().rstrip('\n'))
Relais2 = eval(fichier.readline().rstrip('\n'))
Temperature3 = eval(fichier.readline().rstrip('\n'))
Relais3 = eval(fichier.readline().rstrip('\n'))
Cible1 = eval(fichier.readline().rstrip('\n'))
Cible2 = eval(fichier.readline().rstrip('\n'))
Cible3 = eval(fichier.readline().rstrip('\n'))
Pid1 = eval(fichier.readline().rstrip('\n'))
Pid2 = eval(fichier.readline().rstrip('\n'))
Pid3 = eval(fichier.readline().rstrip('\n'))
fichier.close()

Page = "<html><head><title>FG_PID V01</title></head>";
Page += "<body><center><H1>Senseur : Bouchon1</H1> IP = localhost";
Page += "<Frame name='pilotage'> <Form target='pilotage' action='http://CHAMP_000/setData' method='get'><P>";
Page += "<table><tr><td><LABEL for='Affectation'>Affectation: </LABEL></td>";
Page += "<td><INPUT type='text' value='CHAMP_001' name='Affectation'></td></tr>";
Page += "<tr><td><LABEL for='wantedTemp'>Temperature desiree: </LABEL></td>";
Page += "<td><INPUT type='text' value='"+str(Cible1)+"' name='WantedTemp'></td></tr>";
Page += "<tr><td><LABEL for='runingpid'>PID running: </LABEL></td>";
Page += "<td><INPUT type='checkbox' value='Up' name='PID' "
if Pid1 >0:
	Page += "checked "
	
Page +="></td></tr>";
Page += "<tr><td><LABEL for='relay'>Etat du relais: </LABEL></td>";
Page += "<td><INPUT type='radio' value='Up' name='Relay' "
if Relais1 >0:
	Page +="checked "
	
Page +=">Up<br><INPUT type='radio' value='Down' name='Relay' "
if Relais1 <1:
	Page +="checked "
Page += ">Down</td></tr>";
Page += "<tr><td><LABEL for='ActionRelay'>Action du relais sur la temperature</label></td>";
Page += "<td><Input type='radio' value='Heating' name='ActionRelay' checked >Chauffant<BR>";
Page += "<Input type='radio' value='Cooling' name='ActionRelay'  >Refrigerant</td></tr>";
Page += "<tr><td><LABEL for='Display'>Emplacement du graphique</LABEL></td><td><INPUT type='text' value='CHAMP_007' name='Display'></td></tr>";
Page += "<tr><td></td><td><input type='submit'></td></tr>";
Page += "</table></form>";
Page += "</body></html>";

html="Content-type: text/html\n\n"
html += Page


if Relais1 > 0 :
	Temperature1+=0.3;
else:
	Temperature1-=0.1;
	
if Relais2 > 0 :
	Temperature2+=0.3;
else:
	Temperature2-=0.1;
	
if Relais3 > 0 :
	Temperature3+=0.3;
else:
	Temperature3-=0.1;
	
if Pid1 >0:
	if Temperature1 > Cible1:
		Relais1 = 0
	else:
		Relais1 = 1
if Pid2 >0:
	if Temperature2 > Cible2:
		Relais2 = 0
	else:
		Relais2 = 1
if Pid3 >0:		
	if Temperature3 > Cible3:
		Relais3 = 0
	else:
		Relais3 = 1

fichier = open("data","w")
fichier.write(str(Temperature1))
fichier.write("\n")
fichier.write(str(Relais1))
fichier.write("\n")
fichier.write(str(Temperature2))
fichier.write("\n")
fichier.write(str(Relais2))
fichier.write("\n")
fichier.write(str(Temperature3))
fichier.write("\n")
fichier.write(str(Relais3))
fichier.write("\n")
fichier.write(str(Cible1))
fichier.write("\n")
fichier.write(str(Cible2))
fichier.write("\n")
fichier.write(str(Cible3))
fichier.write("\n")
fichier.write(str(Pid1))
fichier.write("\n")
fichier.write(str(Pid2))
fichier.write("\n")
fichier.write(str(Pid3))
fichier.write("\n\n")
fichier.close()

print(html)