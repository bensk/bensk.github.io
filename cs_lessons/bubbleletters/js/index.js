var red = [0, Math.floor(Math.random()*255), Math.floor(Math.random(20)*60)];
var orange = [40, Math.floor(Math.random()*255), 60];
var green = [75, Math.floor(Math.random()*255), 40];
var blue = [Math.floor(Math.random(150)*200), Math.floor(Math.random()*255), 55];
var purple = [Math.floor(Math.random()*255), 50, 60];

var myName = "Code!";
var letterColors=[red,orange,green,blue,purple]
if (1>0){
    bubbleShape="circle";
} else{
    bubbleShape="square";
}


drawName(myName, letterColors);
bounceName();
bounceBubbles();