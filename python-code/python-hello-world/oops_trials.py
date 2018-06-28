class Book:

    count = 0

    def __init__(self, name):
        self._name = name
        Book.count = Book.count + 1

    @property
    def name(self):
        print("Getter For Name Called")
        return self._name

    @name.setter
    def name(self, name):
        print("Setter For Name Called")
        self._name = name

    @staticmethod
    def static_method():
        print("I'm static")

    def __setattr__(self, key, value):
        print(f'{key} - {value}')
        self.__dict__[key] = value


# book1 = Book('Microservices')
# print(book1.name)
# book1.name = 'ABC'
# print(book1.name)
# book2 = Book('Web Services')

# print(Book.count)
# print(book1.count)
# print(book2.count)
# Book.static_method()
# book1.static_method()

# print(book1.name)

def do_this_and_print(func,data):
    print(func(data))


def double(data):
    return data * 2

def triple(data):
    return data * 3


do_this_and_print(double,5)

do_this_and_print(triple,5)

do_this_and_print(lambda x : x*2, 5)

do_this_and_print(lambda x : x*5, 5)