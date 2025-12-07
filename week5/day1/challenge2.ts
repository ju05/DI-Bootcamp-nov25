// 1. Type Inference: Create a variable greeting with a string value and let TypeScript infer its type.

// 2. Type Annotations: Create a function subtract that takes two numbers as arguments and returns their difference. Use type annotations for both the parameters and the return type.

// Bonus: Try changing the inferred type variable to a different type (e.g., assign a number to greeting) and observe the TypeScript error

let greeting = 'Ahoy!';

function subtract(num1: number, num2: number): number {
  return num1 - num2;
}

let myBool: boolean = !true;
