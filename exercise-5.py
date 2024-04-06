def reverse_ascending(numbers):
    for i in numbers:
        for i in range(len(numbers) - 1):       
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers

number = [2,5,3,6,7,8,9,10,11,12]
print(reverse_ascending(number))