label renpyper_moods:
    
    $ global_moods = {}
    
    python:
        class RenpyperMood(RenpyperTrait):
            helper_ = 0
            
            def timeHook_(): pass
            
            def __init__(self, val = 500, top = 1000, bottom = 0, mode = RENPYPER_LINEAR_MOOD,
                incdec = incdecLinear, topName = '', bottomName = '', timeHook = defaultMoodTimeHookFunction,
                helper = 0):
                super(RenpyperMood, self).__init__(val, top, bottom, mode, incdec, topName, bottomName)
                self.timeHook_ = timeHook
                self.helper_ = helper
                if mode == RENPYPER_LINEAR_MOOD:
                    self.incdec_ = incdecLinear
                
            def __deepcopy__(self, memo):
                newMood = type(self)()
                newMood.value_ = copy.deepcopy(self.value_, memo)
                newMood.top_ = copy.deepcopy(self.top_, memo)
                newMood.bottom_ = copy.deepcopy(self.bottom_, memo)
                newMood.mode_ = copy.deepcopy(self.mode_, memo)
                newMood.nameTop_ = copy.deepcopy(self.nameTop_, memo)
                newMood.nameBottom_ = copy.deepcopy(self.nameBottom_, memo)
                newMood.timeHook_ = copy.deepcopy(self.timeHook_, memo)
                return newMood
                
            def timeHook(self, time, helper = 0):
                self.value_ = self.timeHook_(self.value_, time, helper)
                if (self.value_ > self.top_):
                    self.value_ = self.top_
                if (self.value_ < self.bottom_):
                    self.value_ = self.bottom_
    
    return
    