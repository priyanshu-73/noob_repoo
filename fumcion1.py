def calculate_total_ticket_cost(no_of_adults,no_of_children):
    price = 37550.0
    price_of_adults = no_of_adults*price
    price_of_children = no_of_children*((1/3)*price)
    total = price_of_adults + price_of_children
    tax = (7/100)*total
    total_a = total + tax
    dis = (10/100)*total_a
    final_price = total_a - dis
    return final_price

d = calculate_total_ticket_cost(5,2)
print(d)

e = calculate_total_ticket_cost(3,3)
print(e)

f = calculate_total_ticket_cost(3,0)
print(f)