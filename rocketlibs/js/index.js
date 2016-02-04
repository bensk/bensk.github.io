function madlibs() {
  var story = document.getElementById("story");
  var name = document.getElementById("Name").value;
  var adjective = document.getElementById("Adjective").value;
  var noun = document.getElementById("Noun").value;
  var verb = document.getElementById("Verb").value;
  story.innerHTML = "A" + " " + "important" +" " + noun +" " +" " + "variable" + " " +"named" + " " + name + "'s" + " " + adjective + " " + "rocket boys" + " " + verb + " " + "to" + " " + " the " + " " + "moon" + " ! " + " ! ";
}