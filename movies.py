while True:
    Age = input("\n Please enter your age (or 'q' quit):")
    
    if Age.lower() == 'q':
        break
    Age = int(Age)
    
    if Age < 3:
        ticket_price = 0 #Ticket is free
        #print(f"Your have a free movie ticket \n")
    elif Age >= 3 and Age <=12:
        ticket_price = 10 #Ticket price for age 3 to 12
    else:
        ticket_price = 15 # ticket price for ages 15
   
    
    #Display ticket
    if Age < 3:
         print(f"Your have a free movie ticket \n")
    else:
        print(f"Your movie ticket cost ${ticket_price}\n")
    
#the End
print('Thank you for using this service. Enjoy your movie ')