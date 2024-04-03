def replace_last(numbers):
    try:
        numbers.insert(0, numbers[-1])
        numbers.pop(-1)
        return numbers
    except IndexError:
        return numbers
number = [2,5,3,6,7,8,9,10,11,12]
print(replace_last(number))

