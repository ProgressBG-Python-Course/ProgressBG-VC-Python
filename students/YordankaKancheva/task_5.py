#task 5
#Enter a name, please: Stoyan

#The names you've entered are:

tries = 0
list1 = []
# iep: discuss
while tries < 3:
    y=str(input("Enter a name, please:\n"))
    list1.append(y)
    tries +=1
    if tries == 3:
        print("The names you've entered are:\n", list1)
