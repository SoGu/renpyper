label renpyper_flags:
    
    $ global_flags = {}
    
    python:
        class RenpyperFlag(PersModel):
            
            val_ = None
            
            name_ = ''
            
            def __init__(self, name = '', val = None):
                self.name_ = name
                self.val_ = val
            
            def getValue(self):
                return self.val_
                
            def setValue(self, val):
                self.val_ = val
                
            def get(self):
                return self.getValue()
                
            def set(self, newValue):
                self.setValue(newValue)
                
            def getName(self):
                return self.name_
            
            def __deepcopy__(self, memo):
                newFlag = type(self)()
                newFlag.val_ = copy.deepcopy(self.val_, memo)
                newFlag.name_ = copy.deepcopy(self.name_, memo)
                return newFlag
    
    return