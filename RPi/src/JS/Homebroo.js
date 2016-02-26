/**
 * 
 */
var PICO=JSON.parse('{ 	"name" : "Pico1",' +
			   '"background" : "./Images/FridayGeekLab_Pico_noIcon.png",' +
			   '"NbSensors":1,' +
			   '"Sensors" : [{"URL":"./Data/Sensor1.json"}],'+
			   '"NbActors":1,'+
			   '"Actors" : [{"URL":"./Data/Actor1.json"}],'+
			   '"NbJunks" : 0,'+
			   '"Junks" : [],'+
			   '"Recipe" : "./Data/Recipe1.json"'+
			  ' }');
var RECIPE=JSON.parse('{"name" : "Basique"}');

var canvas = null;
var context = null;

IHM_Update = function()
{ var Recette=document.getElementById('MenuName');
	Recette.innerHTML="Recette : "+RECIPE.name;
	};


IHM_Update = function()
{ var Recette=document.getElementById('MenuName');
	Recette.innerHTML="Recette : "+RECIPE.name;
	};

Canva_update = function()
{
	 canvas = document.getElementById('DisplayPico');
	 if(!canvas)
     {alert("Impossible de récupérer le canvas"); return; }
	 context = canvas.getContext('2d');
     if(!context)
     {alert("Impossible de récupérer le context du canvas");return;}
     
	 BackGround=new Image();
     BackGround.onload = function() {context.drawImage(BackGround,0,0,640,480)};
 	 BackGround.src=PICO.background; 
	};

window.onload = function()
{
    
		Canva_update();
    //C'est ici que l'on placera tout le code servant à nos dessins.       
        IHM_Update();
              
        
 
};