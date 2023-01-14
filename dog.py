from pet import Pet


class Dog(Pet):
  '''
    This is a dog that inherits attributes and methods from the Pet parent class

    Attributes
    ----------
    trainedToServe: boolean
      This will indicate whether or not the dog is trained to serve as a support animal
    
    tricks: array
      This will hold all the tricks the dog knows in an array
    
    Methods
    -------
    changeTrainedToServe() -> None
        Changes the status of the service animal to the opposite of what it currently is
    
    learnTrick(newTrick: String) -> None
        Adds the newly learned trick to the array of learned tricks

    wagTail() -> String
        Returns a graphical representation of the dog wagging its tail
    
    bark() -> String
        Returns the sound effect of barking
    
  '''
  def __init__(self, name, gender, furColor, eyeColor, age, breed, forAdoption = True, neutered = False, childFriendly = 5, trainedToServe = False, tricks = []):
    '''
    Constructor to build a dog

    Parameters
    -------
    trainedToServe: boolean
      the service status of the dog
      the default is False, not trained to serve
    
    tricks: array
      the array of tricks the dog already knows
      the default is an empty array, the dog knows no tricks

    Returns
    -------
    None

    '''
    super().__init__(name, gender, furColor, eyeColor, age, breed, forAdoption, neutered, childFriendly)
    self.trainedToServe = trainedToServe
    self.tricks = tricks
    
  
  def __repr__(self):
    '''
    returns the basic information about the dog (trainedToServe, tricks)

    Parameters
    -------
    None

    Returns
    -------
    String
      a concatenated string with all basic information
    '''

    #changing the boolean value of trainedToServe to something more user friendly
    if self.trainedToServe == True:
      trainedToServe = "yes"
    else:
      trainedToServe = "no"
    
    return super().__str__() + "\n Trained to Serve?: " +  str(trainedToServe) + "\n Tricks: " + str(self.tricks)
    

  def changeTrainedToServe(self):
    '''
    Changes the service status of the dog from True (trained to serve) to false (not trained to serve) and vice versa

    Parameters
    -------
    None
    
    Returns
    -------
    None
    '''
    self.trainedToServe = not self.trainedToServe
  
  def learnTrick(self, newTrick):
    '''
    Adds a new trick to the dog's list of known tricks

    Parameters
    -------
    newTrick: String
      the new trick the dog learned
    
    Returns
    -------
    None
    '''
    self.tricks.append (newTrick)

  def wagTail(self):
    '''
    Mirrors the dog wagging its tail

    Parameters
    -------
    None
    
    Returns
    -------
    String
      a graphical representation of a dog wagging its tail
    '''
    return "▽･ｪ･▽ﾉ"

  def bark(self):
    '''
    Mirrors the dog barking

    Parameters
    -------
    None
    
    Returns
    -------
    String
      the sound effect of barking
    '''
    return "🐕 woof"