class BookEnhanced:
    def __init__(self, name, copies):
        self.name = name
        self._copies = copies

    @property
    def copies(self):
        print('getter called')
        return self._copies

    @copies.setter
    def copies(self, copies):
        print('setter called')
        if(copies>=0):
            self._copies = copies

microservices = BookEnhanced('Microservices',5)

print(microservices.copies)

microservices.copies = 10

print(microservices.copies)