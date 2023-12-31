#car = 'BMW'
#car.lower() == 'bmw'
#print("\n Is car == 'bmw'.")
#print(car == 'BMW')

alien_color = ['green', 'yellow', 'red']

input_color = input("\n" 'Chose alien color' + "\n")
for input_color in alien_color:
    if input_color == 'yellow': #10p for yellow
        print("\n" 'You have just earn 10 points!' + "\n" 'Alien color is correct')
    
    if input_color == 'red': #20 points for red
        print("\n" 'You have 20 points' + "\n" 'color is correct')
    if input_color == 'green': #5 points for green
        print("\n" + 'You have 5 points')

    else:
        print('You lost')
print("\n game over")
