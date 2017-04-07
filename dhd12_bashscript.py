# import modules
print "spooling up"
import ConfigParser
# read configuration file into the script
print "pulling variables from the configuration file"
# we need some if/or here to determine if the config file is in the proper location
#perhaps "did you move configuration file?" "if so, what's the new path?"

#engage the config parser to pull in our configuration file
#need to adjust path to config file to default
Config = ConfigParser.ConfigParser()
Config.read("authproxy.cfg")

#getting verbose here...but list out the sections found
#print Config.sections()

#pull in individual config parameters
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

print ConfigSectionMap("ad_client")['host']
