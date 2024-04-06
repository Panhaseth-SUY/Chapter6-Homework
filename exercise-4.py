def chunking_by(number, chunck):
    list = []
    temp = []
    i=0
    while i < len(number):
        print(number[i])
        temp.append(number[i])
        if len(temp)==chunck:
            list.append(temp)
            temp =[]
        i+=1
    if len(temp) > 0:
        list.append(temp)
    return list
number = [2,5,3,6,7,8,9,10,11,12]
print(chunking_by(number, 3))
