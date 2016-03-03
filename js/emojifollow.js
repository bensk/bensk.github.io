

// Write something to select a random emoji
var myArray = ['⚡️', '💩', '💡', '🍑', '👍', '🌮', '👾', '🖥'];
var rand = myArray[Math.floor(Math.random() * myArray.length)];

 ! function() {
 	document.body.style.cursor = document.body.parentNode.style.cursor = "none"
 	var e = document.createElement("div")
 	e.innerHTML = rand, e.style.fontSize = "30px", e.style.position = "absolute", e.style.zIndex = 9999, e.style.pointerEvents = "none", document.body.appendChild(e), window.addEventListener("mousemove", function(t) {
 		e.style.left = t.pageX + "px", e.style.top = t.pageY + "px"
 	})
 }()
