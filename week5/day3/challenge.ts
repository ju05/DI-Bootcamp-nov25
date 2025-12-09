interface BusinessPartner {
  name: string;
  credit: number;
}

interface Identity {
  id: number;
  name: string;
}

interface Contact {
  email: string;
  phone: string;
}

// Define a type Customer as an intersection type of BusinessPartner and Contact. Create an instance of the Customer type and initialize it with the appropriate properties.

type Customer = BusinessPartner & Contact;

let cusomer: Customer = {
  name: 'Billy',
  credit: 1000000,
  email: 'billy@bob.com',
  phone: '(212)879-4877'
};
