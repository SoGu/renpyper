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
#    if testSys.isRoleFree('Lord') is not False:
#        "A role is still considered to be free although a character was assigned to it."
#    $ testSys.fire(char = testChar1, role = 'Lord')
#    if testSys.isRoleFree('Lord') is not True:
#        "A role is still considered to be occupied although the character was fired."
    $ testChar2 = RenpyperCharacter(name = 'Ludmilla')
#    $ testSys.grant(char = testChar1, role = 'Lord')
#    $ testSys.grant(char = testChar2, role = 'Lord')
#    if testSys.getRole('Ludmilla') == 'Lord':
#        "Granting a character a role although that role was already taken did work."
#    if testSys.find('Lord') != 'Brian':
#        "Finding the character having a role in a role system didn't work."
#    $ testSys.grant(char = testChar2, role = 'Lady')
#    if testSys.find('Lady') != 'Ludmilla':
#        "Finding the character having a role in a role system didn't work."
#    $ testSys.fire(char = testChar2, role = 'Lady')
#    if testSys.find('Lady') != '':
#        "Finding a character that does not have a specific role didn't return an empty string."
    $ del testChar1
    $ del testChar2
    $ del testSys
    
#    $ testSys = RenpyperRoleSystem(name = 'St. Patrick School')
#    $ testSys.addRole(name = 'Teacher')
#    $ testSys.addRole(name = 'Student')
#    $ testStudent1 = RenpyperCharacter(name = 'Thomas')
#    $ testStudent2 = RenpyperCharacter(name = 'Lara')
#    $ testStudent3 = RenpyperCharacter(name = 'Paul')
#    $ testTeacher = RenpyperCharacter(name = 'Mr. Filch')
#    $ testSys.grant(char = testStudent1, role = 'Student')
#    $ testSys.grant(char = testTeacher, role = 'Teacher')
#    $ testSys.grant(char = testStudent2, role = 'Student')
#    $ testSys.grant(char = testStudent3, role = 'Student')
#    $ testList = testSys.findAll('Student')
#    if set(testList) != set(['Thomas', 'Paul', 'Lara']):
#        #"The findAll function for Role Systems didn't work correctly."
#        #"[testList[0]], [testList[1]], [testList[2]]."
#    $ del testList
#    $ del testStudent1
#    $ del testStudent2
#    $ del testStudent3
#    $ del testTeacher
#    $ del testSys
    
    return
    