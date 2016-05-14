var c_801 = ["Adam", "Alyzza", "Amerie", "Ana", "Annalis", "Anthony", "Atiba", "Breanna", "Carlos", "Elizabeth", "Emarie", "Emily", "Jaila", "Janna", "Jhon", "Jordan", "Jose", "Joseph", "Kailyn", "Kathryn", "Keishaun", "Leslie", "Mamadou", "Michael", "Natalie", "Rich", "Souvan", "Stephanie", "Tiara", "Tyrell", "Victor"];
var c_803 = ["Alexander", "Anjeliqe", "Antonio", "Ashley", "Benjamin", "Carolyn", "Catherine", "Daina", "David F.", "David K.", "Edgar", "Elaine", "Eric", "Evelyn", "Jared", "Josue", "Juan", "Katia", "Magnelie", "Malene", "Nayeli", "Noe", "Paola", "Patrick", "Shakira", "Soriel", "Tulio", "Vanessa F.", "Vanessa H.", "Yadira"]
var c_804 = ["Adrianna", "Alexander", "Alyssa", "Axel", "Brianna", "Caitlin", "Chanel", "Chasity", "Crystal", "Dallana", "Devonte", "Fatoumata", "Jaron", "Jeremiah", "Jese", "Joncarlo", "Josue", "Keisha", "Kendra", "Luis", "Mariam", "Mariyam", "Matthew", "Mayra", "Melvin", "Nyasia", "Ricardo", "Tanisha", "Xiuya", "Yafer", "Yaritza"]
var econ = ["Anthony", "Bianny", "Charleen", "Christopher", "Darlenis", "Dazhane", "Elias", "Elvis", "Hailey", "Hector", "Jennifer", "Joanna", "Jonathan", "Jose", "Joshua", "Julian", "Julio", "Kellam", "Marlene", "Nephi", "Yennifer"]
var cs_11 = ["Aaron", "Aileen", "Angie", "Bestydanis", "Brionna", "David", "Dayris", "Genesis", "Gregorio", "Grismely", "Ibrahim", "Izaiyah", "James", "Jorge", "Jose", "Justin", "Karen", "Luis", "Marquis", "Michael Chavez", "Michael Delvalle", "Mommina", "Steven", "Vianelys", "Yomaris", "Zaire"]
  // var index;
  // Get a random element from an array

function setup() {
  createCanvas(windowWidth, windowHeight)
  background('white')
    // var index = floor(random(words.length)); // Convert to integer
    // var inp = createInput('');
    // inp.input(myInputEvent);
    // text(words[index],10,50);  // Displays one of the four words

  button801 = createButton("801")
  button801.position(windowWidth / 7, 10);
  button801.touchStarted(popsicle801);
  button803 = createButton("803")
  button803.position(3 * windowWidth / 7, 10);
  button803.touchStarted(popsicle803);
  button804 = createButton("804")
  button804.position(5 * windowWidth / 7, 10);
  button804.touchStarted(popsicle804);

}



function popsicle801() {
  background('white')
    // line(0, 0, 50, 50)
    // text(words[1], 10, 50)
  textSize(32)
  text(String(c_801[floor(random(c_801.length))]), windowWidth / 7, 100); // Displays one of the four words

}

function popsicle803() {
  background('white')
    // line(0, 0, 50, 50)
    // text(words[1], 10, 50)
  textSize(32)
  text(String(c_803[floor(random(c_801.length))]), 3 * windowWidth / 7, 100); // Displays one of the four words

}

function popsicle804() {
  background('white')
    // line(0, 0, 50, 50)
    // text(words[1], 10, 50)
  textSize(32)
  text(String(c_804[floor(random(c_801.length))]), 5 * windowWidth / 7, 100); // Displays one of the four words

}


function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}