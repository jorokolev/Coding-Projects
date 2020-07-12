#To keep track of the kinds of pizzas you sell, create a list called toppings
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

#To keep track of how much each kind of pizza slice costs, create a list called prices
prices = [2, 6, 1, 3, 2, 7, 2]

#Find the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas = len(toppings)

#Print the string "We sell X different kinds of pizza!", with num_pizzas where the X is.
print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

#Use zip to combine the two lists into a list called pizzas
pizzas = list(zip(prices, toppings))
pizzas.sort()

#Print pizzas
print(pizzas)

#SStore the first element of pizzas in a variable called cheapest_pizza.
cheapest_pizza = pizzas[1]

#Get the last item of the pizzas list and store it in a variable called priciest_pizza.
priciest__pizza = pizzas[-1]

#Slice the pizzas list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizzas[:3]

#Print the three_cheapest list.
print(three_cheapest)

#Count the number of occurrences of 2 in the prices list, and store the result in a variable called
num_two_dollar_slices = prices.count(2)

#Print it out
print(num_two_dollar_slices)