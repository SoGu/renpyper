label unit_test_roles:
    
    $ testRole = RenpyperRole(na = 'Master of Horse', gr = 'Lord', nu = 1)
    if testRole.number_ != 1 or testRole.grantableBy_ != 'Lord' or testRole.name_ != 'Master of Horse':
        "Creating a custom Role object didn't work."
    if testRole.isFree() is not True:
        "Role object didn't know that it is free after creation."
    $ del testRole
    
    $ testRole = RenpyperRole(na = 'Lord', gr = 'a', nu = 1)
    $ testChar = RenpyperCharacter(name = 'Louis')
    $ testRole.grant(testChar)
    if testRole.getChar() is not testChar:
        "Granting a character a role didn't work."
    if testRole.isFree() is not False:
        "A Role object didn't know that it is free."
    $ testRole.fire()
    if testRole.get() is not None:
        "Removing a character from a role didn't work."
    if testRole.isFree() is not True:
        "A Role object didn't know that it isn't free."
    $ del testChar
    $ del testRole
    
    $ testRole1 = RenpyperRole(na = 'Peasent', gr = 'Lord', nu = 2)
    $ testChar1 = RenpyperCharacter(name = 'Lucius')
    $ testChar2 = RenpyperCharacter(name = 'Claudia')
    $ testChar3 = RenpyperCharacter(name = 'Brian')
    $ testRole1.grant(testChar1)
    if testRole1.getChar() is not testChar1:
        "Granting a character a role didn't work."
    if testRole1.isFree() is not True:
        "Granting a character a role didn't work if that role is already occupied, but it should have been leagal to assign that role."
    $ testRole1.grant(testChar2)
    if testRole1.isFree() is not False:
        "isFree function didn't work if there are more than one character assigned and that role is full."
    $ testRole1.grant(testChar3)
    if testRole1.numOfCharacters() > 2:
        "Granting a character a role although that role was full already worked."
    if set(testRole1.getAllCharacters()) == set(['Claudia', 'Brian']):
        "Saving and returning several characters into a role didn't work."
    $ del testChar1
    $ del testChar2
    $ del testChar3
    $ del testRole1
    
    $ testRole = RenpyperRole(na = 'Master of Horse', gr = 'Lord', nu = 1)
    $ testChar = RenpyperCharacter()
    $ testRole.grant(testChar, grantedBy = 'Lady')
    if testRole.numOfCharacters() != 0:
        "Role could be granted by a character that doesn't hold the power to do so."
    $ testRole.grant(testChar, grantedBy = 'Lord')
    if testRole.numOfCharacters() != 1:
        "Role couldn't be granted by a character that should be allowed to do so."
    $ del testRole
    $ del testChar
    
    $ testRole = RenpyperRole(na = 'Teacher', gr = '', nu = 2)
    $ testChar = RenpyperCharacter(name = 'Bert')
    $ testRole.grant(testChar)
    $ testRole.grant(testChar)
    if testRole.numOfCharacters() != 1:
        "Granting a character the same role twice did work."
    $ del testChar
    $ del testRole
    
    return
    