label renpyper_goals:
    
    $ global_goals = {}
    
    python:
        class RenpyperGoal(object):
            name_ = ''
            
            goals_ = []
            
            events_ = []
            
            relativeImportance_ = 1
            
            persistent_ = True
            
            # Must return True if the goal is reached and False if it isn't.
            def reached_(self): pass
            
            def __init__(self, reached, persistent = True, name = '', importance = 1):
                self.reached_ = reached
                self.persistent_ = persistent
                self.name_ = name
                self.relativeImportance_ = importance
                self.goals_ = []
                self.events_ = []
                
            def __deepcopy__(self, memo):
                newGoal = type(self)(self.reached_)
                newGoal.name_ = copy.deepcopy(self.name_, memo)
                newGoal.goals_ = copy.deepcopy(self.goals_, memo)
                newGoal.events_ = copy.deepcopy(self.events_, memo)
                newGoal.relativeImportance_ = copy.deepcopy(self.relativeImportance_, memo)
                return newGoal
            
            def pursue(self):
                pass
                
            def addGoal(self, goal, effectiveness, bias):
                pass
                
            def addEvent(self, event, effectiveness):
                self.events_.append([event, effectiveness])
                
            def updateImportance(self):
                pass
                
            def reached(self, character):
                return self.reached_(character)
    
    return
    