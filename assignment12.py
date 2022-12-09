for i in range (1,501):
    name = input("enter your name\n")
    branch = input("enter branch\n")
    score = int(input("enter your score\n"))
    fee = float(input("enter your course fee\n"))
    if (branch=='arts'):
        if(score>=90):
            scholarship = 50.0
        elif(score%2!=0):
            scholarship = 5.0
        else:
            scholarship = 0.0
    elif(branch=='engineering'):
        if(score>85):
            scholarship = 60.0
        elif(score%7==0):
            scholarship = 5.0
        else:
            scholarship = 0.0
    else:
        print("we don't have this  branch\n")


    scholarship_amt = fee*(scholarship/100)
    final_fee = fee-scholarship_amt
    print("the final fee of",name,"is :",final_fee)

