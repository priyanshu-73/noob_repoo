num1=int(input("enter number 1\n"))
num2=int(input("enter number 2\n"))
num3=int(input("enter numer 3\n"))
if (num1<num2):
    if(num1<num3):
        print("num1 is the smallest")
    else:
        print("num3 is the smallest")
elif (num2<num3):
    print("num2 is the smallest")
else:
    print("num3 is the smallest")