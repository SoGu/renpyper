init:
    python:
        def parsePersonalityModel(file_name):
            pass
            
        def parseCharacters(file_name):
            pass
        
        # open the main file
        renpyper_main_file = open(renpy.loader.transfn("renpyper/renpyper_main.xml"), "r")
        
        # import xml related library
        import xml.etree.ElementTree as etree
        
        # parse the main file
        files_tree = etree.parse(renpy.loader.transfn("renpyper/renpyper_main.xml"))
        
        # get the files tree root element
        files_tree_root = files_tree.getroot()
        
        # check if there are exactly two children in the renpyper_main.xml file
        if (len(files_tree_root) != 2):
            b = 1/0 #produce error

        files_tree_list = list(files_tree_root)
        
        # get the lists for personality files and character files
        personality_files_tree = None
        characters_files_tree = None
        
        if (files_tree_list[0].tag == "personality_model"):
            personality_files_tree = files_tree_list[0]
        elif (files_tree_list[0].tag == "characters"):
            characters_files_tree = files_tree_list[0]
        else:
            b = 1/0
            
        if (files_tree_list[1].tag == "personality_model"):
            personality_files_tree = files_tree_list[1]
        elif (files_tree_list[1].tag == "characters"):
            characters_files_tree = files_tree_list[1]
        else:
            b = 1/0
            
        #-----  personality files -----#        
        pers_files = len(personality_files_tree)
        
        for i in range(pers_files):
            parsePersonalityModel(personality_files_tree[i].text)
            
            
        #----- character files -----#
        char_files = len(character_files_tree)
        
        for i in range(char_files):
            parseCharacters(character_files_tree[i].text)