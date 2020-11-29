class Library():
    week = "Please return the book in one week"

    def __init__(self, ListofBook):
        self.book = ListofBook

    def Avialablebooks(self):
        print("Books Avialable books")
        n = 1
        print("Sno. Books:Qantity")
        for books in self.book:
            print(str(n)+"    " + books + ":"+str(self.book[books]))
            n = n+1

    def Takebook(self):
        Bookname = input("Enter the name of the book to Take: ")
        for books in self.book:
            if books == Bookname:
                a = self.book[Bookname]
                if a > 0:
                    self.book[Bookname] = a-1
                else:
                    print("Book not Avialable")
            else:
                print("Book not found")

    def Returnbook(self):
        Bookname = input("Enter the name of the book to Return: ")
        a = self.book[Bookname]
        self.book[Bookname] = a+1

    def NewBook(self):
        newbook = input("Enter the name of Book to Add in library: ")
        num = int(input("Enter the qantity Available: "))
        self.book.update(newbook, num)


Centrallibrary = Library(
    {"Python": 10, "C++": 9, "HTML": 56, "CSS": 123, "Javascript": 98, "django": 45})
n = True
while n:
    print("\n")
    print("***********Menu**************")
    print("\n")
    print("1.Books availables")
    print("2.Take a book")
    print("3.Return a book")
    print("4.Add a new book in Library")
    print("5.Exit")
    num1 = int(input("Enter the choice:"))
    if num1 == 1:
        Centrallibrary.Avialablebooks()
    elif num1 == 2:
        Centrallibrary.Takebook()
        print(Centrallibrary.week)
    elif num1 == 3:
        Centrallibrary.Returnbook()
    elif num1 == 4:
        Centrallibrary.NewBook()
    elif num1 == 5:
        n = False
