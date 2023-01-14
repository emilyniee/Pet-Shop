
from pet import Pet

class Cat(Pet):
  '''
    This is a cat that inherits attributes and methods from the Pet parent class

    Attributes
    ----------
    scratches: boolean
      holds the scratch tendancy of the cat
    
    favouriteToy: String
      holds the name of the cat's favourite toy
    
    Methods
    -------
    changeScratches() -> None
        Changes the scratches status of the cat to the opposite of what it currently is
    
    changeFavouriteToy(newFavouriteToy: String) -> None
        Changes the cat's favourite toy

    purr() -> String
        Returns the sound effect of purring
    
    sleep() -> String
        Returns a graphical representation of a cat sleeping
    '''

  def __init__(self, name, gender, furColor, eyeColor, age, breed, forAdoption = True, neutered = False, childFriendly = 5, scratches = False, favouriteToy = "yarn"):
    '''
    Constructor to build a cat

    Parameters
    -------
    scratches: boolean
      the scratch tendancy of the cat
      the default is false, does not scratch
    
    favouriteToy: String
      the name of the cat's favourite toy
      the default is "yarn"

    Returns
    -------
    None

    '''
    self.scratches = scratches
    self.favouriteToy = favouriteToy
    super().__init__(name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly)
  
  def __repr__(self):
    '''
    returns the basic information about the animal (scratches, favouriteToy)

    Parameters
    -------
    None

    Returns
    -------
    String
      a concatenated string with all basic information
    '''
    #changing the boolean value of scratches to something more user friendly
    if self.scratches == True:
      scratches = "yes"
    else:
      scratches = "no"

    return super().__str__() + "\n Scratches?: " +  str(scratches) + "\n Favourite toy: " + str(self.favouriteToy)
    
  
  def changeScratches(self):
    '''
    Changes the scratch tendancy of the cat from True (scratches) to False (does not scratch) and vice versa

    Parameters
    -------
    None
    
    Returns
    -------
    None
    '''
    self.scratches = not self.scratches
  
  def changeFavouriteToy(self, newFavouriteToy):
    '''
    Changes the favourite toy of the cat

    Parameters
    -------
    newFavouriteToy: String
      the new favourite toy of the cat
    
    Returns
    -------
    None
    '''
    self.favouriteToy = newFavouriteToy

  def purr(self):
    '''
    Mirrors the cat purring

    Parameters
    -------
    None
    
    Returns
    -------
    String
      the sound effect of purring
    '''
    return "🐈 purr"

  def sleep(self):
    '''
    Mirrors the cat sleeping

    Parameters
    -------
    None
    
    Returns
    -------
    String
      a graphical representation of a cat sleeping
    '''
    return "( ≚ᄌ≚)ƶƵ"