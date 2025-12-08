class Person {
  constructor(private firstName: string, private lastName: string) {
    this.firstName = firstName;
    this.lastName = lastName;
  }
  getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
  describe(): string {
    return `This is ${this.firstName} ${this.lastName}.`;
  }
}

class Employee extends Person {
  constructor(firstName: string, lastName: string, private jobTitle: string) {
    super(firstName, lastName);
  }

  describe(): string {
    return super.describe() + ` I'm a ${this.jobTitle}.`;
  }
}

class Manager extends Employee {
  private static headcount: number = 0;
  private department: string;

  constructor(
    firstName: string,
    lastName: string,
    jobTitle: string,
    department: string
  ) {
    super(firstName, lastName, jobTitle);
    this.department = department;
  }

  describe(): string {
    return super.describe() + `I work in the ${this.department} department`;
  }
}

let mabratu = new Manager('Mabratu', 'Smith', 'Dept head', 'high tech');
console.log(mabratu.describe()); // This is Mabaratu Smith. I'm a Dept head.
