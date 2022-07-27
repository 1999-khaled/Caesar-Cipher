val = input("press 1 for encryption and 2 for decryption ")
if val == "1":
    print("you have chosen encryption...")
    lst = []
    x = int(input("please enter your encryption key"))
    y = input("please enter the plain text:")
    for i, v in enumerate(y):
        c = chr(ord(v) + x)
        lst.append(c)

    listToStr = ' '.join([str(elem) for elem in lst])
    print("cipher text:" + listToStr)

elif val == "2":
    print("you  have chosen decryption...")
    lst2 = []
    z = input("please enter the cipher text:")
    n=0
    while n<94:
       for i, v in enumerate(z):
            c = chr(ord(v)-n)
            lst2.append(c)
       listToStr = ' '.join([str(elem) for elem in lst2])
       print("plain text:" + listToStr)
       print("key=",n)
       lst2.clear()
       check=input("is this the right plain text?(y/n)")
       if check == "y":
           print("thank you for your time :)")
           exit()
       elif check == "n":
           print("oops..let's try again")
           n=n+1
       else:
           print("please enter either 'y' or 'n")
    print("out of keys..please check again from the previous results")

else:
    print("please choose the number correctly")
