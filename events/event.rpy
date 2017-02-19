label renpyper_event:
    python:
        class RenpyperEvent(object):
            name_ = ''
            
            label_ = ''
            
            involvedCharacters_ = []
            
            occured_ = 0
            
            active_ = False
            
            duration_ = 0
            
            effects_ = []
            
            def __init__(self, duration = 0, name = '',  label = ''):
                self.duration_ = duration
                self.name_ = name
                self.label_ = label
                self.effects_ = []
                
            def start(self, listOfCharacters = []):
                self.occured_ += 1
                self.active_ = True
                self.involvedCharacters_ = list(listOfCharacters)
                
            def end(self):
                # self.applyEffects()
                for i in self.involvedCharacters_:
                    for j in i.moods_:
                        i.moods_[j].timeHook(self.duration_)
                self.involvedCharacters_ = []
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
                
            def addEffect(self, effect, character = -1):
                self.effects_.append([effect, character]) # ... add an effect for that character
                
            def applyEffects(self):
                for i in self.effects_:
                    if i[1] == -1: # apply effect to all characters in event
                        for j in range(0, len(self.involvedCharacters_)):
                            i[0](self.involvedCharacters_[j].getName()) # apply effect to character
                    else:
                        i[0](self.involvedCharacters_[i[1]].getName()) # apply effect to a single character
                
    return