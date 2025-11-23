// code code code
console.log('Is everybody with me?');

let myVar;

console.log(myVar);

myVar = 'chicken';

console.log(myVar);

let x = 15;
let y = 18;

let longString = `
One time I took my cat to the park. dog dog doggie.
`;

console.log(longString.indexOf('ook'));

console.log(longString.substring(13, 32));

//
//
// Exercise 1
//
//

// let addressNumber = 55;
// let addressSteet = 'Chicken rd.';
// let country = 'Madagascar';

// console.log('I live at ' + addressNumber + ' ' + addressSteet + ', ' + country);

//
//
// Exercise 2
//
//

let birthYear = 1880;
let futureYear = 1991;
let myAge = futureYear - birthYear;
console.log('I will be ' + myAge + ' in ' + futureYear + '.');

//
//
// Excecise 3
//
//

// 1. Create a numerically indexed table (ie. an array): pets, like this ['cat','dog','fish','rabbit','cow']

let numericallyIndexedTable = ['cat', 'dog', 'fish', 'rabbit', 'cow'];

// 2. Display dog

console.log(numericallyIndexedTable[1]);

// 3. Add to the array pets, the pet horse. Remove the pet rabbit

numericallyIndexedTable.push('horse');
numericallyIndexedTable.splice(3, 1);
console.log(numericallyIndexedTable);

// 4. Display the array length

console.log(numericallyIndexedTable.length);

//
//
// exercise 5
//
//

// Create a stuctured html file linked to a JS file

// 1. Create an object that has properties "username" and "password". Fill those values in with strings.

// 2. Create an array which contains the object you have made above and name the array "database".

// 3. Create an array called "newsfeed" which contains 3 objects with properties "username" and "timeline".

let myObj = {
  username: 'coolguy',
  password: 'password1'
};

let database = [myObj];

let newsfeed = [
  { username: 'chicken nuggest', timeline: 'logged in' },
  { username: 'porcupine', timeline: 'liked a video' },
  { username: 'musicPerson', timeline: 'downvoted a song' }
];

// If statements!!!

// let myNum = prompt('Pick a number');

// if (myNum == 10) {
//   alert('That is a good number!');
// } else if (myNum > 10) {
//   alert('That is a big number');
// } else {
//   alert('That is a little number');
// }

//
//
// exercise 6
//
//

// Make a keyless car!

// This car will only let you drive if you are over 18. Make it do the following:

// Using prompt() and alert(), ask a user for their age.

// IF they say they are below 18, respond with: "Sorry, you are too young to drive this car. Powering off
// IF they say they are 18, respond with: "Congratulations on your first year of driving. Enjoy the ride!
// IF they say they are over 18, respond with: "Powering On. Enjoy the ride!"

// let age = prompt('what is your age');

// if (age < 18) {
//   alert('Too young to drive!');
// } else if (age == 18) {
//   alert('congrats');
// } else {
//   alert('Moving the car');
// }

//
//
// exercise 7
//
//

// Create a structured HTML file linked to a JS file

// 1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen.

// Sample Output: //"0 is even" //"1 is odd" //"2 is even"

for (let i = 0; i <= 15; i++) {
  if (i % 2 === 0) {
    console.log(i + ' is even');
  } else {
    console.log(i + ' is odd');
  }
}

let addressNumber = 55;
let addressSteet = 'Chicken rd.';
let country = 'Madagascar';

// console.log('I live at ' + addressNumber + ' ' + addressSteet + ', ' + country);
console.log(
  `I live at ${addressNumber} ${addressSteet}, ${country}. I have $\{addressStreet\}`
);
