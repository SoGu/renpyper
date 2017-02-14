label unit_tests_moods:
    
    $ testMood = RenpyperMood(topName = 'Tiredness')
    if testMood.getTopName() != 'Tiredness':
        "Creating a Mood object didn't work."
    $ del testMood
    
    python:
        def testTimeHook(current, time, helper):
            return current - time * (helper + 1)
    
    $ testMood = RenpyperMood(top = 1000, bottom = 0, val = 444, timeHook = testTimeHook)
    if testMood.getValue() != 444:
        "Creating a Mood with a specific value didn't work."
    $ testMood.timeHook(111)
    if testMood.getValue() != 333:
        "Mood object didn't react to the timeHook function."
    $ del testMood
            
    $ del testTimeHook
    
    return
    