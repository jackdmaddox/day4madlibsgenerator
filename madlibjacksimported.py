import madlibsfunctions
want_to_write_madlib = "yes"

while want_to_write_madlib == "yes":
    celeb_action = input('Enter a verb...')
    celebrity = input('Please enter the name of a celebrity...')
    gender = input('is that a he, she or they?')
    animal = input('Please enter a type of animal...')
    animal_verb = input('What is the animal doing...')
    number_of_animals = int(input('How many of them are there?'))
    print(madlibsfunctions.madlibsfunction(celeb_action, celebrity, gender, animal, animal_verb, number_of_animals))
    want_to_write_madlib = input("Would you like to play again?")