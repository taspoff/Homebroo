const String JPage = "<html><head><title>FG_PID V01</title></head><body><center><Title>Senseur : CHAMP_001</title>IP = CHAMP_000<Frame name='pilotage'><Form target='pilotage' action='http://CHAMP_000/setData' method='get'><P><table><tr><td><LABEL for='Affectation'>Affectation: </LABEL></td><td><INPUT type='text' value='CHAMP_001' name='Affectation'></td></tr><tr><td><LABEL for='wantedTemp'>Temperature desiree: </LABEL></td><td><INPUT type='text' value='CHAMP_002' name='WantedTemp'></td></tr><tr><td><LABEL for='MesureTemp'>Temperature Mesuree: </LABEL></td><td> CHAMP_008</td></tr><tr><td><LABEL for='runingpid'>PID running: </LABEL></td><td><INPUT type='checkbox' value='Up' name='PID' CHAMP_009></td></tr><tr><td><LABEL for='relay'>Etat du relais: </LABEL></td><td><INPUT type='radio' value='Up' name='Relay' CHAMP_003>Up<br><INPUT type='radio' value='Down' name='Relay' CHAMP_004>Down</td></tr><tr><td><LABEL for='ActionRelay'>Action du relais sur la temperature</label></td><td><Input type='radio' value='Heating' name='ActionRelay' CHAMP_005 >Chauffant<BR><Input type='radio' value='Cooling' name='ActionRelay' CHAMP_006 >Refrigerant</td></tr><tr><td><LABEL for='Display'>Emplacement du graphique</LABEL></td><td><INPUT type='text' value='CHAMP_007' name='Display'></td></tr><tr><td></td><td><input type='submit'></td></tr></table></form><IFRAME SRC='http://CHAMP_000/sensor' WIDTH=100% HEIGTH=400></iframe></body></html>";
const String JBanner = "\n\n\n***************************\n***      HomeBruino     ***\n***************************\n\n\n";
