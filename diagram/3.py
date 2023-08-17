def find_large(numbers):
    if not numbers:
        return None
    #largest = None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]
largest_number  = find_large(numbers)
print(largest_number)
