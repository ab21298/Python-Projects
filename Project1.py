# creating a class library (oops MINI project)
#   - show books
#   - lend book
#   - add book
#   - return book


class Library:
    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {}

    def show_Book(self):
        for book in self.booklist:
            print(book)

    def lend_Book(self, name, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: name})
            print(f"Lender-Book Dictionary has been updated successfully You can take your book now")
        else:
            print(f"Book is already used by {self.lendDict[book]}")

    def add_book(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list of the library.")

    def return_book(self, book):
        self.lendDict.pop(book)
        print("Book returned.")

    def show_lended(self):
        i = 1
        for book in self.lendDict.keys():
            print(f"{i} - {book} lended by {self.lendDict[book]}")
            i = i + 1


if __name__ == '__main__':
    ab = Library(['python', 'c++', 'cyber security', 'java', 'web development'], "AB Library")
    print(f"Welcome to {ab.name} ! ")
    while True:
        print("Enter Your Choice to Continue")
        print("1 - Display Book")
        print("2 - Lend Book")
        print("3 - Add Book")
        print("4 - Return Book")
        print("5 - show lended Book")
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Enter a valid number")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            ab.show_Book()
        elif user_choice == 2:
            book = input("Enter the name of the book You want to Lend : ")
            name = input("Enter Your name : ")
            ab.lend_Book(name, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add : ")
            ab.add_book(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return : ")
            ab.return_book(book)
        elif user_choice == 5:
            ab.show_lended()
        else:
            print("Enter a valid option")

        print("Press q to Quit and c to continue")
        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input().lower()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
