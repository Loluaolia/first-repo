class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"


class BookManager:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        print("\nწიგნი წარმატებით დაემატა!")
    
    def list_books(self):
        if not self.books:
            print("\nსია ცარიელია!")
            return
        print("\nწიგნების სია:")
        for book in self.books:
            print(book)
    
    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("\nნაპოვნი წიგნები:")
            for book in found_books:
                print(book)
        else:
            print("\nწიგნი ვერ მოიძებნა!")


def main():
    manager = BookManager()
    while True:
        print("\n1. ახალი წიგნის დამატება")
        print("2. ყველა წიგნის ჩვენება")
        print("3. წიგნის ძებნა")
        print("4. გასვლა")
        
        choice = input("აირჩიეთ მოქმედება: ")
        
        if choice == "1":
            title = input("შეიყვანეთ წიგნის სათაური: ")
            author = input("შეიყვანეთ ავტორი: ")
            year = input("შეიყვანეთ გამოცემის წელი: ")
            if year.isdigit():
                manager.add_book(title, author, int(year))
            else:
                print("\nგთხოვთ, შეიყვანოთ სწორი წელი!")
        elif choice == "2":
            manager.show_books()
        elif choice == "3":
            search_title = input("შეიყვანეთ საძიებო სათაური: ")
            manager.search_book(search_title)
        elif choice == "4":
            print("\nპროგრამის დასრულება...")
            break
        else:
            print("\nარასწორი არჩევანი! სცადეთ თავიდან.")


if __name__ == "__main__":
    main()
