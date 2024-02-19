# Ibrahim PAMUK || ibrahimpamuk@outlook.com
import os
class Library():

    def __init__(self, filename):
        self.filename = filename

        self.file = open(self.filename, 'a+')
        print(f"File {self.filename} opened successfully!")
    
    def __del__(self):
        if hasattr(self, 'file') and self.file is not None:
            self.file.close()
            print(f"File {self.filename} closed.")

     
    def read_books_info(self):
        books = []

        for line in self.file:
            book_info = line.strip().split(',')
            if len(book_info) == 4:
                book_name, author, release_date, total_page = book_info
                books.append({
                    'book_name': book_name,
                    'author': author,
                    'release_date': release_date,
                    'total_page': int(total_page)
                })
        return books
    
lib = Library('books.txt')

def print_interface():
    print("*** MENU ***")
    print("1) List Books\n2) Add Books\n3) Remove Book\n4) Quit")

def extract_book_and_author(line):
    parts = line.strip().split(',')
    return parts[0].strip(), parts[1].strip()
    
    
def list_books():
    temp_file = open(lib.filename, 'r', encoding="utf-8")
    if(os.path.getsize(lib.filename) == 0):
        print('Book list is empty!')
    else:
        for line in temp_file:
            book_name, author_name = extract_book_and_author(line)
            print(f"Book: {book_name}, Author: {author_name}")    

def add_books():
    temp_file = open(lib.filename, '+a', encoding="utf-8")
    if(os.path.getsize(lib.filename) == 0):
        book_title = input('Enter the book title: ')
        author = input('Enter the author: ')
        release_date = input('Enther the release date: ')
        total_page = input('Enter the number of pages: ')
        temp_file.write(f"{book_title}, {author}, {release_date}, {total_page}")
        print(f"Book informations are written into the {lib.filename} file")
    else:
        book_title = input('Enter the book title: ')
        author = input('Enter the author: ')
        release_date = input('Enther the release date: ')
        total_page = input('Enter the number of pages: ')
        temp_file.write(f"\n{book_title}, {author}, {release_date}, {total_page}")
        print(f"Book informations are written into the {lib.filename} file")    
            
def remove_book():
    lines_to_keep = []
    unwanted_book_name = input("Enter the book name that you wanted to delete: ")
    with open(lib.filename, 'r', encoding="utf-8") as file:
        for line in file:
            if unwanted_book_name.lower() not in line.lower():
                lines_to_keep.append(line)

    with open(lib.filename, 'w', encoding="utf-8") as file:
        file.writelines(lines_to_keep)    

#print_interface()
counter = 0
while True:
    if(counter==3):
        print("3 invalid selections were made. Exiting the app...")
        break
    print_interface()
    choice = input('Select between (1-4): ')
    match choice:

        case '1':
            print('Option 1 is selected!')
            list_books()
            
            
        
        case '2':
            print('Option 2 is selected!')
            add_books()
             
            
        
        case '3':
            print('Option 3 is selected!')
            remove_book()
            
            
        
        case '4':
            print('Exting the app...')
            break
        
        case _:
            if not(choice.isdigit()):
                print('ONLY ENTER NUMBERS BETWEEN 1-4 DO NOT USE LETTERS OR SYMBOLS')
                counter += 1
                print('Please make a valid choice. After 3 invalid selections, you will be logged out of the program!')
                print("Choice remaning: {} ".format(3-counter))
            else:
                print('Invalid selection has been made!')
                counter += 1
                print('Please make a valid choice between 1-4. After 3 invalid selections, you will be logged out of the program!')
                print("Choice remaning: {} ".format(3-counter))