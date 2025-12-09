// Write a function generateReport that takes an array of BusinessPartner objects. The function should iterate over the array and return a list of strings summarizing the status of each partner:

// If the partner is a Customer, return "Customer - Credit Allowed" or "Customer - Credit Denied" based on isCreditAllowed().
// If the partner is a Supplier, return "Supplier - Shortlisted" or "Supplier - Not Shortlisted" based on isInShortList().

class Customer {
  isCreditAllowed(): boolean {
    // ...
    return true;
  }
}

class Supplier {
  isInShortList(): boolean {
    // ...
    return true;
  }
}

type BusinessPartner = Customer | Supplier;

function generateReport(partners: BusinessPartner[]): any {
  partners.map((partner) => {});
}
