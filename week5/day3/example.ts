function getRandomNumberElement(items: number[]): number {
  let randomIndex = Math.floor(Math.random() * items.length);
  return items[randomIndex];
}

function getRandomStringElement(items: string[]): string {
  let randomIndex = Math.floor(Math.random() * items.length);
  return items[randomIndex];
}

function getRandomElement<Type extends number | string>(items: Type[]): Type {
  let randomIndex = Math.floor(Math.random() * items.length);
  return items[randomIndex];
}

let a = [1, 2, 3, 4, 5];
getRandomNumberElement(a);
getRandomElement(a);

let b = ['a', 'b', 'c', 'd'];
// getRandomNumberElement(b) // doesn't work
getRandomStringElement(b);
getRandomElement(b);

let c = ['Etheopia', 'Venesuela', 'Ohio', 'Belgium', 'New York', 22, 15, 99];
getRandomElement(c);
