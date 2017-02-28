label unit_test_abilities:
    
    $ testAb = RenpyperAbility()
    if testAb.get() != 0:
        "Creating an ability object didn't work."
    $ del testAb
    
    $ testAb = RenpyperAbility(val = 100)
    if testAb.get() != 100:
        "Setting the raw value for an ability object didn't work."
    $ del testAb
    
    $ testAb = RenpyperAbility(val = 100, top = 1000, bottom = 10)
    if testAb.get() != 100 or testAb.top_ != 1000 or testAb.bottom_ != 10:
        "Creating an ability object with boundaries didn't work."
    $ del testAb
    
    $ testAb = RenpyperAbility(val = 2000)
    if testAb.get() > 1000:
        "Creating an ability object with a value out of bounds worked."
    $ del testAb
    
    $ testAb = RenpyperAbility(base = 2)
    if testAb.base_ != 2:
        "Creating an ability object with a base value didn't work."
    $ del testAb
    
    $ testAb = RenpyperAbility(talent = 33)
    if testAb.getTalent() != 33:
        "Creating an ability object with a talent value didn't work."
    $ del testAb
    
    $ testAb = RenpyperAbility()
    $ testAb.set(55)
    if testAb.get() != 55:
        "Setting the value in an ability object didn't work."
    $ del testAb
    
    python:
        def testInflFunction(key):
            return 3
    
        testAb = RenpyperAbility(influence = testInflFunction)
        
    if testAb.influence_ is not testInflFunction:
        "Setting the influence function to a custom function in an ability didn't work."
    
    $ testAb.set(55)
    $ result = testAb.get()
    
    if result != 58:
        "Influence function didn't work correctly and wasn't used correctly in the get() method."
    
    $ del testAb
    $ del result
    $ del testInflFunction
    
    return
    