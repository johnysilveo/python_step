# Simple arithmetic example
print(2 + 4.5)  # 6.5

# ----------- Film Class -----------
class Film:
    def __init__(self, title, genre):
        # Constructor with title and genre
        self.title = title
        self.genre = genre

    def show_info(self):
        # Display film info
        print(f"Title {self.title}\nGenre {self.genre}")

# ----------- Book Class -----------
class Book:
    def __init__(self, title, genre, pages):
        # Constructor with title, genre, number of pages
        self.title = title
        self.genre = genre
        self.pages = pages
        self.feedbacks = []  # List to store feedback strings

    def show_info(self):
        # Display book info
        print(f"Title {self.title}\nGenre {self.genre}")

    def __str__(self):
        # Custom string representation when using print()
        return f"Title {self.title}\nGenre {self.genre}\nPages {self.pages}"

    def __eq__(self, other_obj):
        # Equality based on title and pages
        return self.title == other_obj.title and self.pages == other_obj.pages

    def __gt__(self, other_obj):
        # Greater than comparison based on number of pages
        return self.pages > other_obj.pages

    def __getitem__(self, ind):
        # Allows indexing into feedbacks like book[0]
        try:
            return self.feedbacks[ind]
        except IndexError:
            return "Invalid index"

# ----------- Book and Film Instances -----------
film1 = Film("Godzila One", "Horror")
book1 = Book("Python", "Education", 100)
book2 = Book("Python2", "Edu", 100)

book1.feedbacks = ["Great book", "Easy to understand"]

# Polymorphic behavior – both classes have show_info()
for item in (film1, book1):
    item.show_info()

# Print custom __str__ from Book
print(book1)

# Compare books (eq and gt)
print(book1 == book2)  # False
print(book1 > book2)   # False

# Access feedback via index
print(book1[1])        # "Easy to understand"

# ----------- Point Class with Overloaded Operators -----------
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        # Return coordinates
        return f"{self.x} : {self.y}"

    def __mul__(self, other):
        # Multiply either by int or another Point
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        elif isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)

    def __iadd__(self, other):
        # In-place addition (+=)
        if isinstance(other, int):
            self.x += other
            self.y += other
            return self
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise TypeError(f"can not add a Point with {type(other)}")

    def __float__(self):
        # Convert coordinates to float
        return Point(float(self.x), float(self.y))

# Create and add Points
p1 = Point(1, 1)
p2 = Point(2, 2)
p1 += p2  # Now p1 = (3, 3)

print(p1 * p2)  # Output: (3*2, 3*2) = (6, 6)

# ----------- Libra Class with __slots__ -----------
class Libra:
    __slots__ = ('name', 'address', 'book_num', 'num')  # Memory optimization (predefined attributes)

    def __init__(self, name, address, book_num):
        self.name = name
        self.address = address
        self.book_num = book_num

    def __str__(self):
        # Return formatted library info
        return f"Library {self.name} located at {self.address} has {self.book_num} books"

    # def __add__(self, other):
    #     if isinstance(other, int):
    #         return Libra(self.name,self.address,self.book_num + other)
    #     return NotImplemented
    #
    # def __sub__(self, other):
    #     if isinstance(other, int):
    #         return Libra(self.name,self.address,self.book_num - other)
    #
    # def __iadd__(self, other):
    #     if isinstance(other, int):
    #         self.book_num += other
    #         return  self
    #     else:
    #         return NotImplemented
    #
    # def __isub__(self, other):
    #     if isinstance(other, int):
    #         self.book_num -= other
    #         return  self
    #     else:
    #         return NotImplemented
    #
    # def __lt__(self, other):  # <
    #     if isinstance(other, Libra):
    #         return self.book_num < other.book_num
    #     return NotImplemented
    #
    # def __le__(self, other):  # <=
    #     if isinstance(other, Libra):
    #         return self.book_num <= other.book_num
    #     return NotImplemented
    #
    # def __gt__(self, other):  # >
    #     if isinstance(other, Libra):
    #         return self.book_num > other.book_num
    #     return NotImplemented
    #
    # def __ge__(self, other):  # >=
    #     if isinstance(other, Libra):
    #         return self.book_num >= other.book_num
    #     return NotImplemented
    #
    # def __eq__(self, other):  # ==
    #     if isinstance(other, Libra):
    #         return self.book_num == other.book_num
    #     return NotImplemented
    #
    # def __ne__(self, other):  # !=
    #     if isinstance(other, Libra):
    #         return self.book_num != other.book_num
    #     return NotImplemented

lib = Libra('Central', '4175 Executive Dr. La Jolla, San Diego', 3000)


print(lib.name,lib.address,lib.book_num)


