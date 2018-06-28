i = 0

while i<11:
    print(i)
    i += 1


# print all the squares of numbers < 100
# 1 4 9 .. 81
def print_squares_of_numbers_below(limit):
    i = 1
    while i*i < limit :
        print(i*i, end=' ')
        i += 1
    print()

print_squares_of_numbers_below(100)