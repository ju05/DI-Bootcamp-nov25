// Write a generic function combine that takes two objects: one representing a user profile and the other representing user preferences. Merge these two objects into a single combined object and demonstrate how it works with different types of inputs.
//

function combined<U, V>(obj1: U, obj2: V) {
  return {
    ...obj1,
    ...obj2
  };
}

let user = { name: 'Goofy', DOB: 1932 };
let profile = { hobbies: ['sleep', 'swimming'] };

combined(user, profile);

// output:
// {name: 'Goofy', DOB: 1932, hobbies: ['sleep', 'swimming']}
