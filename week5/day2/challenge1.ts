class Person {
  constructor(
    // private ssn: string,
    private firstName: string,
    private lastName: string,
    private readonly age: number
  ) {
    // this.ssn = ssn;
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }

  getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }

  public greet(): string {
    return `Hey there, ${this.getFullName()}!`;
  }
}

class Student extends Person {
  constructor(
    // ssn: string,
    firstName: string,
    lastName: string,
    age: number,
    protected studentId: string
  ) {
    super(firstName, lastName, age);
    this.studentId = studentId;
  }
}

// let auggie = new Student('123', 'Augustine', 'Smith', 19, 'tf456');
// let betel = new Person('456', 'Betel', 'Channing', 24);

// console.log(auggie.getFullName());
// console.log(betel.greet());

class Employee extends Person {
  constructor(
    firstName: string,
    lastName: string,
    age: number,
    private jobTitle: string
  ) {
    // call the constructor of the Person class:
    super(firstName, lastName, age);
  }
}

// Define a subclass Manager that extends Employee and includes a private property department.

// class Manager extends Employee {
//   private department: string;

//   constructor(
//     firstName: string,
//     lastName: string,
//     jobTitle: string,
//     department: string
//   ) {
//     super(firstName, lastName, jobTitle);
//     this.department = department;
//   }
// }
