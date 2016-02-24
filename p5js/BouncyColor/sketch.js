var circleX; //=random(0, width);
var circleY; //=random(0, height);
var xDirection=1;
var yDirection=1;
var speed=10.5;


function setup() {
  
  createCanvas(windowWidth, windowHeight);
  circleX=random(0, width);
  circleY=random(0, height);
  background(255, 255, 255);
}

function draw() {


  fill(circleY, circleX, random(100, 250));
  ellipse(circleX, circleY, 100, circleX);
  circleX=circleX+xDirection*speed;
  circleY=circleY+yDirection*speed;
  // Try || pipes for 'or' next time
  if (circleX>=width-50) {
    xDirection=xDirection*-1;
  } else if (circleX<=0) {
    xDirection=xDirection*-1;
  }
  if (circleY>=height) {
    yDirection=yDirection*-1;
  } else if (circleY<=0) {
    yDirection=yDirection*-1;
  }
  println("circleX: "+ circleX, "circleY: "+ circleY);
  
}


function keyPressed() {
  background(255, 255, 255);
  
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}