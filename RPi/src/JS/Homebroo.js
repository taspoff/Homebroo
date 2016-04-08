/**
 * 
 */
var PICO=JSON.parse('{ 	"name" : "Pico1",' +
			   '"background" : "./Images/FridayGeekLab_Pico_noIcon.png",' +
			   '"Sensors" : [{"id":"0","URL":"./Data/Sensor1.json"}],'+
			   '"Actors" : [{"id":"0","URL":"./Data/Actor1.json"}],'+
			   '"Junks" : [],'+
			   '"Recipe" : "./Data/Recipe1.json"'+
			  ' }');

var RECIPE=JSON.parse('{"name" : "Basique"}');

var canvas = null;
var context = null;
var BackGround = null;
var TabSensors = [{"id":"0","URL":"./Data/Sensor1.json"}];
var TabActors = [{"id":"0","URL":"./Data/Actor1.json"}];

function Jlog(J,R)
{
	console.log("JLOG=#FG#"+JSON.stringify(J)+"#FG# ["+R+"]");
	}
function Tlog(J,R)
{
	console.log("TLOG=#FG#"+J+"#FG# ["+R+"]");
	}

function getJSON(jURL,Jvalue)
{
	var jReq = new XMLHttpRequest();
	var Temp=""
	var lock=true;
	JsonRet = function(e,Jvalue)
		{Jvalue.push(JSON.parse(unescape(jReq.response)))}
	jReq.addEventListener("load",JsonRet, false);
	jReq.open("get",jURL,true);
	jReq.send();
	Jlog(Jvalue,"Jvalue getJson")
	
}







function Load_Recette()
{
	if (!localStorage.TabRecipe)
		localStorage.TabRecipe='["name":"externe"]';	
	alert(localStorage.TabRecipe);
		
}



//file:///C:\Users\yfgi7251\Documents\Important\Architecture\___Archives\FridayGeekLab\CodeSRC\RPi\src\Data\Pico1.json
function Load_Pico()
{
	var UrlPico = prompt("URL du JSON de votre Pico");
	getJSON(UrlPico,PICO);
	Jlog(PICO,"PICO LoadPico");
	Canva_Update();
}

 function IHM_Update()
{ var Recette=document.getElementById('MenuName');
	Recette.innerHTML="Recette : "+RECIPE.name;
	};

function Sensor_Init(URL,S)
{
	getJSON(URL,S);
	Jlog(S,"S SensorInit");
}

function Sensor_Update(Cont,Sensor)
{
	Im=new Image();
	
	Jlog(Sensor,"Sensor SensorUpdate");
	Im.src=Sensor.Image;
	Im.onload = function() {Cont.drawImage(Im,Sensor.X,Sensor.Y)};
}

function Canva_Init()
{
	 canvas = document.getElementById('DisplayPico');
	 if(!canvas)
     {alert("Impossible de récupérer le canvas"); return; }
	 context = canvas.getContext('2d');
     if(!context)
     {alert("Impossible de récupérer le context du canvas");return;}


     context.clearRect(0, 0, canvas.width, canvas.height);

     ///tracage du background
	 BackGround=new Image();
     BackGround.onload = function() {context.drawImage(BackGround,0,0,640,480)};
 	 BackGround.src=PICO.background; 
 	 
 	 ///tracage des senseurs
 
 	 for( var NS in PICO.Sensors)
 		 {
 		 	Tlog(NS,"NS CanvaInit")
 		 	Jlog(TabSensors[NS],"TabSensor CanvaInit")
 		 	Tlog(PICO.Sensors[NS].URL,"URL Sensor CanvaInit")
 		 	Sensor_Init(PICO.Sensors[NS].URL,TabSensors[NS]);
 		 }
 	 
 	 
	};
	
function Canva_Update()
	{
		context.clearRect(0, 0, canvas.width, canvas.height);

	     ///tracage du background
		 BackGround=new Image();
	     BackGround.onload = function() {context.drawImage(BackGround,0,0,640,480)};
	 	 BackGround.src=PICO.background; 
	 	 Jlog(PICO,"PICO CanvaUpdate");
	 	 ///tracage des senseurs
	 	 
	 	 for( var NS in PICO.Sensors)
	 		 {
	 		 	Jlog(TabSensors[NS],"TabSensor["+NS+"] canvaUpdate")
	 		 	Sensor_Update(context,TabSensors[NS]);
	 		 }
		};	
	
init = function()
{
	Canva_Init();
	
}
loop = function()
{	
	Canva_Update();
	IHM_Update();
	;
}
	

window.onload = function()
{
    init();
	Mainloop = setInterval(loop,500);
              
        
 
};