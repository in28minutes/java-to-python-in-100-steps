def print_squares_of_numbers_upto(n):
    for i in range(1,n+1):
        print(i*i)


def print_squares_of_even_numbers_upto(n):
    for i in range(2,n+1,2):
        print(i*i)


def sum_of_two_numbers(number1,number2):
    sum = number1 + number2
    return sum


def print_numbers_in_reverse(n):
    for i in range(n,0,-1):
        print(i)


print(sum_of_two_numbers(5,6))
# print_squares_of_even_numbers_upto(10)
# print_numbers_in_reverse(10)