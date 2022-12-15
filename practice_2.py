tickets = []
def generate_ticket(airline,source,destination,no_of_passengers):
   for ticket_number in range(101,101+no_of_passengers):

      tickets.append('%s:%s:%s:%d'%(airline,source[0:3],destination[0:3],ticket_number))

   if no_of_passengers > 5:

      print(tickets[-5:])

   else:

      print(tickets)

generate_ticket("AI","Banglore","London",7)