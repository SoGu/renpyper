label unit_test_roles:
    
    $ testRole = RenpyperRole(na = 'Master of Horse', gr = 'Lord', nu = 1)
    if testRole.number_ != 1 or testRole.grantableBy_ != 'Lord' or testRole.name_ != 'Master of Horse':
        "Creating a custom Role object didn't work."
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
    
    return
    