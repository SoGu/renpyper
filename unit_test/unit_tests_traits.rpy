label unit_test_traits:
    
    $ testTrait = RenpyperTrait()
    if testTrait is None:
        "Couldn't create a Trait object."
    $ testTrait.set(55)
    if testTrait.get() is not 55:
        "Setting a trait value didn't work."
    $ del testTrait
    
    $ testTrait = RenpyperTrait(val = 76)
    if testTrait.get() is not 76:
        "Creating a trait object with a certain value didn't work."
    $ del testTrait
            
    $ testTrait = RenpyperTrait(top = 101, bottom = 2)
    if testTrait.top_ is not 101 or testTrait.bottom_ is not 2:
        "Creating a trait object with top and bottom values didn't work."
    $ del testTrait
        
    $ testTrait = RenpyperTrait(top = 103, bottom = 14, val = 105)
    if testTrait.get() is not 103:
        "Boundaries of top or bottom violated."
    $ testTrait.set(3)
    if testTrait.get() is not 14:
        "Boundaries of top or bottom violated."
    $ del testTrait
    
    $ testTrait = RenpyperTrait(val = 24)
    $ testTrait.inc(12)
    if testTrait.get() is not 36:
        "Incrementing the value didn't work."
    $ testTrait.inc(-16)
    if testTrait.get() is not 20:
        "Decrementing the value didn't work."
    $ del testTrait
    
    $ testTrait = RenpyperTrait(top = 100, bottom = -10, val = 50)
    $ testTrait.inc(100)
    if testTrait.get() is not 100:
        "Incrementing led to out of bounds error."
    $ testTrait.inc(-333)
    if testTrait.get() != -10:
        "Decrementing led to out of bounds error."
    $ del testTrait
    
    $ testTrait = RenpyperTrait(val = 500)
    $ copiedTrait = copy.deepcopy(testTrait)
    $ testTrait.set(400)
    if copiedTrait.get() is 400:
        "Deepcopy didn't copy correctly, the cloned object is still bound to the original somehow."
    $ del testTrait
    $ del copiedTrait
    
    $ testTrait = RenpyperTrait(topName = 'Trustfulness', bottomName = 'Distrust')
    if testTrait.topName() != 'Trustfulness' or testTrait.bottomName() != 'Distrust':
        "Setting and retrieving topName or bottomName didn't work correctly."
    $ del testTrait
    
    return