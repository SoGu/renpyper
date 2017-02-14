label unit_test_events:
    
    $ global_traits['confidence'] = Trait()
    $ global_traits['happyness'] = Trait()
    $ global_moods['tiredness'] = RenpyperMood(val = 500)
    $ char1 = RenpyperCharacter(name = 'Romeo')
    $ char2 = RenpyperCharacter(name = 'Juliet')
    $ listOfCharacters = [char1, char2]
    
    $ testEvent = RenpyperEvent(duration = 100)
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
    if global_characters['Romeo'].mood('tiredness').get() != 600 or global_characters['Juliet'].mood('tiredness').get() != 600:
        "Time hook function wasn't called correctly on an event's end."
        
    $ testEvent = RenpyperEvent(name = 'Go to bed')
    
    python:
        def effectOfEventGoToBed(character):
            global_characters[character].mood('tiredness').value_ -= 500
            
    $ testEvent.addEffect(effectOfEventGoToBed)
    
    if testEvent.effects_[0] != [effectOfEventGoToBed, -1]:
        "Adding an effect to an event didn't work."
        
    $ testEvent.start([char2]) # send Juliet to bed
    $ testEvent.end()
    if char2.mood('tiredness').get() != 100:
        "Applying the automatic effects of an event to characters didn't work."
    
    $ testEvent.effects_ = [] # reset the effects
    
    $ testEvent.addEffect(effectOfEventGoToBed, 0)
    
    if testEvent.effects_[0] != [effectOfEventGoToBed, 0]:
        "Adding an effect with a specific character to an event didn't work."
        
    $ testEvent.start([char1, char2]) # now send both to bed although the effect only applies to char1
    $ testEvent.end()
    
    $ char2.mood('tiredness').value_ = 555 # cheat to set the value manually
    
    if char1.mood('tiredness').get() != 100 or char2.mood('tiredness').get() != 555:
        "Applying an effect to specific characters within an event didn't work correctly."

    $ del listOfCharacters
    $ del char1
    $ del char2
    $ global_traits.clear()
    $ global_moods.clear()
    $ del testEvent
    
    # TODO :
    # Add a more thorough test suite:
    # At least 3 characters
    # At least 3 traits
    # At least 3 events that influence those characters (traits)
    
    return
    