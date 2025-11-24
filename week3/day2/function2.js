// 1. Create a structured HTML file linked to a JS file

// 2. Write a Javascript function that takes a parameter: myAge

// 3. In the function, return the age of my mum (my mum is twice my age)

// 4. Call the function

// 5. In the global scope, console.log the result of the function

function ageCalc(myAge) {
  const mum = myAge * 2;
  const dad = mum * 1.2;

  return `Mum is ${mum} years old, and Dad is ${dad} years old.`;
}

console.log(ageCalc(75));
