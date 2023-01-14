from animal import Animal

class Pet(Animal):
  '''
  This is a pet waiting to be adopted, inherits attributes and methods from the Animal parent class

  Attributes
  ----------
  name : string
      This will hold the name of the pet as a string

  breed : string
      This will hold the breed of the pet as a string
  
  forAdoption : boolean
      This will indicate if the pet is available to be adopted at the moment
  
  neutered : boolean
      This will indicate if the pet is neutered
  
  childFriendly : int
      This will indicate if the pet can be raised in a family with kids, ranked from a scale of 0-10
  
  Methods
  -------
  getName() -> String
      Returns the name of the pet
      
  changeAdoptionStatus() -> None
      Changes adoption status to the opposite of what it currrently is
  
  changeNeuterStatus() -> None
      Changes neuter status to neutered
  
  addCFPoints(CFPoints: int) -> None
      Adds an amount of points to the child friendliness score up to a max of 10 points
  
  adoptability() -> int
      Calculates how likely it is the pet will be adopted, the bigger the number the more likely it is

  '''
  
  def __init__(self, name, gender, furColor, eyeColor, age, breed, forAdoption = True, neutered = True, childFriendly = 5):
    '''
    Constructor to build a pet

    Parameters
    -------
    name : String
        the name of the pet
    
    breed : string
        the breed of the pet
    
    forAdoption : boolean
        the adoption status of the pet
        the default is the pet True, the pet is up for adoption
    
    neutered : boolean
        the neutering status of the pet
        the default is True, neutered
    
    childFriendly : int
        the scalar value of how child friendly the pet is
        the default value is neutral, 5

    Returns
    -------
    None

    '''
    super().__init__(gender, furColor, eyeColor, age)
    self.name = name
    self.breed = breed
    self.forAdoption = forAdoption
    self.neutered = neutered
    self.childFriendly = int(childFriendly)
  
  def __str__(self):
    '''
    returns the basic information about the pet (name, breed, forAdoption, neutered, childFriendly)

    Parameters
    -------
    None

    Returns
    -------
    String
      a concatenated string with all basic information
    '''
    
    #changing the boolean value of adoption and neutered to something more user friendly
    if self.forAdoption == True:
      forAdoption = "yes"
    else:
      forAdoption = "no"
    if self.neutered == True:
      neutered = "yes"
    else:
      neutered = "no"
    
    return "\n\n Name: " + self.name + "\n " + super().__str__() +  "\n Breed: " + self.breed + "\n For Adoption?: " +forAdoption + "\n Neutered?: " + neutered + "\n Child Friendliness Rating: " + str(self.childFriendly)
  
  def getName(self):
    '''
    Returns the pet's name

    Parameters
    -------
    None  

    Returns
    -------
    String
      the name of the pet

    '''
    return self.name
        
  def changeAdoptionStatus(self):
    '''
    Changes adoption status of animal from True (adoptable) to False (not adoptable) and vice versa

    Parameters
    -------
    None  

    Returns
    -------
    None

    '''
    self.forAdoption = not self.forAdoption
  
  def changeNeuterStatus(self):
    '''
    Changes neuter status of animal from False (not neutered) to True (neutered)

    Parameters
    -------
    None  

    Returns
    -------
    None

    '''
    self.neutered = True
  
  def addCFPoints(self, CFPoints):
    '''
    Adds points to the pet's child friendliness score up to a max of 10 points

    Parameters
    -------
    CFPoints : int
      the amount of added points
    
    Returns
    -------
    None

    '''
    if self.childFriendly + CFPoints <= 10:
      self.childFriendly += CFPoints
    else:
      self.childFriendly = 10
  
  def adoptability(self):
    '''
    Calculates the adoptability of the pet based on whether or not its for adoption, neutered, its age, and its child friendliness

    Parameters
    -------
    None
    
    Returns
    -------
    int
      the adoptability score of the pet
    '''
    adoptabilityPoints = 0
    if self.forAdoption == False:
      adoptabilityPoints = 0
    else:
      adoptabilityPoints = 10
      if self.neutered == True:
        adoptabilityPoints += 10
      adoptabilityPoints += int(self.childFriendly)
      adoptabilityPoints -= int(self.age)

    return adoptabilityPoints
  