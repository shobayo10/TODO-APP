usernames = []
user_input = input("\n" 'Who are you' + "\n")
if usernames:
    for username in usernames:
        if user_input == 'Admin':
         print('Hello Admin,' + "\n" ' would you like to see a status report')
    else:
        print('Hello' + "\n" + user_input + ' thank you for logging in again.' )
else:
    print("we need to find some users")
