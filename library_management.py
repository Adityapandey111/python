class Book:
    def __init__(self,id,name,author,noc):
        self.book_id=id
        self.book_name=name
        self.author=author
        self.copies_available=noc

    def __str__(self):
        return f"book id : {self.book_id}, book : {self.book_name}, author : {self.author}, available copies : {self.copies_available}"


class Member:
    borrowed_books=[]
    def __init__(self,id,name):
        self.m_id=id
        self.name=name
        # self.borrowed_books=b
    def __str__(self):
        return f"member id : {self.m_id}, Name : {self.name}, borrowed books : {self.borrowed_books}"



class Library:
    books=dict()
    members=dict()

    def add_book(self,book):
        self.books[book.book_id]=book
    
    def register_member(self,member: Member):
        self.members[member.m_id]=member
    
    def find_book_by_title(self,title: str):
        list=[]

        for key,value in self.books.items():
            title=value.book_name
            if str==title:
                list.append(value)
        
        return list

    def issue_book(self,member_id: int, book_id: int):
        flag=False
        for key,value in self.books.items():
            if key==book_id and value.copies_available>=1:
                for k,v in self.members.items():
                    if member_id==v.m_id:
                        v.borrowed_books.append(value)
                        value.copies_available-=1
                        flag=True
                        break
        if not flag:
            print("Book is not available")

    
    def accept_return(self,member_id: int, book_id: int):
        for key in self.members.keys():
            if member_id==key:
                book=self.books[book_id]
                self.members[key].borrowed_books.remove(book)
                self.books[book_id].copies_available+=1

    
    def show_all_books(self):
        for value in self.books.values():
            # print(f"book_id : {value.book_id},book : {value.book_name}, author : {value.author}, copies : {value.copies_available}")
            print(value)

    def show_all_members(self):
        for value in self.members.values():
            # print(value)
            print(f"member id : {value.m_id},name : {value.name}")
            if len(value.borrowed_books)>0:
                print("<=:borrowed books:=>")
                for x in value.borrowed_books:
                    print(f"book_id : {x.book_id},book : {x.book_name}, author : {x.author}")




library = Library()


book1 = Book(101, "The Alchemist", "Paulo Coelho", 5)
book2 = Book(102, "1984", "George Orwell", 2)
# print(book1)
library.add_book(book1)
library.add_book(book2)


member1 = Member(1, "Alice")
member2 = Member(2, "Bob")
library.register_member(member1)
library.register_member(member2)


library.issue_book(1, 101)
library.issue_book(2, 102)


library.show_all_books()


library.show_all_members()

print("<-------------------after returning the books----------------------->")

library.accept_return(1,101)
library.accept_return(2,102)

library.show_all_books()
library.show_all_members()