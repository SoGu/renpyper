label unit_test_goals:
    
    $ testGoal = RenpyperGoal(reached = lambda x: False, name = 'Sleep')
    if testGoal.name_ != 'Sleep':
        "Creating a simple Goal object didn't work."
    $ del testGoal
    
    python:
        def sleepGoalReached(character):
            if global_characters[character].mood('Tiredness').get() < 200:
                return True
            else:
                return False
    
    $ global_moods['Tiredness'] = RenpyperMood(top = 1000, bottom = 0, val = 500)
    $ global_goals['Sleep'] = RenpyperGoal(reached = sleepGoalReached, name = 'Sleep')
    $ testChar1 = RenpyperCharacter(name = 'Brian')
    $ testChar2 = RenpyperCharacter(name = 'Monty')
    
    if testChar1.goal('Sleep').reached('Brian') != False:
        "Basic setup of a system using goals didn't work."
    # make Monty awake now:
    $ testChar2.mood('Tiredness').value_ = 50
    if testChar2.goal('Sleep').reached(testChar2.getName()) != True:
        "Determining if a goal was reached didn't work correctly."

    python:
        eventSleep = RenpyperEvent(name = 'Go to bed')
        
        def effectEventSleep(character):
            global_characters[character].mood('Tiredness').inc(-500)
            
        eventSleep.addEffect(effectEventSleep)
        
        global_goals['Sleep'].addEvent(event = eventSleep, effectiveness = 100)
        
    if global_goals['Sleep'].events_[0][0] != eventSleep:
        "Adding an event to a goal didn't work."
    
    $ testGoal2 = RenpyperGoal(reached = lambda x: False, name = 'Fit for race day')
    $ testGoal2.addGoal(global_goals['Sleep'], effectiveness = 20)
    if testGoal2.goals_[0][0] != global_goals['Sleep'] or testGoal2.goals_[0][1] != 20:
        "Adding a goal to a goal didn't work."
        
    $ del testChar1
    $ del testChar2
    $ del sleepGoalReached
    $ global_goals.clear()
    $ global_moods.clear()
    
    
    python:
        global_events['Play Piano'] = RenpyperEvent(name = 'Play Piano')
        global_events['Read a Book'] = RenpyperEvent(name = 'Read a Book about playing Piano')
        global_events['Earn Money'] = RenpyperEvent(name = 'Earn Money')
        global_events['Buy new Piano'] = RenpyperEvent(name = 'Buy new Piano')
        
        global_flags['Owns Piano'] = RenpyperFlag(name = 'Owns Piano')
        
        global_abilities['Piano Skill'] = RenpyperAbility(top = 1000, bottom = 0, val = 0)
        
        def boughtPianoGoalReached(character):
            if character.getFlag('Owns Piano').get() == True:
                return True
            else:
                return False
                
        global_goals['Buy new Piano'] = RenpyperGoal(reached = boughtPianoGoalReached)
        global_goals['Buy new Piano'].addEvent(global_events['Earn Money'], 100)
        global_goals['Buy new Piano'].addEvent(global_events['Buy new Piano'], 10)
        
        def learnedToPlayPianoGoalReached(character):
            if character.getAbility('Piano Skill').get() > 800:
                return True
            else:
                return False
        
        global_goals['Learn Piano'] = RenpyperGoal(reached = learnedToPlayPianoGoalReached, name = 'Learn Piano')
        global_goals['Learn Piano'].addEvent(global_events['Play Piano'], 50)
        global_goals['Learn Piano'].addEvent(global_events['Read a Book'], 10)
        global_goals['Learn Piano'].addGoal(global_goals['Buy new Piano'], 20)
        
        testChar = RenpyperCharacter(name = 'Pi')
        
    if testChar.goals_['Learn Piano'].name_ != 'Learn Piano':
        "Setting a goal to a character didn't work correctly."
    $ goalCtr = len(testChar.goals_)
    if goalCtr != 2:
        "Setting goals to a character didn't work correctly."
        
    $ nextEvent = testChar.goals_['Learn Piano'].pursue(strength = 0.9)
    
    $ count = 100
    while count > 0:
        $ nextEvent = testChar.goals_['Learn Piano'].pursue(strength = 0.9)
        if nextEvent == None:
            "I got a None object as the next Event. Baaaaaaaad!"
        $ count -= 1
        
    python:
        global_events.clear()
        global_flags.clear()
        global_abilities.clear()
        global_goals.clear()
        del learnedToPlayPianoGoalReached
        del boughtPianoGoalReached
        del testChar
        del nextEvent
        del goalCtr
    
    return
    