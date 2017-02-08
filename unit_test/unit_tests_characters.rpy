label unit_test_characters:
    
    $ testChar = RenpyperCharacter(name = 'Larry')
    
    if len(global_characters) != 1:
        "A character adding itself to the global character list didn't work."
        
    if global_characters['Larry'] is not testChar:
        "A character didn't add itself to the global character list correctly."
        
    $ testChar2 = RenpyperCharacter(name = 'Test')
    
    if len(global_characters) != 2:
        "Deleting a character didn't remove it from the global character list."
        
    $ testChar.__del__()
    $ testChar2.__del__()
    
    if len(global_characters) != 0:
        "Deleting a character didn't remove it from the global character list."
    
    
    $ global_traits['trust'] = Trait()
    
    $ testChar = RenpyperCharacter(name = 'John', col = "#000000")
    if testChar.rc_.name != 'John':
        "Ren'Py character didn't get the name of the constructor that it should have."
    $ del testChar
    
    $ testChar1 = RenpyperCharacter()
    $ testChar2 = RenpyperCharacter()
    $ testChar1.getTrait('trust').setValue(333)
    if testChar1.getTrait('trust').get() != 333:
        "Setting a trait of a character to a certain value didn't work."
    $ testChar2.getTrait('trust').setValue(555)
    if testChar1.getTrait('trust').get() != 333:
        "Deep copying the global traits dictionary of traits on character generation didn't work."
    $ del testChar1
    $ del testChar2
    
    $ global_traits.clear()
    
    
    $ global_flags['Vampire'] = Renpyper_Flag()
    
    $ testChar1 = RenpyperCharacter()
    $ testChar2 = RenpyperCharacter()
    $ testChar1.getFlag('Vampire').setValue(True)
    if testChar1.getFlag('Vampire').get() is not True:
        "Setting a flag of a character to a certain value didn't work."
    $ testChar2.getFlag('Vampire').setValue(False)
    if testChar1.getFlag('Vampire').get() is not True:
        "Deep copying the global flags dictionary of traits on character generation didn't work."
    $ del testChar1
    $ del testChar2
    
    $ global_flags.clear()
    
    $ global_properties['eye color'] = RenpyperProperty('blue')
    
    $ testChar1 = RenpyperCharacter()
    $ testChar2 = RenpyperCharacter()
    $ testChar2.getProp('eye color').set('white')
    if testChar1.getProp('eye color').get() == 'white':
        "Deep copying a property object didn't work correctly."
    $ del testChar1
    $ del testChar2
    
    
    $ global_abilities['dancing'] = RenpyperAbility(topName = 'Dance', base = 1.0)
    
    $ testChar1 = RenpyperCharacter()
    $ testChar1.getAb('dancing').set(15)
    if testChar1.getAb('dancing').get() != 15:
        "Setting a value in an ability didn't work correctly."
    $ testChar1.getAb('dancing').setTalent(2.0)
    if testChar1.getAb('dancing').getTalent() != 2.0:
        "Setting a talent value in an ability didn't work correctly."
    $ testChar1.getAb('dancing').learn(10)
    if testChar1.getAb('dancing').get() != 45:
        "Learning an ability didn't work correctly."
    $ del testChar1
    $ global_abilities.clear()
    
    
    $ global_traits['size'] = Trait(bottom = 0, top = 250)
    
    python:
        def testInflFunc(key):
            return (global_characters[key].getTrait('size').get() - 170) / 5
    
    $ global_abilities['dancing'] = RenpyperAbility(topName = 'Dance', base = 1.0, talent = 0.0, influence = testInflFunc)
    
    $ testChar = RenpyperCharacter(name = 'ABC')
    $ testChar.getTrait('size').set(180)
    $ testChar.getAb('dancing').setKey('ABC')
    
    $ testChar.getAb('dancing').set(10)
    if testChar.getAb('dancing').get() == 12:
        "Providing and using an influence function for abilities didn't work correctly."
    
    $ global_traits.clear()
    $ del testChar
    $ global_abilities.clear()
    $ del testInflFunc
    
    return
    