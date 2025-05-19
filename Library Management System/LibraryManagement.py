import json
import os

class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"{self.title} by {self.author} ({self.year})")


class Book(LibraryItem):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def display_info(self):
        print(f"[Book] {self.title} by {self.author}, Genre: {self.genre}")


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year)
        self.issue = issue

    def display_info(self):
        print(f"[Magazine] {self.title} (Issue: {self.issue})")


class Journal(LibraryItem):
    def __init__(self, title, author, year, field):
        super().__init__(title, author, year)
        self.field = field

    def display_info(self):
        print(f"[Journal] {self.title}, Field: {self.field}")


class Library:
    def __init__(self, filename=None):
        if filename is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(base_dir, "library_data.json")
        self.items = []
        self.filename = filename
        self.load_items()

    def add_item(self, item):
        self.items.append(item)
        self.save_item_to_file(item)
        print(f"Item '{item.title}' added successfully!")

    def show_all_items(self):
        self.load_items()
        if not self.items:
            print("Library is empty.")
        else:
            for item in self.items:
                item.display_info()  # Polymorphism in action!

    def load_items(self):
        self.items.clear()
        for entry in self.load_all_from_file():
            item_type = entry["type"]
            title = entry["title"]
            author = entry["author"]
            year = entry["year"]
            extra = entry["extra"]

            if item_type == "Book":
                self.items.append(Book(title, author, year, extra))
            elif item_type == "Magazine":
                self.items.append(Magazine(title, author, year, extra))
            elif item_type == "Journal":
                self.items.append(Journal(title, author, year, extra))

    def load_all_from_file(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    
    def save_item_to_file(self, item):
        item_data = {
            "type": type(item).__name__,
            "title": item.title,
            "author": item.author,
            "year": item.year
        }

        # Add the extra field
        if isinstance(item, Book):
            item_data["extra"] = item.genre
        elif isinstance(item, Magazine):
            item_data["extra"] = item.issue
        elif isinstance(item, Journal):
            item_data["extra"] = item.field

        # Append to file
        all_data = self.load_all_from_file()
        all_data.append(item_data)
        with open(self.filename, "w") as f:
            json.dump(all_data, f, indent=4)


lib = Library()

print("---------------------------------")
print("Welcome to the Library Management")
print("---------------------------------")

while True:
    print("\n1. Show the items in Library")
    print("2. Add item in Library")
    print("3. Exit")

    try:
        inputValue = int(input("\nPlease input your choice: "))
    except ValueError:
        print("Invalid Input. Please enter the correct option.")
        continue

    if inputValue == 1:
        lib.show_all_items()

    elif inputValue == 2:
        print("\nWhat do you want to add into the library?")
        print("1. Book")
        print("2. Magazine")
        print("3. Journal")

        item_types = {
            1: ("Book", Book, "genre"),
            2: ("Magazine", Magazine, "issue"),
            3: ("Journal", Journal, "field")
        }

        try:
            item_choice = int(input("Please input your choice: "))
            if item_choice not in item_types:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid option (1-3).")
            continue

        # Common input fields
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = input("Enter the year: ")

        extra_label = item_types[item_choice][2]
        extra_value = input(f"Enter the {extra_label} of the {item_types[item_choice][0].lower()}: ")

        # Create object dynamically
        item_class = item_types[item_choice][1]
        item = item_class(title, author, year, extra_value)
        lib.add_item(item)

    elif inputValue == 3:
        print("Exiting the library management system.")
        break

    else:
        print("Invalid option. Please select 1, 2, or 3.")
