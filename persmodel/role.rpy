label renpyper_role:
    
    python:
        class RenpyperRole(object):
            ## Name of the role, e.g. 'Lord'.
            name_ = ''
            
            ## Character currently in this role
            character_ = []
            
            ## Who can grant this position to a character.
            ## Can only be a position within the Role System.
            grantableBy_ = ''
            
            ## How many entities of this role may exist in a 
            number_ = 1
            
            def __init__(self, gr, nu, na):
                self.name_ = na
                self.grantableBy_ = gr
                self.number_ = nu
                
            def grant(self, character):
                if len(self.character_) < self.number_:
                    self.character_.append(character)
                
            def fire(self, char = None):
                if char is None:
                    self.character_ = []
                else:
                    self.character_ = list(filter(lambda x: x != char, a))
                
            def getChar(self):
                if len(self.character_) > 0:
                    return self.character_[0]
                else:
                    return None
                
            def getCharacter(self):
                return self.getChar()
                
            def get(self):
                return self.getChar()
                
            def getName(self):
                return self.name_
                
            def isFree(self):
                if len(self.character_) < self.number_:
                    return True
                else:
                    return False
                
            """def __deepcopy__(self, memo):
                newRole = type(self)()
                newRole.name_ = copy.deepcopy(self.name_, memo)
                newRole.character_ = None
                newRole.grantableBy_ = copy.deepcopy(self.grantableBy_, memo)
                newRole.number_ = copy.deepcopy(self.number_, memo)
                return newRole
            """
    
    return
    