numbers = input("Enter numbers separated by comma: ").split(',')
# This code takes a list of numbers as input from the user, splits them by comma, and converts them to integers.

def find_biggest_number(numbers):
    numbers = [int(num) for num in numbers]
    biggest_number = numbers[0]
    for number in numbers:
        if number > biggest_number:
            biggest_number = number
    return biggest_number

biggest_number = find_biggest_number(numbers)
print("The biggest number is:", biggest_number)
# This code takes a list of numbers as input from the user, splits them by comma, converts them to integers, and finds the biggest number in the list.