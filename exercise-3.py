def remove_all_after(number, n):
    list= []
    i=0
    while i< len(number):
        list.append(number[i])
        if number[i] == n:
            break
        i+=1
    return list
number = [2,5,3,6,7,8,9,10,11,12]
print(remove_all_after(number, 9))