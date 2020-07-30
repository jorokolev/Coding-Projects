TICKET_PRICE = 10

tickets_remaining = 100


#Run this code until there are tickets left.
while tickets_remaining >= 1:

	#Output how many tickets are remaining using the tickets_remaining variable

	print("There are " + str(tickets_remaining) + " tickets remaining.")
	#or:
	#print("There are {} tickets remaining.".format(tickets_remaining))

	#Gather the users name and assign in to a new variable

	user_name = input("What is your name?  ")

	#Promt the user by name and ask how many tickets they would like
	#Calculate the price (numbber of tickets multiplied by the price) and assign it to a variable
	#Output the price to the screen

	number_of_tickets = input("How many tickets would you like?  ")
	try:
		number_of_tickets = int(number_of_tickets)
		if number_of_tickets > tickets_remaining:
			raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
	except ValueError as err:
		print("We ran into a little issue. Please try again.")
	else:
		amount_due = number_of_tickets * TICKET_PRICE
#or
#		def calculate_price(number__of_tickets):
#			return number_of_tickets * TICKET_PRICE



		print("The total due is " + str(amount_due) + " pounds")
	#or:
	#print("The total due is £{}".format(amount_due))

	#Prompt user if they want to proceed. Y/N?
	#If Y then print SOLD on screen to confirm purchase and decrement tickets purchased and thank them by name.

		should_proceed = input("Do you want to proceed? Y/N  ")
		if should_proceed.lower() == "y":
			print("SOLD")
			tickets_remaining -= number_of_tickets
		else:
			print("Thank you anyways, {}!".format(user_name))
		
#Notify the user when the tickets are all sold out.
print("Sorry all tickets are sold out! :(")
	