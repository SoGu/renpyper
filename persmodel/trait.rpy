label renpyper_traits:
        
    call renpyper_trait_utils
    
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

            mode_ = RENPYPER_LINEAR      # The mode of operation of the increment function. Linear by default.
            
            nameTop_ = ""       # How the high value of this trait is called
            nameBottom_ = ""    # How the low value of this trait is called
            
            def incdec_(): pass # Function object that is used for incrementing
            
            def __init__(self, val = 500, top = 1000, bottom = 0, mode = RENPYPER_LINEAR, incdec = incdecLinear, topName = "", bottomName = ""):
                """ Constructor """
                self.top_ = top
                self.bottom_ = bottom
                if (val > self.top_):
                    self.value_ = top
                elif (val < self.bottom_):
                    self.value_ = bottom
                elif val == 0:
                    self.value_ = 0
                elif (val):
                    self.value_ = val
                else:
                    self.value_ = math.floor((self.top_ + self.bottom_) / 2)
                self.mode_ = mode
                self.nameTop_ = topName
                self.nameBottom_ = bottomName
                if (self.mode_ == RENPYPER_MANUAL):
                    self.incdec_ = incdec
                elif (self.mode_ == RENPYPER_LINEAR):
                    self.incdec_ = incdecLinear
                    
            def __deepcopy__(self, memo):
                newTrait = type(self)()
                newTrait.value_ = copy.deepcopy(self.value_, memo)
                newTrait.top_ = copy.deepcopy(self.top_, memo)
                newTrait.bottom_ = copy.deepcopy(self.bottom_, memo)
                newTrait.mode_ = copy.deepcopy(self.mode_, memo)
                newTrait.nameTop_ = copy.deepcopy(self.nameTop_, memo)
                newTrait.nameBottom_ = copy.deepcopy(self.nameBottom_, memo)
                return newTrait
            
            def getValue(self):
                """ The basic getter method. Use only this method to receive the trait value. """
                return self.value_
                
            def get(self):
                """ Shortcut for getValue() """
                return self.getValue()
                
            def setValue(self, newValue = 500):
                """ Setter method. Most useful for initializing the value for a newly generated character.
                Try not to use this method. Setting values to specific values is only realistic in extreme cases.
                E.g.: A complete loss of trust after a failed murder attempt.
                Other methods that provide smoother value changes are better in most cases.
                """
                if (newValue > self.top_):
                    self.value_ = self.top_
                elif (newValue < self.bottom_):
                    self.value_ = self.bottom_
                else:
                    self.value_ = newValue
                
            def set(self, newValue = 500):
                """ Shortcut for setValue() """
                self.setValue(newValue)
                              
            def inc(self, var):
                self.value_ = self.incdec_(var, self.value_)
                if (self.value_ > self.top_):
                    self.value_ = self.top_
                if (self.value_ < self.bottom_):
                    self.value_ = self.bottom_
                    
            def topName(self):
                """ Return a word for the top value. E.g. 'trust' """
                return self.nameTop_
                
            def bottomName(self):
                """ Return a word for the top value. E.g. 'mistrust' """
                return self.nameBottom_
                
            def getTopName(self):
                return self.topName()
                
            def getBottomName(self):
                return self.bottomName()
                
    return
    