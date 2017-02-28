label unit_test_characters:
    
    $ testChar = RenpyperCharacter(name = 'Larry')
    
    if len(global_characters) != 1:
        "A character adding itself to the global character list didn't work."
        
    if global_characters['Larry'] is not testChar:
        "A character didn't add itself to the global character list correctly."
        
    $ RenpyperCharacter(name = 'Test')
    
    if len(global_characters) != 2:
        "Deleting a character didn't remove it from the global character list."
        
    $ testChar.__del__()
    $ global_characters['Test'].__del__()
    
    if len(global_characters) != 0:
        "Deleting a character didn't remove it from the global character list."
    
    
    $ global_traits['trust'] = RenpyperTrait()
    
    $ testChar = RenpyperCharacter(name = 'John', col = "#000000")
    if testChar.rc_.name != 'John':
        "Ren'Py character didn't get the name of the constructor that it should have."
    $ del testChar
    
    $ testChar1 = RenpyperCharacter()
    $ testChar2 = RenpyperCharacter()
    $ testChar1.trait('trust').setValue(333)
    if testChar1.trait('trust').get() != 333:
        "Setting a trait of a character to a certain value didn't work."
    $ testChar2.trait('trust').setValue(555)
    if testChar1.trait('trust').get() != 333:
        "Deep copying the global traits dictionary of traits on character generation didn't work."
        
    $ testChar2.setTrait('trust', 123)
    if testChar2.getTrait('trust') != 123:
        "The setTrait shortcut in the character object didn't work."
    $ testChar2.incTrait('trust', 123)
    if testChar2.getTrait('trust') != 246:
        "The incTrait shortcut in the character object didn't work."
        
    $ del testChar1
    $ del testChar2
    
    $ global_traits.clear()
    
    
    $ global_flags['Vampire'] = RenpyperFlag()
    
    $ testChar1 = RenpyperCharacter()
    $ testChar2 = RenpyperCharacter()
    $ testChar1.flag('Vampire').setValue(True)
    if testChar1.flag('Vampire').get() is not True:
        "Setting a flag of a character to a certain value didn't work."
    $ testChar2.flag('Vampire').setValue(False)
    if testChar1.flag('Vampire').get() is not True:
        "Deep copying the global flags dictionary of traits on character generation didn't work."
        
    $ testChar1.setFlag('Vampire')
    if testChar1.getFlag('Vampire') != True:
        "The setFlag shortcut in the character object didn't work."
        
    $ del testChar1
    $ del testChar2
    
    $ global_flags.clear()
    
    $ global_properties['eye color'] = RenpyperProperty('blue')
    
    $ testChar1 = RenpyperCharacter()
    $ testChar2 = RenpyperCharacter()
    $ testChar2.prop('eye color').set('white')
    if testChar1.prop('eye color').get() == 'white':
        "Deep copying a property object didn't work correctly."
    
    $ testChar2.setProp('eye color', 'green')
    if testChar2.getProp('eye color') != 'green':
        "The setProperty shortcut in the character object didn't work."
    
    $ del testChar1
    $ del testChar2
    
    
    $ global_abilities['dancing'] = RenpyperAbility(topName = 'Dance', base = 1.0)
    
    $ testChar1 = RenpyperCharacter()
    $ testChar1.ab('dancing').set(15)
    if testChar1.ab('dancing').get() != 15:
        "Setting a value in an ability didn't work correctly."
    $ testChar1.ab('dancing').setTalent(2.0)
    if testChar1.ab('dancing').getTalent() != 2.0:
        "Setting a talent value in an ability didn't work correctly."
    if testChar1.getTalent('dancing') != 2.0:
        "The getTalent shortcut for character objects didn't work."
    $ testChar1.ab('dancing').learn(10)
    if testChar1.ab('dancing').get() != 45:
        "Learning an ability didn't work correctly."
        
    $ testChar1.setAb('dancing', 8)
    if testChar1.getAb('dancing') != 8:
        "The setAbility shortcut for character objects didn't work."
    
    $ testChar1.setTalent('dancing', 3)

    if testChar1.getTalent('dancing') != 3:
        "The setTalent shortcut in the character class didn't work."
        
    $ testChar1.learn('dancing', 10)
    if testChar1.getAb('dancing') != 48:
        "The learn shortcut it the character object didn't work."

    $ del testChar1
    $ global_abilities.clear()
    
    
    $ global_traits['size'] = RenpyperTrait(bottom = 0, top = 250)
    
    python:
        def testInflFunc(key):
            return (global_characters[key].getTrait('size') - 170) / 5
    
    $ global_abilities['dancing'] = RenpyperAbility(topName = 'Dance', base = 1.0, talent = 0.0, influence = testInflFunc)
    
    $ testChar = RenpyperCharacter(name = 'ABC')
    $ testChar.trait('size').set(180)
    $ testChar.ab('dancing').setKey('ABC')
    
    if testChar.ab('dancing').superCharacterKey_ != 'ABC':
        "Setting the super character key in an ability didn't work."
    
    $ testChar.ab('dancing').set(10)
    
    $ val = testInflFunc('ABC')
    if val != 2:
        "Something went wrong with an influence function."
        "The value was [val]."
    $ del val
    
    if testChar.ab('dancing').influence_ is emptyAbilityInfluenceFunction:
        "Setting the test influence function to a custom function in abilities didn't work."
    
    if testChar.getAb('dancing') != 12:
        "Providing and using an influence function for abilities didn't work correctly."
        $ val = testChar.getAb('dancing')
        "Value was: [val]"
        $ del val
    
    $ global_traits.clear()
    $ del testChar
    $ global_abilities.clear()
    $ del testInflFunc
    
    return
    