class Member:
    def __init__(self,name,membership_id):
       self.name=name
       self.membership_id=membership_id
    def display_info(self):
        print(f"Name:{self.name} , Membership ID:{self.membership_id}")
class StudentMember(Member):
    def __init__(self,name,membership_id):
        super().__init__(name,membership_id)
        self.borrowed_books=[]
    def add_books(self,book_title):
        self.borrowed_books.append(book_title)
        print(f"{book_title} has been added to {self.name}'s borrowed books.")
    def return_books(self,book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            print(f"{book_title} has been removed by {self.name}")
        else:
            print(f"{self.name} has not borrowed {book_title}")
    def display_borrowed_book_status(self):
        print(f"{self.name}'s borrowed books {','.join(self.borrowed_books) if self.borrowed_books else 'no books borrowed.'}")
        if self.borrowed_books:
            print("Books: ")
            for book in self.borrowed_books:
                print(f"-{book}")
            
#Test
Student = StudentMember("John","r234")
Student.display_info()
Student.add_books("The World War")
Student.add_books("Advance Computer Architecture")
Student.display_borrowed_book_status()
Student.return_books("The World War")
Student.display_borrowed_book_status()

