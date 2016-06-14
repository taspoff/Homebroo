struct configWifi {
   char* DNS;
   char* ssid;
   char* password;
   boolean DHCP;
   uint8_t IP[4];
   uint8_t Mask[4];
   uint8_t Gateway[4];
};

const size_t nbRetryWifi = 20;
const size_t nbWifi = 3;
const configWifi tabWifi[nbWifi]= {
  {"Homebruino_FG",
    "Livebox-Taspoff",
    "xxxx",
    0,
    {192,168,1,213},
    {255,255,255,0},
    {192,168,1,1}
  },
  {"Homebruino_Boulot",
    "Livebox-77b6",
    "kartopulimon",
    0,
    {192,168,1,214},
    {255,255,255,0},
    {192,168,1,1}
  },
  {"Homebruino_LesVans",
    "Livebox-F444",
    "6F1A2A23E2FF676769319C7C91",
    0,
    {192,168,1,213},
    {255,255,255,0},
    {192,168,1,1}
  }
};

