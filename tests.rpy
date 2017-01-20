# The script of the game goes in this file.

# The game starts here.
label start:
    
    call renpyper_init
    
    # The game itself starts here now    
    scene bg room
    show eileen happy
        
    call renpyper_testEvent(Player, MaxMustermann)

    return
