function madlibs() {
  var story = document.getElementById("story");

  var adjective = document.getElementById("Adjective").value;
  var noun = document.getElementById("Noun").value;
  var noun1 = document.getElementById("Noun1").value;
  var verb = document.getElementById("Verb").value;
  var noun2 = document.getElementById("Noun2").value;
  story.innerHTML = "When building rockets, don't rely on " + noun + ". First, you need to come up with a " + adjective + " hypothesis for your project. If your experiment doesn't work (or is destroyed on impact), you will need to adjust your calculation. Another considerable factor in building rockets is " + noun1 + ". You need to generate sufficient thrust in order to " + verb + " correctly. You should also integrate " + noun2 + " into your design.";
}

