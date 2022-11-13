class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"The author is {self.author} and the page count is {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"The chief editor is {self.chief_editor}")


m = Magazine("Donald Duck", "Aki Hyyppä")
m.print_information()

b = Book("Compartment No. 6", "Rosa Liksom", 192)
b.print_information()

# you can also make a list and use a for loop for printing the info
# list is easier to follow

# example:
# publication = []
# publication.append(Magazine("Donald Duck", "Aki Hyyppä")
# for p in publication:
#   publication.print.information






