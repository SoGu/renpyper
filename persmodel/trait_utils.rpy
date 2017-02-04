label renpyper_trait_utils:
    python:        
        global_traits = {} # global traits dict that gets (deep-)copied into every character object
        
        def incdecLinear(var, val, top, bottom):
            """ This function increments or decrements the trait linearly."""
            return val + var

    return