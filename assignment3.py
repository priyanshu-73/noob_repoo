a = int(input("enter number : \n"))
reverse = 0
temp = a
while(a>0):
    remainder = a%10
    reverse = reverse*10+remainder
    a=a//10
if (reverse==temp):
    print("palindrome")
else:
    print("not")
