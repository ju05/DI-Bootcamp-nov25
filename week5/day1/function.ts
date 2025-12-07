function add(x: number, y: number): number {
  return x + y;
}

// Write code that attempts to call the add function with arguments of different types. Observe the compile-time error message.

const first = add(1, 4);
// const second = add('3', 6);
// const third = add(7, true);

console.log(first);
