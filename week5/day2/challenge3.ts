// Define a Car Interface

// Task: Create an interface Car with properties make, model, and year (all strings). Then, write a function getCarInfo that takes a Car object and returns a formatted string with the car's details.

interface Car {
  make: string;
  model: string;
  year: number;
}

function carInfo(car: Car): string {
  return `A ${car.year}, ${car.make} ${car.model}`;
}

let my_car = {
  make: 'Chevy',
  model: 'Camaro',
  year: 1987
};

console.log(carInfo(my_car));
