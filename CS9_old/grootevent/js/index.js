var changeImage=function() {
    var image = document.getElementById('myImage');
    if (image.src.match("Groot.png")) {
        image.src = "Groot.gif";
    } else {
        image.src = "Groot.png";
    }
}