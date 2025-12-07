let myNums: number[] = [];

myNums.push(9);
myNums.push(19);
myNums.push(91);
myNums.push(89745);

myNums.pop();

let myOtherNums: [number, number, string] = [1, 2, 'a'];
myOtherNums.push(99);

myOtherNums.pop();
myOtherNums.pop();

let myVar: any = 'Augustin';
myVar = 44;
myVar = [1, 2, 3, 4];

let food: string | boolean = 'falafel';
food = 'hamburger';
food = true;
// food = 22;

function isAllowed(action: number | string): boolean {
  if (typeof action == 'string') return true;
  else {
    return false;
  }
}

type aaron = boolean | string;
let guy: aaron = 'Wolf';
guy = true;
guy = false;
// guy = 55
