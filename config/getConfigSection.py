'''
Created on Jan 4, 2015

@author: nb
'''
def getConfigSection(config,section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section,option)
            if dict1[option] == -1:
                print "no value for ",option
        except:
            print "Error occured while reading ",option
            dict1[option] = None
    return dict1