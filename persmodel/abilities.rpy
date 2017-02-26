label renpyper_abilities:
    
    $ global_abilities = {}
    
    python:
        class RenpyperAbility(RenpyperTrait): 
            # How fast a character can achieve an ability.
            talent_ = 0.0
            
            # Base learning rate, is added to talent.
            base_ = 1.0
            
            superCharacterKey_ = ''
            
            def influence_(): pass
            
            def __init__(self, base = 1, talent = 0, val = 0, top = 1000, bottom = 0,
                mode = RENPYPER_LINEAR_ABILITY, incdec = incdecLinear, topName = "", bottomName = "",
                influence = None):
                super(RenpyperAbility, self).__init__(val, top, bottom, mode, incdec, topName, bottomName)
                self.talent_ = talent
                self.base_ = base
                if influence == None:
                    self.influence_ = emptyAbilityInfluenceFunction
                else:
                    self.influence_ = influence
                if self.mode_ == RENPYPER_LINEAR_ABILITY:
                    self.incdec_ = incdecLinearAbility
                
            def getValue(self):
                return self.value_
                
            def get(self):
                return self.getRawValue() + self.influence_(self.superCharacterKey_)
                
            def getRawValue(self):
                return self.value_
                
            def getTalent(self):
                return self.talent_
                
            def setTalent(self, talent):
                self.talent_ = talent
                
            def getBase(self):
                return self.base_
                
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
                newAb.influence_ = self.influence_
                return newAb
                
            def learn(self, var):
                self.value_ = self.incdec_(self.value_, var, self.talent_, self.base_)
                if self.value_ > self.top_:
                    self.value_ = self.top_
                if self.value_ < self.bottom_:
                    self.value_ = self.bottom_
                    
            def setKey(self, key):
                self.superCharacterKey_ = key
                
    return
    