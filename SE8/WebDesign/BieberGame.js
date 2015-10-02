// Under the existing code, declare a variable age.
// Make age equal to prompt("What's your age");. See the example above.
// Then write an if/else statement. If age is less than 13, use console.log to tell the user that they're allowed to play but you take no responsibility.
// Else, use console.log and give them an encouraging message to play on!
confirm("Are you ready?");
var age = prompt("What is your age?"); // Question! & Answer
if (age < 13){ // Conditional!
  console.log("You're too young!")
} else {
  console.log("You're too old!")
}

// Question --> answer --> variable --> conditional


// Under your existing code, print out the storyline: "Suddenly, Bieber stops and says, 'Who wants to race me?'"
// Then declare a variable userAnswer. Make it equal a prompt that asks the user "Do you want to race Bieber on stage?". This will be the question that you ask your user.

console.log("Suddenly, Bieber stops and says, 'Who wants to race me?'")

var userAnswer=prompt("Do you want to race Bieber on stage?")

if(userAnswer==="YES"){
  console.log("You and Bieber start racing. It's neck and neck! You win by a shoelace!") } else {
    console.log("You and Bieber start racing. It's neck and neck! You win by a shoelace!")
  }


//   Create a variable called feedback and prompt the user to rate your game out of 10.
//
// If feedback is greater than 8, print out: "Thank you! We should race at the next concert!"
//
// Otherwise, print out:
// "I'll keep practicing coding and racing."

var feedback = prompt("Please rate my stupid stupid game")
if(feedback>8){
  console.log("Thank you! We should race at the next concert!")
} else {
  console.log("I'll keep practicing coding and racing.")
}
