label renpyper_events:
    python:
        class Event(object):
            involvedCharacters_ = []
            
            def __init__(self, listOfCharacters):
                self.involvedCharacters_ = list(listOfCharacters)
                
    return