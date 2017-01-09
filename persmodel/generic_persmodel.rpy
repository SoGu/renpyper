# The generic personality model is the core of the simulation of the game.
# All the personality model entities are encoded as renpyper_genericPersmod classes.
# This class is an interface and provides common basic functionality.
label renpyper_genericPersmod:
    python:
        class PersModel:
            def __init__(self):
                pass
            
            def getValue(self):
                pass
                
            def setValue(self):
                pass
                
    return