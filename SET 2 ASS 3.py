def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    # Start writing your code here
    # Populate the variables: five_needed and one_needed
    a = rupees_to_make // 5
    b = rupees_to_make % 5
    if (a < no_of_five):
        five_needed = a
        if (b > no_of_one):
            print(-1)
        else:
            one_needed = b
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
    else:
        five_needed = no_of_five
        if (no_of_one >= (a - no_of_five) * 5 + b):
            one_needed = (a - no_of_five) * 5 + b
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    # print(-1)


# Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(100, 19, 8)