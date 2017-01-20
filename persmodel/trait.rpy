# A trait object is a personality trait that describes a personality aspect of a character.
# A trait provides the most basic personality description entity, although it is very mighty.
# Most games can be written with only personality traits.
# A trait is described by one single integer value.
label renpyper_traits:
    python:
        class Trait(PersModel):
            # This value is the value that describes the character trait.
            value_ = 0
            
            # The highest and lowest value that the value can have.
            top_ = 0
            bottom_ = 0
            
            # This is the mode of operation on the value_ variable by functions like 
            # For example, when the mode is set to linear, incrementing will work linearly.
            mode_ = LINEAR
            
            # Constructor
            # Set all the important values
            def __init__(self, value = 500, top = 1000, bottom = 0, mode = LINEAR):
                self.value_ = value
                self.top_ = top
                self.bottom_ = bottom
                self.mode_ = mode
            
            # The basic getter method. Only use this method to receive the trait value.
            def getValue(self):
                return self.value_
                
            # Setter method. Most useful for initializing the value for a newly generated character.
            # Try not to use this method. Setting values to specific values is only realistic in extreme cases.
            # E.g.: A complete loss of trust after a failed murder attempt.
            # Other methods that provide smoother value changes are better in most cases.
            def setValue(self, newValue = 500):
                self.value_ = newValue
                
    return