label unit_test_characters:
    
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
    
    return