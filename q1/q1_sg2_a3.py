import time
birthyear = int(input("Input your birth year to know your zodiac sign. (It cannot be before 1900): ")) #Birthyear input
signs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"] #List to be used later

if birthyear < 1900: #Statement to filter years before 1900
  print("That year is not supported (Before 1900)")
else: #Valid statement function
  number = (birthyear - 1900) % 12 #Uses modulo to loop
  print(f"Your zodiac sign is {signs[number]}!") #Output
time.sleep(2) #So the user can see their sign before program terminates
