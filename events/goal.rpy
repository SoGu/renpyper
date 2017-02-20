label renpyper_goals:
    
    $ global_goals = {}
    
    python:
        class RenpyperGoal(object):
            name_ = ''
            
            goals_ = []
            
            events_ = []
            
            persistent_ = True
            
            # Must return True if the goal is reached and False if it isn't.
            def reached_(self): pass
            
            def __init__(self, reached, persistent = True, name = ''):
                self.reached_ = reached
                self.persistent_ = persistent
                self.name_ = name
                self.goals_ = []
                self.events_ = []
                
            def __deepcopy__(self, memo):
                newGoal = type(self)(self.reached_)
                newGoal.name_ = copy.deepcopy(self.name_, memo)
                newGoal.goals_ = copy.deepcopy(self.goals_, memo)
                newGoal.events_ = copy.deepcopy(self.events_, memo)
                return newGoal
            
            ## returns an event object - this is the event the character wants to do now
            def pursue(self, strength = 0.5):
                sumOfGoals = 0
                for i in self.goals_:
                    sumOfGoals += i[1]
                sumOfEvents = 0
                for i in self.events_:
                    sumOfEvents += i[1]
                
                sum = sumOfEvents + sumOfGoals
                randNr = randint(0, sum)
                eventStrength = sumOfEvents/sum*strength + randNr*(1-strength)
                goalStrength = sumOfGoals/sum*strength + (sum-randNr)*(1-strength)
                
                if (eventStrength >= goalStrength or
                    sumOfGoals == 0): # this one actually cost me a few hours of debugging... -.-
                    tmpEventList = []
                    for h in self.events_:
                        tmpEventList.append([h[0], strength*h[1] + (1-strength)*randint(0, math.floor(sumOfEvents/len(self.events_)))])
                    max = 0
                    newEvent = None
                    for i in tmpEventList:
                        if i[1] > max:
                            max = i[1]
                            newEvent = i[0]
                    del tmpEventList
                    return newEvent
                else:
                    tmpGoalList = []
                    for j in self.goals_:
                        tmpGoalList.append([j[0], strength*j[1] + (1-strength)*randint(0, math.floor(sumOfGoals/len(self.goals_)))])
                    max = 0
                    newGoal = None
                    for k in tmpGoalList:
                        if k[1] >= max:
                            max = k[1]
                            newGoal = k[0]
                    del tmpGoalList
                    return newGoal.pursue(strength)
                
            def addGoal(self, goal, effectiveness):
                self.goals_.append([goal, effectiveness])
                
            def addEvent(self, event, effectiveness):
                self.events_.append([event, effectiveness])
                
            def reached(self, character):
                return self.reached_(character)
    
    return
    