# This is a unit test file.

label start:
    
    call renpyper_init
    
    scene bg room
    show eileen happy
    
    call unit_test_traits
    
    call unit_test_flags
    
    call unit_test_characters
    
    call unit_test_events
    
    call unit_test_properties
    
    call unit_test_abilities
    
    "All unit tests completed."
    
    return
