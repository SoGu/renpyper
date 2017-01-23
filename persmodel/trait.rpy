label renpyper_traits:
    python:
        class Trait(PersModel):
            """A trait object is a personality trait that describes a personality aspect of a character.
            A trait provides the most basic personality description entity, although it is very mighty.
            Most games can be written with only personality traits.
            A trait is described by one single integer value.
            """
            
            value_ = 0
            
            top_ = 0    # The highest value that value_ can have.
            bottom_ = 0 # The lowest value that value_ can have.
            
            # This is the mode of operation on the value_ variable by functions like 
            # For example, when the mode is set to linear, incrementing will work linearly.
            mode_ = LINEAR
            
            def incdec_(): pass
            
            def __init__(self, value = 500, top = 1000, bottom = 0, mode = LINEAR, incdec = incdecLinear):
                """ Constructor """
                self.value_ = value
                self.top_ = top
                self.bottom_ = bottom
                self.mode_ = mode
                self.incdec_ = incdec
            
            def getValue(self):
                """ The basic getter method. Use only this method to receive the trait value."""
                return self.value_
                
            def get(self):
                return self.getValue()
                
            def setValue(self, newValue = 500):
                """Setter method. Most useful for initializing the value for a newly generated character.
                Try not to use this method. Setting values to specific values is only realistic in extreme cases.
                E.g.: A complete loss of trust after a failed murder attempt.
                Other methods that provide smoother value changes are better in most cases.
                """
                self.value_ = newValue
                              
            def inc(self, var):
                if (self.mode_ == LINEAR):
                    self.value_ = self.incdec_(var, self.value_, self.top_, self.bottom_)
                    
                

                
    return