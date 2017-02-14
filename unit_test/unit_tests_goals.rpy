label unit_test_goals:
    
    $ testGoal = RenpyperGoal(reached = lambda x: False, name = 'Sleep', importance = 0)
    if testGoal.name_ != 'Sleep' or testGoal.relativeImportance_ != 0:
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
    
    if testChar1.goal('Sleep').reached(testChar1.getName()) != False:
        "Basic setup of a system using goals didn't work."
    # make Monty awake now:
    $ testChar2.mood('Tiredness').value_ = 50
    if testChar2.goal('Sleep').reached(testChar2.getName()) != True:
        "Determining if a goal was reached didn't work correctly."
        
    
        
    $ del testChar1
    $ del testChar2
    $ del sleepGoalReached
    $ global_goals.clear()
    $ global_moods.clear()
    
    return
    