
tickets_remaining = 100 
#run this code continuously until we run out of tickets
while tickets_remaining >= 1:
  #output how many tickets are remaining using the tickets_remaining variable
  print("There are {} tickets remaining.".format(tickets_remaining))
  
  #Gather the user's name and assign it to a new variable
  user_name = input("What is your name? ")
  #prompt the user by name and ask how many tickets they would like
  ticket_num = input("How many tickets would u like, {}?".format(user_name))
  ticket_num = int(ticket_num)
  #calculate the price of the ticket
  price = ticket_num * TICKET_PRICE
  print("The total due is ${}".format(price))
  #prompt user if they want to proceed.  Y/N?
  should_proceed = input("Do you want to proceed? Y/N ")
  #if they want to proceed
  if should_proceed.upper() == "Y":
      #print out to the screen "SOLD!" to confirm purchase
      #Todo: gather credit card information and process it.
      print("SOLD!")  
      #and then decrement the tickets remaining by the number of tickets purchased
      tickets_remaining -=ticket_num
  #otherwise...
  else:
       print("Thank you anyways, {}!".format(user_name))
# notify the user that the tickets are sold out
print("sorry the tickets are all sold out!!!:(")