# This is a unit test file.

label start:
    
    call renpyper_init
    
    scene bg room
    show eileen happy
    
    # TODO: Test Trait generation, copying and data manipulation
    call unit_test_traits
    
    # TODO: Test Character generation and data manipulation
    
    "All unit tests completed."
    
    return
