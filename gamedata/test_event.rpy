label renpyper_testEvent(char1=None, char2=None):
    python:
        testEvent = Event([char1, char2])
        
    "I'm in the test event now"
    
    $ c1 = char1.rc_
    $ c2 = char2.rc_
    
    c1 "Character one now says something."
    
    c2 "And now character two is saying something else."
    
    $ currentTrust = char1.traits_['trust'].get()
    
    c1 "My current trust is [currentTrust]."
    
    $ char1.traits_['trust'].inc(10)
    $ currentTrust = char1.traits_['trust'].getValue()
    
    c1 "My current trust is [currentTrust]."
    
    return