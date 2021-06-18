import configparser,os


#####


"""

    handle the settings off the TODO

    simple !"""

SETTINGS_FILE = './data/SETTINGS.txt'

DEFAULT_FILE_DATA = """"""

class SETTINGS:
    def __init__(self):
        # INTIALIZE THE PARSER
        self.checkfile(SETTINGS_FILE)
        self.parser = configparser.ConfigParser()
        self.parser.read(SETTINGS_FILE)
    def checkfile(self,file):
        # create file if non-existent or deleted
        try:
            with open(file, 'r') as f:
                f.close()
        except:
            with open(file, 'w') as f:
                f.write(DEFAULT_FILE_DATA)
                f.close()
    def default_file(self):
        os.remove(SETTINGS_FILE)
        self.checkfile()
    def current_theme(self):
        return self.parser['CONFIG']['theme']
    def colors(self,widget_name):
        self.parser = configparser.ConfigParser()
        self.parser.read(SETTINGS_FILE)
        theme = self.parser['CONFIG']['theme']
        try:
            return eval(self.parser[theme][widget_name])
        except:
            print("[ALERT] : no color for ",widget_name)
            return((1,0,0,1))
    def read(self, section, var):
        data = self.parser[section][var]
        return data

    def write(self, section,var,  data):

        self.parser[section][var] = data

        with open(SETTINGS_FILE, 'w') as f:
            self.parser.write(f)
print(SETTINGS().current_theme())
