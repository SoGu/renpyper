label renpyper_relationship:
    
    python:
        class RenpyperRelationship(object):
            ## Destination character
            destination_ = None
            
            memory_ = {}
            
            def updateMemory_(): pass
            
            def __init__(self, character, updateMemory = lambda x: None):
                self.destination_ = character
                self.updateMemory_ = updateMemory
                self.memory_ = {}
                
            def addMemory(self, key, value):
                self.memory_[key] = value
                
            def getMemory(self, key):
                return self.memory_[key]
                
            def updateMemory(self, key, superCharacter):
                self.updateMemory_(key, superCharacter, destination_)
    
    return
