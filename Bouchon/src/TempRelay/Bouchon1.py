#!/usr/bin/python3
'''
Created on 4 janv. 2016

@author: YFGI7251
'''
import Mock

Mock.Init()
Mock.Test()



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


MockCompute()

CloseMock()

print(html)