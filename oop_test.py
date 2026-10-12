class Book():
    book_type = 'horror'
    def __init__(self, page):
        self.pages = page
    def open(self):
        print(f'opened the book on last page ({self.pages})')    
b1 = Book(340)
print(b1.book_type)


class Circle():
    pi = 3.1415926
    def __init__(self, r):
        self.r = r
    def masahat(self):
        m = self.r * self.r * Circle.pi
        return m
c1 = Circle(10)
print(c1.masahat())