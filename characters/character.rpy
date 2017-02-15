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
                return self.traits_[key]
                
            def trait(self, key):
                return self.getTrait(key)
                
            def getFlag(self, key):
                return self.flags_[key]
                
            def isPlayer(self):
                return self.player_
                
            def getPath(self):
                return self.resourcePath_
                
            def setPath(self, path):
                self.resourcePath_ = path
                
            def getProperty(self, key):
                return self.props_[key]
                
            def getProp(self, key):
                return self.getProperty(key)
                
            def getAbility(self, key):
                return self.abilities_[key]
                
            def getAb(self, key):
                return self.getAbility(key)
                
            def getMood(self, key):
                return self.moods_[key]
                
            def mood(self, key):
                return self.getMood(key)
                
            def getGoal(self, key):
                return self.goals_[key]
                
            def goal(self, key):
                return self.getGoal(key)
            
    return
    