function changeImage() {
    var image = document.getElementById('myImage');
    if (image.src.match("bulbon")) {
        image.src = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/93927/pic_bulboff.gif";
    } else {
        image.src = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/93927/pic_bulbon.gif";
    }
}