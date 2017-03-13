def reverse():
    str=input("Enter a string")
    if (len(str)%4==0):
        x = ''
        i = len(str) - 1
        while i >= 0:
            x = x + str[i]
            i = i - 1
        print(x)

reverse()
