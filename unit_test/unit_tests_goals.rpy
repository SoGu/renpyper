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
    
    return
    