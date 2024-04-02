def index_power(numnbers, n):
    try:
        return numnbers[n] ** n
    except IndexError:
        return -1
number = [2,5,3,6,7,8,9,10,11,12]
print(index_power(number, 3))