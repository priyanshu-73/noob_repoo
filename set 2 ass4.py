
def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if (distance_in_kms<=0):
        bill_amount = -1
    elif quantity_ordered < 1:
        bill_amount = -1
    else:
        if (food_type== "V"):
            price = 120
            if(quantity_ordered>1):
                price = price*quantity_ordered
        elif (food_type=="N"):
            price = 150
            if (quantity_ordered > 1):
                price = price * quantity_ordered
        else :
            return -1

        if(distance_in_kms<=3):
            d_charge = 0
        elif(distance_in_kms<=6):
            d_charge = (distance_in_kms - 3)*3
        elif(distance_in_kms>=7):
            d_charge = ((distance_in_kms-6)*6)+9
        bill_amount = price + d_charge
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("V",2,7)
print(bill_amount)