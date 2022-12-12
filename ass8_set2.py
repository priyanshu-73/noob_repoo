#lex_auth_012693810762121216155

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0


    if(heads%2!=0 and heads>legs):
        print("no solution")
    else:
        rabbit_count = int((legs + (-2 * heads)) / 2)
        chicken_count = int(heads - rabbit_count)

        print(chicken_count,rabbit_count)
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(23,67)