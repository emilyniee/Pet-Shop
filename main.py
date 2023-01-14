#-----------------------------------------------------------------------------
# Name:        Data Structures Assignment (python.py)
# Purpose:     To learn and practice classes, objects, inheritance, reading/writing files and UML diagrams
#
# References:  video tutorials in class, other links listed as comments beside code
#
#
# Author:      Emily Nie
# Created:     24-Oct-2021
# Updated:     27-Oct-2021
#-----------------------------------------------------------------------------
#importing classes
from dog import Dog
from cat import Cat
from bunny import Bunny

#converts string to bool: https://stackoverflow.com/questions/715417/converting-from-a-string-to-boolean-in-python
def stringToBool(x):
  '''
    Changes String values in the txt file to Boolean values

    Parameters
    -------
    x: String
      the True or False value that is currently in String format  

    Returns
    -------
    bool
      will be true or false depending on x

    '''
  if x == "True":
    boolean = True
  else: 
    boolean = False
  return boolean

#welcome message
print ("WELCOME TO THE ANIMAL SHOP \n")

#information regarding pet dogs
print ("----Dogs----")

#opening dogs.txt and storing the information as a list called dogContent
with open('dogs.txt', 'r') as textFile:
  dogContent = textFile.readlines()

#creating an array for Dog objects
dogs = []

#for each item in the dogContent list, the list item is split up into its individual attributes
for item in dogContent:
  name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly, trainedToServe, tricks = item.split(";")

  #tranforming attributes into their correct datatype
  age = int(age)
  childFriendly = int(childFriendly)
  gender = stringToBool(gender)
  forAdoption = stringToBool(forAdoption)
  neutered = stringToBool(neutered)
  trainedToServe = stringToBool(trainedToServe)
  #https://appdividend.com/2020/09/25/how-to-convert-python-string-to-array/
  tricksArray = tricks[:-1].split(',')

  #creating an object by feeding attributes into constructor
  dogs.append(Dog(name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly, trainedToServe, tricksArray))

#printing all Dog objects and their instance variables from the dogs array
print(dogs)
print(dogs[0])

#information regarding pet cats
print ("\n----Cats----")

#opening cats.txt and storing the information as a list called catContent
with open('cats.txt', 'r') as textFile:
  catContent = textFile.readlines()

#creating an array for Cat objects
cats = []

#for each item in the catContent list, the list item is split up into its individual attributes
for item in catContent:
  name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly, scratches, favouriteToy = item.split(";")

  #tranforming attributes into their correct datatype
  age = int(age)
  childFriendly = int(childFriendly)
  gender = stringToBool(gender)
  forAdoption = stringToBool(forAdoption)
  neutered = stringToBool(neutered)
  scratches = stringToBool(scratches)

  #creating an object by feeding attributes into constructor
  cats.append(Cat(name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly, scratches, favouriteToy))

#printing all Cat objects and their instance variables  from the cats array
print(cats)

#information regarding pet bunnies
print ("\n----Bunnies----")

#opening bunnies.txt and storing the information as a list called bunnyContent
with open('bunnies.txt', 'r') as textFile:
  bunnyContent = textFile.readlines()

#creating an array for Bunny objects
bunnies = []

#for each item in the bunnyContent list, the list item is split up into its individual attributes
for item in bunnyContent:
  name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly, hopStrength, favouriteVegetable = item.split(";")

  #tranforming attributes into their correct datatype
  age = int(age)  
  childFriendly = int(childFriendly)
  hopStrength = int(hopStrength)
  gender = stringToBool(gender)
  forAdoption = stringToBool(forAdoption)
  neutered = stringToBool(neutered)

  #creating an object by feeding attributes into constructor
  bunnies.append(Bunny(name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly, hopStrength, favouriteVegetable))

#printing all Bunny objects and their instance variables  from the bunnies array
print(bunnies)

#creating list of adoptabilities through use of adoptability() method for each object
dogAdoptabilities = ""
for item in dogs:
  dogAdoptabilities += item.getName() + ": "+ str(item.adoptability()) + "\n"
catAdoptabilities = ""
for item in cats:
  catAdoptabilities += item.getName() + ": "+ str(item.adoptability()) + "\n"
bunnyAdoptabilities = ""
for item in bunnies:
  bunnyAdoptabilities += item.getName() + ": "+ str(item.adoptability()) + "\n"

#writing in the starting adoptabilities for the day
with open ('adoptabilities.txt','w') as outputFile:
  outputFile.write("start of the day: \n\n")
with open ('adoptabilities.txt','a') as outputFile:
  outputFile.write(dogAdoptabilities)
  outputFile.write(catAdoptabilities)
  outputFile.write(bunnyAdoptabilities)

#using methods of the objects (Dog, Cat, Bunny) to complete actions and change instance variables as the day progresses
print ("\n THE DAY HAS STARTED \n")
print ("  9AM: John's birthday and he got adopted")
dogs[0].birthday()
dogs[0].changeAdoptionStatus()
print("\t" + dogs[0].bark())
print ("  11AM: Assessments for cats")
cats[0].addCFPoints(3)
cats[0].changeNeuterStatus()
cats[1].changeScratches()
print("\t" + cats[0].purr())
print("\t" + cats[1].purr())
cats[2].addCFPoints(7)
print("\t" + cats[2].sleep())
print ("  1PM: Bunnies got fed celery today")
bunnies[0].changeFavouriteVegetable("celery")
bunnies[1].changeFavouriteVegetable("celery")
print("\t" + bunnies[0].eat())
print("\t" + bunnies[1].eat())
print("\t" + bunnies[2].flop())
print ("  3PM: Play time for the dogs")
dogs[0].learnTrick("strut")
dogs[1].learnTrick("give a paw")
print("\t" + dogs[0].wagTail())
print("\t" + dogs[1].wagTail())
print("\t" + dogs[2].wagTail())
print ("  5PM: Rue's birthday and she became a service dog")
dogs[1].birthday()
dogs[1].changeTrainedToServe()
print("\t" + dogs[1].bark())
print ("  7PM: Anna jumped a fence")
bunnies[1].increaseHopStrength(10)
print("\t" + bunnies[1].hop())
print ("\n THE DAY HAS ENDED \n")

#creating list of mew adoptabilities through use of adoptability() method for each object 
dogAdoptabilities = ""
for item in dogs:
  dogAdoptabilities += item.getName() + ": "+ str(item.adoptability()) + "\n"
catAdoptabilities = ""
for item in cats:
  catAdoptabilities += item.getName() + ": "+ str(item.adoptability()) + "\n"
bunnyAdoptabilities = ""
for item in bunnies:
  bunnyAdoptabilities += item.getName() + ": "+ str(item.adoptability()) + "\n"

#appending in the ending adoptabilities for the day
with open ('adoptabilities.txt','a') as outputFile:
  outputFile.write("\n\nend of the day: \n\n")
  outputFile.write(dogAdoptabilities)
  outputFile.write(catAdoptabilities)
  outputFile.write(bunnyAdoptabilities)

#writing in the attributes of the pets at the end of the day
with open ('endOfDay.txt','w') as outputFile:
  outputFile.write("DOGS" + str(dogs))
  outputFile.write("\n\nCATS" + str(cats))
  outputFile.write("\n\nBUNNIES" + str(bunnies))