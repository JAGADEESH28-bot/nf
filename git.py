import json
import os

class LibraryManagementSystem:
    def __init__(self):
        self.books_file = 'books.json'
        self.members_file = 'members.json'
        self.load_data()

    def load_data(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r') as f:
                self.books = json.load(f)
        else:
            self.books = []

        if os.path.exists(self.members_file):
            with open(self.members_file, 'r') as f:
                self.members = json.load(f)
        else:
            self.members = []

    def save_data(self):
        with open(self.books_file, 'w') as f:
            json.dump(self.books, f, indent=4)
        with open(self.members_file, 'w') as f:
            json.dump(self.members, f, indent=4)

    def add_book(self, title, author, isbn):
        self.books.append({'title': title, 'author': author, 'isbn': isbn})
        self.save_data()
        print(f"Book '{title}' added successfully.")

    def add_member(self, name, member_id):
        self.members.append({'name': name, 'member_id': member_id})
        self.save_data()
        print(f"Member '{name}' added successfully.")

    def list_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")

    def list_members(self):
        if not self.members:
            print("No members available.")
            return
        for member in self.members:
            print(f"Name: {member['name']}, Member ID: {member['member_id']}")

    def find_book(self, isbn):
        for book in self.books:
            if book['isbn'] == isbn:
                print(f"Book found: Title: {book['title']}, Author: {book['author']}")
                return
        print("Book not found.")

    def find_member(self, member_id):
        for member in self.members:
            if member['member_id'] == member_id:
                print(f"Member found: Name: {member['name']}, Member ID: {member['member_id']}")
                return
        print("Member not found.")

    def run(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. Add Member")
            print("3. List Books")
            print("4. List Members")
            print("5. Find Book")
            print("6. Find Member")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                self.add_book(title, author, isbn)
            elif choice == '2':
                name = input("Enter member name: ")
                member_id = input("Enter member ID: ")
                self.add_member(name, member_id)
            elif choice == '3':
                self.list_books()
            elif choice == '4':
                self.list_members()
            elif choice == '5':
                isbn = input("Enter book ISBN: ")
                self.find_book(isbn)
            elif choice == '6':
                member_id = input("Enter member ID: ")
                self.find_member(member_id)
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.run()
