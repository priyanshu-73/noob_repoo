def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    if(num1>=num2+num3):
        print(failure)
        return failure
    elif(num2>=num1+num3):
        print(failure)
        return failure
    elif(num3>=num1+num2):
        print(failure)
        return failure
    else:
        print(success)
        return success


form_triangle(5,3,3)