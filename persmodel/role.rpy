label renpyper_role:
    
    python:
        class RenpyperRole(object):
            ## Name of the role, e.g. 'Lord'.
            name_ = ''
            
            ## Character currently in this role
            character_ = None
            
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
                self.character_ = character
                
            def fire(self):
                self.character_ = None
                
            def getChar(self):
                return self.character_
                
            def getCharacter(self):
                return self.getChar()
                
            def get(self):
                return self.getChar()
                
            def getName(self):
                return self.name_
                
            def isFree(self):
                if self.character_ is not None:
                    return False
                else:
                    return True
                
            """def __deepcopy__(self, memo):
                newRole = type(self)()
                newRole.name_ = copy.deepcopy(self.name_, memo)
                newRole.character_ = None
                newRole.grantableBy_ = copy.deepcopy(self.grantableBy_, memo)
                newRole.number_ = copy.deepcopy(self.number_, memo)
                return newRole
            """
    
    return
    