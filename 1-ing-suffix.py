def mine():
    name = input("Enter a string")
    pp = "ing"
    cc = "ly"
    if (len(name)> 3 and name[-3:]!=pp):
        new_name=name+pp
        print (new_name)
    elif (name[-3:]==pp):
        new_name=name+cc
        print(new_name)
    elif(len(name)<=3):
        print(name)

mine()