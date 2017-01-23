label renpyper_trait_utils:
    python:
        def incdecLinear(var, val, top, bottom):
            """ This function increments or decrements the trait linearly."""
            retValue = val + var
            if (retValue > top):
                return top
            elif (retValue < bottom):
                return bottom
            else:
                return retValue
