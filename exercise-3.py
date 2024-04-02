def remove_all_after(numbers, n):
    list= []
    for i in numbers:
        list.append(i)
        if i == n:
            break
    return list
number = [2,5,3,6,7,8,9,10,11,12]
print(remove_all_after(number, 9))