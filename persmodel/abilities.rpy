label renpyper_abilities:
    
    global_abilities = {}
    
    python:
        class RenpyperAbility(Trait): 
            # How fast a character can achieve an ability.
            talent_ = 0
            
            base_ = 1
            
            def __init__(self, base = 1, talent = 0, val = 0, top = 1000, bottom = 0, mode = RENPYPER_LINEAR, incdec = incdecLinear, topName = "", bottomName = ""):
                super(RenpyperAbility, self).__init__(val, top, bottom, mode, incdec, topName, bottomName)
                self.talent_ = talent
                self.base_ = base
                
            def getValue(self):
                return self.value_
               
            # Warning: Do only use this method when initializing an object.
            # Every other way of using it may cause unintended behaviour.
            def setValue(self, newValue):
                self.value_ = newValue
                
            def get(self):
                return self.getValue()
                
            def set(self, newValue):
                self.setValue(newValue)
                
            def getTalent(self):
                return self.talent_
                
            def __deepcopy__(self, memo):
                newAb = type(self)()
                newAb.value_ = copy.deepcopy(self.value_, memo)
                newAb.top_ = copy.deepcopy(self.top_, memo)
                newAb.bottom_ = copy.deepcopy(self.bottom_, memo)
                newAb.mode_ = copy.deepcopy(self.mode_, memo)
                newAb.nameTop_ = copy.deepcopy(self.nameTop_, memo)
                newAb.nameBottom_ = copy.deepcopy(self.nameBottom_, memo)
                newAb.talent_ = copy.deepcopy(self.talent_, memo)
                newAb.base_ = copy.deepcopy(self.base_, memo)
                return newAb
                
    return
    