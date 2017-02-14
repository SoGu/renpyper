label renpyper_trait_utils:
    python:        
        global_traits = {} # global traits dict that gets (deep-)copied into every character object
        
        def incdecLinear(var, val):
            """ This function increments or decrements the trait linearly."""
            return val + var
            
        def incdecLinearAbility(current, toLearn, talent, base):
            return math.floor(current + toLearn * (talent + base))
            
        def emptyAbilityInfluenceFunction(key):
            return 0
            
        def defaultMoodTimeHookFunction(time):
            pass

    return
    