label renpyper_characters:
    python:
        
        global_characters = {}
        
        class RenpyperCharacter(object):
            # For easy storytelling, every renpyper character gets a native Ren'Py character as a member.
            # This makes writing dialog easier.
            rc_ = Character('', color="#000000")
            
            # Path to the directory where the resources for this character are saved.
            resourcePath_ = ''
            
            name_ = ''
            
            # Dictionaries of the different personality model objects.
            traits_ = {}
            flags_ = {}
            props_ = {}
            abilities_ = {}
            moods_ = {}
            goals_ = {}
            
            # This variable indicates, if this character is controlled by the user or not.
            # Is needed so the "AI" knows when to pick an answer and when to ask the user for one.
            player_ = False
                
            # Constructor
            # Creates the Ren'Py character internally to be used later in renpyper events
            def __init__(self, name = '', col = "#000000", player=False):
                self.rc_ = Character(name, color=col)
                self.player_ = player
                self.traits_ = copy.deepcopy(global_traits)
                self.flags_ = copy.deepcopy(global_flags)
                self.props_ = copy.deepcopy(global_properties)
                self.abilities_ = copy.deepcopy(global_abilities)
                for ab in self.abilities_:
                    self.abilities_[ab].superCharacterKey_ = name
                self.moods_ = copy.deepcopy(global_moods)
                self.goals_ = copy.deepcopy(global_goals)
                self.name_ = name
                if name != '':
                    global_characters[name] = self
                    
            def __del__(self):
                del global_characters[self.name_]
                
            def getName(self):
                return self.name_
                
            def getTrait(self, key):
                return self.traits_[key].get()
                
            def setTrait(self, key, newValue):
                self.traits_[key].set(newValue)
                
            def incTrait(self, key, inc):
                self.traits_[key].inc(inc)
                
            def trait(self, key):
                return self.traits_[key]
                
            def flag(self, key):
                return self.flags_[key]
                
            def getFlag(self, key):
                return self.flags_[key].get()
                
            def setFlag(self, key):
                self.flags_[key].setValue(True)
                
            def unsetFlag(self, key):
                self.flags_[key].setValue(False)
                
            def isPlayer(self):
                return self.player_
                
            def getPath(self):
                return self.resourcePath_
                
            def setPath(self, path):
                self.resourcePath_ = path
                
            def getProperty(self, key):
                return self.props_[key].get()
                
            def getProp(self, key):
                return self.getProperty(key)
                
            def setProperty(self, key, string):
                self.props_[key].setValue(string)
                
            def setProp(self, key, string):
                self.setProperty(key, string)
                
            def property(self, key):
                return self.props_[key]
                
            def prop(self, key):
                return self.property(key)
                
            def getAbility(self, key):
                return self.abilities_[key].get()
                
            def getAb(self, key):
                return self.getAbility(key)
                
            def setAbility(self, key, newValue):
                self.abilities_[key].setValue(newValue)
                
            def setAb(self, key, newValue):
                self.setAbility(key, newValue)
                
            def setTalent(self, key, newTalent):
                self.abilities_[key].setTalent(newTalent)
                
            def getTalent(self, key):
                return self.abilities_[key].getTalent()
                
            def learn(self, key, var):
                self.abilities_[key].learn(var)
                
            def ability(self, key):
                return self.abilities_[key]
                
            def ab(self, key):
                return self.ability(key)
                
            def getMood(self, key):
                return self.moods_[key].get()
                
            def setMood(self, key, newValue):
                self.moods_[key].set(newValue)
                
            def incMood(self, key, inc):
                self.moods_[key].inc(inc)
                
            def mood(self, key):
                return self.moods_[key]
                
            def goal(self, key):
                return self.goals_[key]
                
            def addGoal(self, goal, name):
                self.goals_[name] = goal
            
    return