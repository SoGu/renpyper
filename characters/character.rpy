label renpyper_characters:
    python:
        
        class RenpyperCharacter(object):
            # For easy storytelling, every renpyper character gets a native Ren'Py character as a member.
            # This makes writing dialog easier.
            rc_ = Character('', color="#000000")
            
            # Path to the directory where the resources for this character are saved.
            resourcePath_ = ''
            
            # A dictionary of all the traits the character has.
            traits_ = {}
            
            # A dictionary of all the flags the character has.
            flags_ = {}
            
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
                
            def getTrait(self, key):
                return self.traits_[key]
                
            def getFlag(self, key):
                return self.flags_[key]
                
            def isPlayer(self):
                return self.player_
                
            def getPath(self):
                return self.resourcePath_
                
            def setPath(self, path):
                self.resourcePath_ = path
            
    return