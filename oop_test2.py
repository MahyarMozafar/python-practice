class Book():
    book_type = 'horror'
    def __init__(self, name, page):
        self.pages = page
        self.name = name
    def open(self):
        print(f'opened the {self.name} which has {self.pages} pages')

b1 = Book("C Programming", 234)

class Darsi(Book): 
    def __init__(self, reshte, paye, name, pages):
        Book.__init__(self, name, pages)
        print('a new darsi book')
        self.reshte = reshte
        self.paye = paye
    def open(self):
        print(f'opened {self.name} of {self.reshte} paye {self.paye}')

d = Darsi('tajrobi', 3, '300 nokte', 120)
d.open()
class runner():
    def __init__(self, name):
        self.name = name 
    def action(self):
        print(f'{self.name} is running')

leila = runner('leila')


class cyclist():
    def __init__(self, name):
        self.name = name 
    def action(self):
        print(f'{self.name} is biking')

babak = cyclist('babak')
for person in [babak, leila]:
    person.action()

class Human():
    def __init__(self, name):
        pass
    def jump(self):
        raise NotImplementedError("implement the jump")
class Programmer(Human):
    pass
    def jump(self):
        print('I jumped')
kian = Programmer('kian')
kian.jump()