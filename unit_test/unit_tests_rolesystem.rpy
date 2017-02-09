label unit_test_roleSystems:
    
    $ testSys = RenpyperRoleSystem(name = 'Family Obama')
    if testSys.name_ != 'Family Obama':
        "Creating a Role System object didn't work."
    $ del testSys
    

    $ testSys = RenpyperRoleSystem(name = 'Family Obama')
    $ testSys.addRole(name = 'Lord')
    if testSys.role_list_[0].name_ != 'Lord':
        "Adding a Role to a Role System didn't work."
    $ del testSys
    
    
    $ testSys = RenpyperRoleSystem(name = 'Family Obama')
    $ testSys.addRole(name = 'Lady')
    $ testSys.addRole(name = 'Lord')
    $ testChar1 = RenpyperCharacter(name = 'Brian')
    $ testSys.grant(char = testChar1, role = 'Lord')
    if testSys.getRole('Brian') != 'Lord':
        "Granting a Character a role or getting a character's role in a system didn't work."
    if testSys.isRoleFree('Lord') is not False:
        "A role is still considered to be free although a character was assigned to it."
    $ testSys.fire(char = testChar1, role = 'Lord')
    if testSys.isRoleFree('Lord') is not True:
        "A role is still considered to be occupied although the character was fired."
        
    $ testChar2 = RenpyperCharacter(name = 'Ludmilla')
    $ testSys.grant(char = testChar1, role = 'Lord')
    $ testSys.grant(char = testChar2, role = 'Lord')
    if testSys.getRole('Ludmilla') == 'Lord':
        "Granting a character a role although that role was already taken did work."
    
    $ del testChar1
    $ del testChar2
    $ del testSys
    
    return
    