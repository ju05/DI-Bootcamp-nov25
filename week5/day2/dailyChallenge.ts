// Instructions
// Create a simple library system with TypeScript:

// Interface Book: Define an interface Book with the following properties:

// title (string)
// author (string)
// isbn (string)
// publishedYear (number)
// An optional genre property (string)

interface Book {
  title: string;
  author: string;
  isbn: string;
  publishedYear: number;
  genre?: string;
}

// Class Library: Create a class Library with:

// A private property books (array of Book).
// A public method addBook to add a new book to the library.
// A public method getBookDetails that returns details of a book based on the isbn.
// Class DigitalLibrary: Create a class DigitalLibrary that extends Library and adds:

class Library {
  constructor(private books: Book[] = []) {
    this.books = books;
  }

  addBook(book: Book) {
    this.books.push(book);
  }

  getBookDetails(id: string) {
    let myBook = this.books.filter((item) => item.isbn === id);
    return `${myBook.title}, ${myBook.author}, ${myBook.publishedYear}`;
  }
}

// A readonly property website (string) for the library’s website.
// A public method listBooks that returns a list of all book titles in the library.
// Create an instance of DigitalLibrary, add some books to it, and then print out the details of the books and the list of all book titles.
