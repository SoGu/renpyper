label renpyper_roleSystems:
    
    call renpyper_role
    
    $ global_role_systems = {}
    
    python:
        class RenpyperRoleSystem(object):
            name_ = ''
            
            role_list_ = []
            
            def addRole(self, name, grantableBy = '', number = 1):
                role = RenpyperRole(gr = grantableBy, nu = number, na = name)
                self.role_list_.append(role)
                
            def __init__(self, name = ''):
                self.name_ = name
                
            def grant(self, char, role):
                # if self.isRoleFree(role):
                for i in self.role_list_:
                    if i.getName() == role:
                        i.grant(char)
                        break
                #else:
                #    return
                            
            def fire(self, role, char = None):
                for i in self.role_list_:
                    if i.getName() == role:
                        if i.getChar() is None:
                            pass
                        elif i.getChar() is char:
                            i.fire()
                            break
                
            ## Finds one (undefined) character in the role with the given name.
            ## Should only be used if the author is sure there is only one such role.
            def getRole(self, name):
                for i in self.role_list_:
                    if i.getChar() is not None:
                        if i.getChar().name_ == name:
                            return i.getName()
                return ''
                
            ## Finds all roles that the given character has.
            def getAllRoles(self, name):
                pass
                
            ## Finds one (undefined) CHARACTER with the given name and returns the ROLE it is in.
            ## Should only be used if the author is sure the character has only that one role.
            def find(self, name):
                for i in self.role_list_:
                    if i.name_ == name:
                        if i.getChar() is not None:
                            return i.getChar().name_
                return ''
                
            ## Finds all CHARACTERS with the given role and returns their name as part of a list.
            def findAll(self, role):
                listOfChar = []
                for i in self.role_list_:
                    if i.name_ == role and i.getChar() is not None:
                        listOfChar.append(i.getChar().name_)
                return listOfChar
                    
                
            ## Returns true if there is at least one role slot with the given name that is not blocked by a character.
            ## Returns false otherwise.
            def isRoleFree(self, role):
                free = True
                for i in self.role_list_:
                    if i.getName() == role:
                        if i.isFree() is False:
                            free = False
                return free
    
    return
    