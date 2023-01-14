from pet import Pet


class Bunny(Pet):
  '''
    This is a bunny that inherits attributes and methods from the Pet parent class

    Attributes
    ----------
    hopStrength: int
      Holds the measure of the bunny's hop strength in terms of a number from 0-10

    favouriteVegetable: String
      Holds the bunny's favourite vegetable

    Methods
    -------
    increaseHopStrength(hopStrength) -> None
        Increases hopStrength of the bunny by a number of up to 10
    
    changeFavouriteVegetable(newFavouriteVegetable) -> None
        Changes the bunny's favouriteVegetable to newFavouriteVegetable

    hop() -> String
        Returns a graphical representation of a bunny hopping
    
    flop() -> String
        Returns a graphical representation of a bunny flopping
    
  '''
  def __init__(self, name, gender, furColor, eyeColor, age, breed, forAdoption = True, neutered = False, childFriendly = 5, hopStrength = 1, favouriteVegetable = "carrot"):
    '''
    Constructor to build a bunny

    Parameters
    -------
    hopStrength: int
      a scale from 0-10 for the hop strength of the bunny
      the default is 1
    
    favouriteVegetable: String
      the name of the bunny's favourite vegetable
      the default is "carrot"

    Returns
    -------
    None

    '''
    self.hopStrength = int(hopStrength)
    self.favouriteVegetable = favouriteVegetable
    super().__init__(name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly)
  
  def __repr__(self):
    '''
    returns the basic information about the bunny (hopStrength, favouriteVegetable)

    Parameters
    -------
    None

    Returns
    -------
    String
      a concatenated string with all basic information
    '''
    return super().__str__() + "\n Hop Strength: " +  str(self.hopStrength) + "\n Favourite vegetable: " + str(self.favouriteVegetable)
    
  
  def increaseHopStrength(self, hopStrength):
    '''
    Increases the hop strength of the bunny if the hop strength is not maxed (10)

    Parameters
    -------
    hopStrength: int
      the amount of strength to be increased
    
    Returns
    -------
    None
    '''
    if self.hopStrength + hopStrength <= 10:
      self.hopStrength += hopStrength
    else:
      self.hopStrength = 10
  
  def changeFavouriteVegetable(self, newFavouriteVegetable):
    '''
    Changes the favourite vegetable of the bunny

    Parameters
    -------
    newFavouriteVegetable: String
      the new favourite vegetable of the bunny
    
    Returns
    -------
    None
    '''
    self.favouriteVegetable = newFavouriteVegetable

  def hop(self):
    '''
    Mirrors the bunny hopping

    Parameters
    -------
    None
    
    Returns
    -------
    String
      a graphical representation of a bunny hopping
    '''
    return " ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ､., ⌒ ／( =ﾟｪﾟ=)"
    
  def flop(self):
    '''
    Mirrors the bunny flopping

    Parameters
    -------
    None
    
    Returns
    -------
    String
      a graphical represenyation of a bunny flopping
    '''
    return "_(:3」∠)_"