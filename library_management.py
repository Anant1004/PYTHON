class library_management:
    def __init__(self):
        self.No_of_books = 0
        self.Books = []

    def add_Book(self,book):
        self.Books.append(book)
        self.No_of_books = len(self.Books)
    
    def show_info (self):
        print(f"The total books in the library are : {self.No_of_books}")
        print(f"The books are listed below")
        for book in self.Books:
            print(book)


l1  = library_management()
l1.add_Book("harry potter")
l1.add_Book("haris beny")
l1.add_Book("lucy gravel") 
l1.add_Book("flamingo")

l1.show_info()