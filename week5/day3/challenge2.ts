interface typeA {
  isNeat: boolean;
  color: string;
}

interface typeB {
  isArgentinian: boolean;
  drinkMate: boolean;
}

type Augustin = typeA & typeB;

let augustin: Augustin = {
  isNeat: true,
  color: 'turquoise',
  isArgentinian: true,
  drinkMate: true
};

type Betel = typeB & typeA;

let betel: Betel = {
  isNeat: true,
  color: 'cream',
  isArgentinian: false,
  drinkMate: false
};
