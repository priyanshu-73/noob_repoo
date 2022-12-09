sum = 0
choice='yes'

while(choice =='yes'):

    choice = input("enter choice yes or no :\n")

    if(choice=='yes'):
        a = int(input("enter number : "))
        if(a%4==0):
            sum=sum+a
            print("the sum is : ",sum)
        else:
            print("give another number which is divisible by 4\n")
    else:
        print("the code is over\n")