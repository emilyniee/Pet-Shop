class Animal():
  '''
    This is an animal

    Attributes
    ----------
    gender : bool
        This will hold the gender of the animal as a boolean
        true = male
        false = female
    
    furColor : String
        This will hold the color of the animal's fur as a string
    
    eyeColor : String
        This will hold the color of the animal's eyes as a string
    
    age : int
        This will hold the age of the animal as an integer
    
    
    Methods
    -------
    birthday() -> None
        Increases the age of the animal by 1 year
    
    eat() -> String
        Returns a graphical depiction of an animal eating 
  '''

  def __init__(self, gender, furColor, eyeColor, age):
    '''
    Constructor to build an animal

    Parameters
    -------
    gender: boolean
      the gender of the animal
    
    furColor: String
      the color of the animal's fur

    eyeColor: String
      the color of the animal's eyes
    
    age: int
      the age of the animal at the moment in years

    Returns
    -------
    None

    '''
    self.gender = gender
    self.furColor = furColor
    self.eyeColor = eyeColor
    self.age = age
  
  def __str__(self):
    '''
    returns the basic information about the animal (gender, furColor, eyeColor, age)

    Parameters
    -------
    None

    Returns
    -------
    String
      a concatenated string with all basic information
    '''

    #changing the boolean value of gender to something more user friendly
    if self.gender == True:
      gender = "male"
    elif self.gender == False:
      gender = "female"
    
    return "Gender: " + str(gender) + "\n Fur Color: " + self.furColor + "\n Eye Color: " + self.eyeColor + "\n Age: " + str(self.age)

  def birthday(self):
    '''
    Increases the age of the pet by 1 year

    Parameters
    -------
    None  

    Returns
    -------
    None

    '''
    self.age += 1

  def eat(self):
    '''
    To mirror the animal eating a meal

    Parameters
    -------
    None  

    Returns
    -------
    String
      a graphical representation of eating

    '''
    return "(っ˘ڡ˘ς)"
  