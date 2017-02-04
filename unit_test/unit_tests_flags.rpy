label unit_test_flags:
    
    $ testFlag = Renpyper_Flag()
    if testFlag.get() is not None:
        "Making a flag object didn't work."
    $ testFlag.set(True)
    if testFlag.getValue() is not True:
        "Setting a flag to true didn't work."
    $ testFlag.set(False)
    if testFlag.get() is not False:
        "Setting a flag to false didn't work."
    $ del testFlag
    
    $ testFlag = Renpyper_Flag(name = 'Is a vampire')
    if testFlag.getName() != 'Is a vampire':
        "Creating a flag object with a name didn't work."
    $ del testFlag
    
    $ testFlag = Renpyper_Flag(name = 'Vampire')
    $ testFlag.set(True)
    $ copiedFlag = copy.deepcopy(testFlag)
    $ testFlag.set(False)
    if copiedFlag.get() is False:
        "Deepcopy didn't copy correctly, the cloned flag object is still bound to the original somehow."
    $ del testFlag
    $ del copiedFlag
    
    return