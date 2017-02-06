label unit_test_properties:
    
    $ testProp = RenpyperProperty()
    if testProp.get() != '':
        "Creating a Property object didn't work."
        
    $ testProp.setValue('blue')
    if testProp.get() != 'blue':
        "Setting a property value didn't work."
    $ del testProp
    
    $ testProp = RenpyperProperty('huge')
    if testProp.get() != 'huge':
        "Creating a property object with a value didn't work."
    $ del testProp
    
    return
    