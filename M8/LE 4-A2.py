class Library:
    def __init__(self, list_of_books, name):
        self.booksList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have the following books in our library:{self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.booksList:
            print("Sorry,we do not have that book.")
        elif book in self.lendDict:
            print(f"The book is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book]=user
            print(
                "Lender-Book database has been updated.You can take the book  now"
            )
    
    def addBook(self,book):
        if book not in self.booksList:
            self.booksList.append(book)
            print(f"{book} has been added to the book list.")
        else:
            print(f"{book} already exist in the library.")

    def returnBook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]   
            print("Book has been returned.")
        else:
            print("That book wasnt borrowed from us.")

if __name__=='__main__':
    books = Library(["python",
                     'Rich Das Poor Dad',
                     'Harry potter',
                     'c++ Basics',
                     'Algorithms by CLRS'],"Let's Upskill") 
user_name = input("Welcome to our library! Please enter your name: ")

while True:
    print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:")

    print("1. Display Books\n 2. Lend a Book\n 3. Add a Book\n 4. Return a Book\n 5. Quit")

    user_choice = input("Enter your choice to continue: ")

    if user_choice not in ['1', '2', '3', '4', '5']:
        print("Please enter a valid option.")
        continue

    if user_choice == '1':
        books.displayBooks()
    elif user_choice == '2':
        book = input("Enter the name of the book you want to lend: ")
        books.lendBook(user_name, book)
    elif user_choice == '3':
        book = input("Enter the name of the book you want to add: ")
        books.addBook(book)
    elif user_choice == '4':
        book = input("Enter the name of the book you want to return: ")
        books.returnBook(book)
    elif user_choice == '5':
        print(f"Thank you for using the library, {user_name}. Goodbye!")
        break