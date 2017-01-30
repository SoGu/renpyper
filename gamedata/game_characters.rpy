# This list defines all the characters that are present at the start of a game.
label renpyper_gameCharacters:
    python:
        # define Max Mustermann
        MaxMustermann = RenpyperCharacter('Max Mustermann', "#8f8f8f")
        MaxMustermann.traits_['trust'].set(23)
        
        # define playerCharacter
        Player = RenpyperCharacter('Me', "#d1d1d1", True)
        Player.traits_['trust'].set(55)
        
    return