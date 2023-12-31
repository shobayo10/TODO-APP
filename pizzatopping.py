pizza_toppings = "\nPlease enter your pizza topings:"
pizza_toppings += "\n(Enter 'quit' to finish order.)"


while True:
    pizza_toppings = input(pizza_toppings)
    
    #print(f"\n I will be adding {pizza_toppings} to your pizza")
    
    if pizza_toppings == 'quit':
        break
    
    else:
        print(f"\n I will be adding {pizza_toppings} to your pizza")
   

    