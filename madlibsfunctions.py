""""
celebAction = input('Enter a verb...')
celebrity = input('Please enter the name of a celebrity...')
gender = input('is that a he, she or they?')
animal = input('Please enter a type of animal...')
animalVerb = input('What is the animal doing...')
numberOfAnimals = int(input('How many of them are there?'))

def fixCelebAction(celebAction):
    celebAction = celebAction.lower()
    return celebAction

def fixCelebrity(celebrity):
    celebrity = celebrity.title()
    return celebrity

def fixGender(gender):
    gender = gender.lower()
    return gender

def fixAnimal(animal):
    animal = animal.lower()
    return animal

def fixAnimalVerb(animalVerb):
    animalVerb = animalVerb.lower()
    return animalVerb
"""    

def madlibsfunction(celeb_action, celebrity, gender, animal, animal_verb, number_of_animals):
    madlib = ("%s " "%s " "are" " %s" " %s " "while %s %ss" % (number_of_animals, animal, animal_verb, celebrity, gender, celeb_action))
    return madlib
