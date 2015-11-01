var googleColors=function(color, color1, color2, color3){
	var gColor = document.getElementById("g");
	var oColor = document.getElementById("o");
	var o1Color = document.getElementById("o1");
	var g1Color = document.getElementById("g1");
	var lColor = document.getElementById("l");
	var eColor= document.getElementById("e");
	gColor.style.color = color;
	oColor.style.color= color1;
	o1Color.style.color=color2;
	g1Color.style.color=color;
	lColor.style.color=color3;
	eColor.style.color=color1;

}

var blackOut=function(color){
	var gColor = document.getElementById("b");
	var oColor = document.getElementById("e");
	var o1Color = document.getElementById("o1");
	var g1Color = document.getElementById("g1");
	var lColor = document.getElementById("l");
	var eColor= document.getElementById("e");
	gColor.style.color = color;
	oColor.style.color= color;
	o1Color.style.color=color;
	g1Color.style.color=color;
	lColor.style.color=color;
	eColor.style.color=color;

}
