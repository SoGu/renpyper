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
    
    python:
        global_traits['determination'] = Trait(top = 100, bottom = 0, val = 50, topName = 'determined', mode = RENPYPER_LINEAR)
        global_traits['talent'] = Trait(top = 100, bottom = 0, val = 50, topName = 'talented', mode = RENPYPER_LINEAR)
        global_traits['experience'] = Trait(top = 100, bottom = 0, val = 50, topName = 'experienced', mode = RENPYPER_LINEAR)
        
        def incFitness(current, time, effect):
            return current + time * effect
        
        global_moods['fitness'] = RenpyperMood(top = 100, bottom = 0, val = 100, timeHook = incFitness)
        
        athlete1 = RenpyperCharacter(name = 'Messi')
        athlete2 = RenpyperCharacter(name = 'Ronaldo')
        athlete3 = RenpyperCharacter(name = 'Monty')
        
        athlete1.trait('determination').set(87)
        athlete1.trait('talent').set(91)
        athlete1.trait('experience').set(76)
        
        athlete2.trait('determination').set(98)
        athlete2.trait('talent').set(81)
        athlete2.trait('experience').set(88)
        
        athlete3.trait('determination').set(22)
        athlete3.trait('talent').set(99)
        athlete3.trait('experience').set(26)
        
        eventTrain = RenpyperEvent(name = 'Training', duration = 3)
        eventPlay = RenpyperEvent(name = 'Match', duration = 2)
        eventRest = RenpyperEvent(name = 'Rest', duration = 6, label = 'unit_test_event_rest')
        
        def effectOfTrain(character):
            global_characters[character].trait('experience').inc(1)
            global_characters[character].mood('fitness').inc(-5)
            
        def effectOfPlay(character):
            global_characters[character].trait('experience').inc(2)
            global_characters[character].trait('determination').inc(-1)
            global_characters[character].mood('fitness').inc(-10)
            
        def effectOfRest(character):
            global_characters[character].trait('talent').inc(1)
            global_characters[character].mood('fitness').inc(20)
            
        eventTrain.addEffect(effectOfTrain)
        eventPlay.addEffect(effectOfPlay)
        eventRest.addEffect(effectOfRest)
            
        eventTrain.start([athlete1, athlete2])
        eventTrain.end()
    if (athlete1.trait('experience').get() != 77 or
        athlete1.mood('fitness').get() != 95 or
        athlete2.trait('experience').get() != 89 or
        athlete2.mood('fitness').get() != 95 or
        athlete1.trait('determination').get() != 87 or
        athlete3.trait('experience').get() != 26 or
        athlete3.mood('fitness').get() != 100):
        "Something regarding events and event effects didn't work correctly."
        
    $ eventPlay.start([athlete1, athlete3, athlete2])
    $ eventPlay.end()
    if (athlete1.trait('determination').get() != 86 or
        athlete1.mood('fitness').get() != 85 or
        athlete3.trait('experience').get() != 28):
        "Something regarding events and event effects didn't work correctly."
        
    $ wasInEvent = False
    $ jumpTo = eventRest.label_
    $ renpy.call(jumpTo)
    if not wasInEvent:
        "Jumping to a label defined in an event didn't work."
    $ del jumpTo
    $ del wasInEvent
        
    python:
        del effectOfTrain
        del effectOfPlay
        del effectOfRest
        del eventTrain
        del eventPlay
        del eventRest
        global_traits.clear()
        global_moods.clear()
        del athlete1
        del athlete2
        del athlete3
        
    return
        
label unit_test_event_rest:
    $ wasInEvent = True
    return
    