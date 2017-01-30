label unit_test_traits:
    
    $ testTrait = Trait()
    
    if testTrait is None:
        "Couldn't create a Trait object."
        
    $ testTrait.set(55)
    if testTrait.get() is not 55:
        "Setting a trait value didn't work."
        
    $ del testTrait
    
    ### ----- ###
    
    $ testTrait = Trait(val = 76)
    if testTrait.get() is not 76:
        "Creating a trait object with a certain value didn't work."
    $ del testTrait
            
    $ testTrait = Trait(top = 101, bottom = 2)
    if testTrait.top_ is not 101 or testTrait.bottom_ is not 2:
        "Creating a trait object with top and bottom values didn't work."
    $ del testTrait
        
    $ testTrait = Trait(top = 103, bottom = 14, val = 105)
    if testTrait.get() is not 103:
        "Boundaries of top or bottom violated."
    $ testTrait.set(3)
    if testTrait.get() is not 14:
        "Boundaries of top or bottom violated."
    $ del testTrait
        
    return