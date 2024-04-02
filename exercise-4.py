def chunking_by(numbers, chunck):
    list = []
    temp = []
    for i in numbers:
        temp.append(i)
        if len(temp) == chunck:
            list.append(temp)
            temp = []
    if len(temp) > 0:
        list.append(temp)
    return list
number = [2,5,3,6,7,8,9,10,11,12]
print(chunking_by(number, 3))
