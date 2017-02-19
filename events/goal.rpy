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
                # 1. calculate goals weight
                sumOfGoals = 0
                for i in self.goals_:
                    sumOfGoals += i[1]
                # 2. calculate events weight
                sumOfEvents = 0
                for i in self.events_:
                    sumOfEvents += i[1]
                # decide if to take an event or a goal
                sum = sumOfEvents + sumOfGoals
                randNr = randint(0, sum)
                eventStrength = sumOfEvents/sum*strength + randNr*(1-strength)
                goalStrength = sumOfGoals/sum*strength + (sum-randNr)*(1-strength)
                # if event:
                if eventStrength >= goalStrength:
                #       calculate the event to return
                    chooser = randint(0, sumOfEvents)
                    for i in self.events_:
                        if chooser < i[1]:
                            return i[0]
                        else:
                            chooser -= i[1]
                # else:
                else:
                #       calculate the goal to persue
                    chooser = randint(0, sumOfGoals)
                    for i in self.goals_:
                        if chooser < i[1]:
                            return i[0].pursue(strength)
                        else:
                            chooser -= 1
                #       call persue function of that goal
                pass
                
            def addGoal(self, goal, effectiveness):
                self.goals_.append([goal, effectiveness])
                
            def addEvent(self, event, effectiveness):
                self.events_.append([event, effectiveness])
                
            def reached(self, character):
                return self.reached_(character)
    
    return
    