'''THIS FILE IS INTENDED TO BE IMPORTED INTO YOUR MAIN FILE. ALL FILE HANDLING IS INTENDED TO BE DONE FROM THE MAIN FILE DIRECTORY'''


import configparser



config = configparser.ConfigParser()

# Used to read data from the config file


def ReadConfig(section, datatype, file):
    '''This function will read the data from a given config file.
    Usage: ReadConfig(section, datatype, file)
    section (String): The section you want to get data from
    datatype (String): The datatype you wish to retreve
    file (String or Raw String): The location of the file you want to read from'''
    config.read(file)
    # print(section)
    # print(section in config)
    # print(datatype)
    # print(config.sections())
    # print(config[section][datatype])
    return config[section][datatype]

# Used to create the config file
def CreateConfig(file):
    '''This is a default config file generator. Please fill out the config file in the configfile.py file
    Usage: CreateConfig(file)
    file (String or Raw String): The location you want to write your config file to'''
    config['General'] = {'discordbotkey': '',
                         'wikiurl': '',
                         'wikibototken': '',
                         }
    with open(file, 'w') as configfile:
        config.write(configfile)


if __name__ is "__main__":
  print('This file is not designed to run alone.')
