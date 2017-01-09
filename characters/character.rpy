label renpyper_characters:
    python:        
        class RenpyperCharacter:
            # For easy storytelling, every renpyper character gets a native Ren'Py character as a member.
            # This makes writing dialog easier.
            rc_ = Character('', color="#000000")
            
            # A dictionary of all the traits the character has.
            # Should be a complete list of all defined traits.
            traits_ = dict()
            
            # This variable indicates, if this character is controlled by the user or not.
            # Is needed so the "AI" knows when to pick an answer and when to ask the user for one.
            player_ = False
                
            # Constructor
            # Creates the Ren'Py character internally to be used later in renpyper events
            def __init__(self, name, col, player=False):
                self.rc_ = Character(name, color=col)
                self.player_ = player
            
    return