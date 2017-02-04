label renpyper_event:
    python:
        class RenpyperEvent(object):
            involvedCharacters_ = []
            
            occured_ = 0
            
            active_ = False
            
            def __init__(self):
                pass
                
            def start(self, listOfCharacters = []):
                self.occured_ += 1
                self.active_ = True
                self.involvedCharacters_ = list(listOfCharacters)
                
            def end(self):
                self.active_ = False
                self.involvedCharacters_ = []
                
            def resetOccured(self, resetTo = 0):
                self.occured_ = resetTo
                
            def hasOccured(self):
                if self.occured_ > 0:
                    return True
                else:
                    return False
                    
            def occurences(self):
                return self.occured_
                
            def isActive(self):
                return self.active_
                
    return