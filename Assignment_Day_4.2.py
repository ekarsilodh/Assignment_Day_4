def introduction(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

introduction(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
introduction(Firstname="Sreejita", Lastname="Roy", Email="sroy@nomail.com", Country="India", Age=25, Phone=9876543210)
