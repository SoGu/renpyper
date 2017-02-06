label renpyper_properties:
    python:
        
        global_properties = {}
        
        class RenpyperProperty(PersModel):
            prop_ = ''
            
            def __init__(self, prop = ''):
                self.prop_ = prop
                
            def getValue(self):
                return self.prop_
                
            def setValue(self, str):
                self.prop_ = str
                
            def get(self):
                return self.getValue()
                
            def set(self, str):
                self.setValue(str)
                
            def __deepcopy__(self, memo):
                newProp = type(self)()
                newProp.prop_ = copy.deepcopy(self.prop_, memo)
                return newProp
    
    return
    