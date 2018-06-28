from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __repr__(self):
        return repr((self.currency, self.amount))

    def __eq__(self, other):
        return (self.currency, self.amount) == (other.currency,other.amount)

    def __le__(self, other):
        return (self.amount) <= (other.amount)

amount1 = Money('EUR', 10)
amount2 = Money('EUR', 20)
amount3 = Money('EUR', 10)

print(amount1 < amount2)
print(amount2 < amount3)
print(amount3 < amount1)

print(amount3 <= amount1)
print(amount3 >= amount1)

# print(amount1 == amount2)
# print(amount1 != amount2)
# print(amount1 == amount3)
# print(amount1 != amount3)

# print(amount1 + amount2)
# print(amount2 - amount1)



# object.__add__(self, other)
# object.__sub__(self, other)
# object.__mul__(self, other) *
# object.__matmul__(self, other)
# object.__truediv__(self, other) \
# object.__floordiv__(self, other) \\
# object.__mod__(self, other) %
# object.__pow__(self, other[, modulo]) **
# object.__and__(self, other) and
# object.__xor__(self, other) ^
# object.__or__(self, other) or
#
# i methods
