label unit_test_events:
    
    $ global_traits['confidence'] = Trait()
    $ global_traits['happyness'] = Trait()
    $ char1 = RenpyperCharacter(name = 'Romeo')
    $ char2 = RenpyperCharacter(name = 'Juliet')
    $ listOfCharacters = [char1, char2]
    
    $ testEvent = RenpyperEvent()
    $ testEvent.start(listOfCharacters)
    if not testEvent.hasOccured():
        "Starting the test event or setting the occurence counter didn't work."
    $ testEvent.resetOccured()
    if testEvent.hasOccured():
        "Resetting the occurence counter didn't work."
    python:
        for x in range(0,10):
            testEvent.start(listOfCharacters)
    if testEvent.occurences() != 10:
        "Number of occurences does not match the number of times the event was started. Was there a problem with resetting the counter?"
    
    if not testEvent.isActive():
        "Setting an event to active didn't work."
        
    $ testEvent.end()
    if testEvent.isActive():
        "Setting an event to inactive again didn't work."
    
    $ del listOfCharacters
    $ del char1
    $ del char2
    $ global_traits.clear()
    
    return