#name = {
   # 'first_name':'Austin',
   # 'last_name':'Okafor',
   # 'Age':23,
   # 'city':'Bradford'    
   # }
#print(name)

favorite_number = { 
'John':7,
'Mathew': 10,
'Tonia':8,
'Murdryk':11,
'Palmer':20,
}

for name, number in favorite_number.items(): #to print key&value 
    #method .get can get key&values in a large dictionary
    print(f"{name}'s favorite number is {number}.")
    #print(f"{name} {number}.")
 