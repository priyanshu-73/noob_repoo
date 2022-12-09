sum = 0
a = int(input("enter number :\n"))
b=a
while(a>0):
    remainder = a%10
    sum=sum+remainder*remainder*remainder
    a = a//10
if(b==sum):
    print("armstrong\n")
else:
    print("booohhhhhh\n")
