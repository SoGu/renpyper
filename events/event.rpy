label renpyper_event:
    python:
        class RenpyperEvent(object):
            involvedCharacters_ = []
            
            occured_ = 0
            
            active_ = False
            
            def __init__(self, listOfCharacters):
                self.involvedCharacters_ = list(listOfCharacters)
                
            def start(self):
                self.occured_ += 1
                self.active_ = True
                
            def end(self):
                self.active_ = False
                
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