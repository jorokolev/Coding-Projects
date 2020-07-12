#Let’s add in our first item, the Lovely Loveseat that is the store’s namesake and create a price for the loveseat.
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

#Let’s extend our inventory with another characteristic piece of furniture and set the price for our Stylish Settee.
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

#We just need one more item before we’re ready for business and set the price for it.
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well. 
sales_tax = .088 #That’s 8.8% tax.

#Our first customer is making their purchase! Let’s keep a running tally of their expenses.
customer_one_total = 0
customer_one_itemization = ""

#The customer has decided they are going to purchase our Lovely Loveseat.
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

#The customer has also decided to purchase the Luxurious Lamp.
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

#They’re ready to check out! Let’s begin by calculating sales tax.
customer_one_tax = customer_one_total * sales_tax
#Add the sales tax to the customer’s total cost.
customer_one_total += customer_one_tax

#Add headings and print the totals for the customer:
print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total")
print(customer_one_total)