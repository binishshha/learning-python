class Book:
    def __init__(self,title,author,total_copies):
        self.title=title
        self.author=author
        self.__total_copies=total_copies
        self.__borrowed_copies=0

    
    def borrow_book(self,name):
        if self.__borrowed_copies>=self.__total_copies:
            print(f"book:{name} is not available right now!!! ")
        else:
            self.__borrowed_copies+=1
            print(f"borrowed")

    def return_book(self,name):
        if name in self.title:
                self.__borrowed_copies-=1
                print(f"{name} book returned")
        else:
                print("no such book borrowed")

    def display_info(self,name):
        print(f"Book's title:{self.title}")
        print(f"Book's author:{self.author}")
        print(f"Total copies:{self.__total_copies}")
        print(f"borrowed copies:{self.__borrowed_copies})")

# lets you store multiple books
class Library:
    def __init__(self):
        self.books={}

    def add_books(self,title,author,total_copies):
        if title in self.books.keys():
            print("already exists!!!!!!")
        else:
            self.books.update({title:Book(title,author,total_copies)})
            print("Added")
    
    def check_books(self,name):
        if name in self.books:
             return self.books[name]
        else:
            print("no book available!!!!")

    def display_book(self, title):
        if title in self.books:
            self.books[title].display_info(title)
        else:
            print(f"Book '{title}' not found!")
    
    def borrow_book(self, title):
        if title in self.books:
            self.books[title].borrow_book(title)
        else:
            print(f"Book '{title}' not found!")

    def return_book(self, title):
        if title in self.books:
            self.books[title].return_book(title)
        else:
            print(f"Book '{title}' not found!")

library=Library()

while True:
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Display Book Info")
    print("5. Exit")

    choice=(input("enter a choice:"))

    if choice=="1":
         name=input("enter a book title:")
         author=input("enter the author of the book:")
         copies=int(input("enter the total copies:"))
         library.add_books(name,author,copies)
    
    elif choice == "2":
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)

    elif choice == "3":
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == "4":
        title = input("Enter book title to display: ")
        library.display_book(title)

    elif choice == "5":
        break

    else:
        print("Invalid choice!!!!!!!!!!!!")