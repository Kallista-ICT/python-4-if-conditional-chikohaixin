user_input = int(input("please enter your birth year(e.g., 1990): "))
#determine category/level based on user input
if birth_year < 1946: 
    generation = "Silent Generation"
elif birth_year < 1965:
    generation = "Baby Boomer"
elif birth_year < 1981:
    generation = "Generation X"
elif birth_year < 1997: 
    generation = "Millenial"
elif birth_year < 2013 
    generation = "Generation Z"
else: 
    generation = "Generation Alpha"
    print(f"you belong to: {generation}")