#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <PID_v1.h>


#define DS18B20 0x28     // Adresse 1-Wire du DS18B20
#define BROCHE_ONEWIRE 2 // Broche utilisée pour le bus 1-Wire
#define BROCHE_RELAY 0
#define DEBUG 1
#define DHCP 1


const char* DNS = "FG_ESPID_02";
//const char* ssid = "Livebox_Taspoff";
//const char* password = "Athena_96";
const char* ssid = "Livebox-77b6";
const char* password = "kartopulimon";
//const char* ssid = "Livebox-F444";
//const char* password = "6F1A2A23E2FF676769319C7C91";

const uint8_t myIP[4]={192,168,1,213};
const uint8_t myMask[4]={255,255,255,0};
const uint8_t myDNS[4]={192,168,1,1};
const uint8_t myGateway[4]={192,168,1,1};


MDNSResponder mdns;
ESP8266WebServer server(80);



OneWire  dso(BROCHE_ONEWIRE);
DallasTemperature ds(&dso);
DeviceAddress dsMac;

boolean relay = 0;
boolean runPID = 0;
String actionRelay = "Heating";
double wantedTemp = 50.0;
double tempSensor,Output;
PID myPID(&tempSensor, &Output, &wantedTemp,100,100,100, DIRECT);

int WindowSize = 10000;
unsigned long windowStartTime,timeTemp;


String affectation = "N-A";
String urldisplay = "truc";

void LOG(String S) {
  if (DEBUG) Serial.println(S);
}


void handleFrame() {
  String Page;
  Page = "<html><head><title>FG_PID V01</title></head>";
  Page += "<FRAMESET row='30%,70%'><Frame name='console' src='http://CHAMP_000/console'></frame><frame name='sensor' src='http://CHAMP_000/sensor'></frame></HTML>";
  String IP;
  IPAddress IPA;
  IPA=WiFi.localIP();
  IP=String(IPA[0])+"."+String(IPA[1])+"."+String(IPA[2])+"."+String(IPA[3]);
  Page.replace("CHAMP_000", IP);
  server.send(200, "text/html", Page);
}

void  handleFrameConsole() {
  String Page;
  Page = "<html><head><title>FG_PID V01</title></head>";
  Page += "<body><center><Title>Senseur : CHAMP_001</title> IP = CHAMP_000";
  Page += "<Frame name='pilotage'> <Form target='pilotage' action='http://CHAMP_000/setData' method='get'><P>";
  Page += "<table><tr><td><LABEL for='Affectation'>Affectation: </LABEL></td>";
  Page += "<td><INPUT type='text' value='CHAMP_001' name='Affectation'></td></tr>";
  Page += "<tr><td><LABEL for='wantedTemp'>Temperature desiree: </LABEL></td>";
  Page += "<td><INPUT type='text' value='CHAMP_002' name='WantedTemp'></td></tr>";
  //Page += "<tr><td><LABEL for='MesureTemp'>Temperature Mesuree: </LABEL></td><td> CHAMP_008</td></tr>";
  Page += "<tr><td><LABEL for='runingpid'>PID running: </LABEL></td>";
  Page += "<td><INPUT type='checkbox' value='Up' name='PID' CHAMP_009></td></tr>";
  Page += "<tr><td><LABEL for='relay'>Etat du relais: </LABEL></td>";
  Page += "<td><INPUT type='radio' value='Up' name='Relay' CHAMP_003>Up<br><INPUT type='radio' value='Down' name='Relay' CHAMP_004>Down</td></tr>";
  Page += "<tr><td><LABEL for='ActionRelay'>Action du relais sur la temperature</label></td>";
  Page += "<td><Input type='radio' value='Heating' name='ActionRelay' CHAMP_005 >Chauffant<BR>";
  Page += "<Input type='radio' value='Cooling' name='ActionRelay' CHAMP_006 >Refrigerant</td></tr>";
  Page += "<tr><td><LABEL for='Display'>Emplacement du graphique</LABEL></td><td><INPUT type='text' value='CHAMP_007' name='Display'></td></tr>";
  Page += "<tr><td></td><td><input type='submit'></td></tr>";
  Page += "</table></form>";
  Page += "</body></html>";
  String IP;
  IPAddress IPA;
  tempSensor=ds.getTempC(dsMac);
  IPA=WiFi.localIP();
  IP=String(IPA[0])+"."+String(IPA[1])+"."+String(IPA[2])+"."+String(IPA[3]);
  Page.replace("CHAMP_000", IP);
  Page.replace("CHAMP_001", affectation);
  Page.replace("CHAMP_002", String(wantedTemp));
  if (relay == 1) {
    Page.replace("CHAMP_003", " checked ");
    Page.replace("CHAMP_004", "");
  }
  else {
    Page.replace("CHAMP_003", "");
    Page.replace("CHAMP_004", " checked ");
  };

  if (actionRelay.equals("Heating")) {
    Page.replace("CHAMP_005", " checked ");
    Page.replace("CHAMP_006", "");
  }
  else {
    Page.replace("CHAMP_005", "");
    Page.replace("CHAMP_006", " checked ");
  };
 Page.replace("CHAMP_007", urldisplay);
 Page.replace("CHAMP_008", String(tempSensor));

   if (runPID) {
    Page.replace("CHAMP_009", " checked ");
  
  }
  else {
    Page.replace("CHAMP_009", "");
 
  };

  server.send(200, "text/html", Page);
}

String JoliePage() {
  String Page;
  Page = "<html><head><title>FG_PID V01</title></head>";
  Page += "<body><center><Title>Senseur : CHAMP_001</title> IP = CHAMP_000";
  Page += "<Frame name='pilotage'> <Form target='pilotage' action='http://CHAMP_000/setData' method='get'><P>";
  Page += "<table><tr><td><LABEL for='Affectation'>Affectation: </LABEL></td>";
  Page += "<td><INPUT type='text' value='CHAMP_001' name='Affectation'></td></tr>";
  Page += "<tr><td><LABEL for='wantedTemp'>Temperature desiree: </LABEL></td>";
  Page += "<td><INPUT type='text' value='CHAMP_002' name='WantedTemp'></td></tr>";
  Page += "<tr><td><LABEL for='MesureTemp'>Temperature Mesuree: </LABEL></td><td> CHAMP_008</td></tr>";
  Page += "<tr><td><LABEL for='runingpid'>PID running: </LABEL></td>";
  Page += "<td><INPUT type='checkbox' value='Up' name='PID' CHAMP_009></td></tr>";
  Page += "<tr><td><LABEL for='relay'>Etat du relais: </LABEL></td>";
  Page += "<td><INPUT type='radio' value='Up' name='Relay' CHAMP_003>Up<br><INPUT type='radio' value='Down' name='Relay' CHAMP_004>Down</td></tr>";
  Page += "<tr><td><LABEL for='ActionRelay'>Action du relais sur la temperature</label></td>";
  Page += "<td><Input type='radio' value='Heating' name='ActionRelay' CHAMP_005 >Chauffant<BR>";
  Page += "<Input type='radio' value='Cooling' name='ActionRelay' CHAMP_006 >Refrigerant</td></tr>";
  Page += "<tr><td><LABEL for='Display'>Emplacement du graphique</LABEL></td><td><INPUT type='text' value='CHAMP_007' name='Display'></td></tr>";
  Page += "<tr><td></td><td><input type='submit'></td></tr>";
  Page += "</table></form>";
  Page += "<IFRAME SRC='http://CHAMP_000/sensor' WIDTH=100% HEIGTH=400></iframe>";
  Page += "</body></html>";
  String IP;
  IPAddress IPA;
  tempSensor=ds.getTempC(dsMac);
  IPA=WiFi.localIP();
  IP=String(IPA[0])+"."+String(IPA[1])+"."+String(IPA[2])+"."+String(IPA[3]);
  Page.replace("CHAMP_000", IP);
  Page.replace("CHAMP_001", affectation);
  Page.replace("CHAMP_002", String(wantedTemp));
  if (relay == 1) {
    Page.replace("CHAMP_003", " checked ");
    Page.replace("CHAMP_004", "");
  }
  else {
    Page.replace("CHAMP_003", "");
    Page.replace("CHAMP_004", " checked ");
  };

  if (actionRelay.equals("Heating")) {
    Page.replace("CHAMP_005", " checked ");
    Page.replace("CHAMP_006", "");
  }
  else {
    Page.replace("CHAMP_005", "");
    Page.replace("CHAMP_006", " checked ");
  };
 Page.replace("CHAMP_007", urldisplay);
 Page.replace("CHAMP_008", String(tempSensor));

   if (runPID) {
    Page.replace("CHAMP_009", " checked ");
  
  }
  else {
    Page.replace("CHAMP_009", "");
 
  };
  LOG (Page);
  return Page;
}



void handleGetTemp() {

  String Ret;
  Ret = "{\"Sensor\":\"" + String(DNS) + "\",\"Temp\":" + String(tempSensor) + "}";
  server.send(200, "text/plain", Ret);
  LOG(Ret);
  
}

void handleFrameSensor() {

  String Ret;
  Ret = "<html><head><meta http-equiv='refresh' content='2'></head><body>Sensor " + String(DNS) + " :" + String(tempSensor) + " <SUP>o</SUP>C <br>Chauffage  "+String((Output/WindowSize*100))+" % </body></html>";
  server.send(200, "text/html", Ret);
  LOG(Ret);
  
}

void handleGetRelay() {
  String Ret, stateRelay;
  if (relay)
    stateRelay = "Up";
  else
    stateRelay = "Down";
  Ret = "{\"Sensor\":\"" + String(DNS) + "\",\"Relay\":\"" + stateRelay + "\"}";
  server.send(200, "text/plain", Ret);
  LOG(Ret);
}

void handleSetRelay() {
  String stateRelay;
  stateRelay = server.arg("Relay");
  if (stateRelay == "Up") {
    relay = 1;
    digitalWrite(BROCHE_RELAY, HIGH);
    LOG("UP de Relay");
  }
  else {
    if (stateRelay == "Down") {
      relay = 0;
      digitalWrite(BROCHE_RELAY, LOW);
      LOG("DOWN de Relay");
    }
  }
}
void handleSetActionRelay() {
  actionRelay = server.arg("ActionRelay");
  LOG("MAJ de actionrelay = "+actionRelay);
}
  
void handleSetAffectation() {
  affectation = server.arg("Affectation");
  LOG("MAJ de affectation = "+affectation);
}

void handleSetWantedTemp() {
  wantedTemp = server.arg("WantedTemp").toFloat();
  LOG("MAJ de wantedTemp : "+String(wantedTemp));
}

void handleSetData() {
  
  String gPID = server.arg("PID");
  runPID=0;
  if(gPID.equals("Up")) runPID=1;
  handleSetRelay();
  handleSetAffectation();
  handleSetWantedTemp();
  handleSetActionRelay();
  handleRoot();
}

void handleStartPID() {
  runPID=1;
  handleRoot();
}
void handleStopPID() {
  runPID=0;
  handleRoot();
}
void handleRoot() {
  String Ret;
  Ret = JoliePage();
  server.send(200, "text/html", Ret) ;
}

void handleNotFound() {

  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);

}
void printAddress(DeviceAddress deviceAddress)
{
  for (uint8_t i = 0; i < 8; i++)
  {
    if (deviceAddress[i] < 16) Serial.print("0");
    Serial.print(deviceAddress[i], HEX);
  }
}
void setup(void) {


  Serial.begin(115200);
  pinMode(BROCHE_RELAY,OUTPUT);
  WiFi.begin(ssid, password);
  Serial.println("");
  if(!DHCP){
    WiFi.config(IPAddress(myIP),IPAddress(myGateway),IPAddress(myMask));
  }

  // Wait for connection
  ds.begin();
   Serial.print("Found ");
   Serial.print(ds.getDeviceCount(), DEC);
    Serial.println(" 18B20 devices.");
    Serial.print("Parasite power is: "); 
    if (ds.isParasitePowerMode()) Serial.println("ON");
    else Serial.println("OFF");
      if (!ds.getAddress(dsMac, 0)) Serial.println("Unable to find address for Device 0"); 
  Serial.print("Device 0 Address: ");
  printAddress(dsMac);
  Serial.println();
  ds.setResolution(dsMac,9);

windowStartTime = millis(); timeTemp=windowStartTime;
myPID.SetOutputLimits(0, WindowSize);  
myPID.SetMode(AUTOMATIC);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (mdns.begin("ESP1", WiFi.localIP())) {
    Serial.println("MDNS responder started");
  }

  server.on("/", handleRoot);
  server.on("/1", handleFrame);
  server.on("/getTemp", handleGetTemp);
  server.on("/getRelay", handleGetRelay);
  server.on("/setRelay", handleSetRelay);
  server.on("/startPID", handleStartPID);
  server.on("/stopPID", handleStopPID);
  server.on("/setData", handleSetData);
  server.on("/sensor", handleFrameSensor);
  server.on("/console", handleFrameConsole);
  
  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
 unsigned long now = millis();
 server.handleClient();
 if(now-2000>timeTemp)
 {
   ds.requestTemperatures();
  tempSensor=ds.getTempC(dsMac);
  timeTemp=now;
 }
 if(runPID)
 {
  myPID.Compute();
  if(now - windowStartTime>WindowSize)
  { //time to shift the Relay Window
    windowStartTime += WindowSize;
  }
  if(Output > now - windowStartTime) 
    { relay = 1;
    digitalWrite(BROCHE_RELAY, HIGH);
    LOG("UP de Relay");}
    
  else 
    { relay = 0;
      digitalWrite(BROCHE_RELAY, LOW);
      LOG("DOWN de Relay");
    }
 }
}
