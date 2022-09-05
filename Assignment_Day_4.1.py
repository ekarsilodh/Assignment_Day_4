def addition(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

addition(3,5)
addition(4,5,6,7)
addition(1,2,3,5,6)
