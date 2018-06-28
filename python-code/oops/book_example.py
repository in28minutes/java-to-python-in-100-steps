# MotorBike
 # gear, speed

class Book:

    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    def __repr__(self):
        return repr((self.name, self.copies))

    def increase_copies(self, how_much):
        self.copies += how_much

    def decrease_copies(self, how_much):
        self.copies -= how_much

    #set
    #get

book1 = Book('Mastering Spring 5.0', 200)
book1.increase_copies(50)

book2 = Book('Mastering Python 3', 15)
book2.decrease_copies(5)

print(book1)
print(book2)
