# beginning of the method
def sum(*args):
    resultfinal = 0
#beginning of for loop
    for arg in args:
        resultfinal = resultfinal + arg

    return resultfinal
#printing the values
print(sum(10, 20))
print(sum(10, 20, 30))
print(sum(10, 20, 40))
