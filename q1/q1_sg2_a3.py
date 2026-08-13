birthyear = int(input("Input your birth year to know your zodiac sign. (It cannot be before 1900): "))
signs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

if birthyear < 1900:
  print("That year is not supported (Before 1900)")
else:
  number = (birthyear - 1900) % 12
  print(f"Your zodiac sign is {signs[number]}!")
