# import modules
print "spooling up"
import ConfigParser
# read configuration file into the script
print "pulling variables from the configuration file"
# we need some if/or here to determine if the config file is in the proper location
#perhaps "did you move configuration file?" "if so, what's the new path?"

#engage the config parser to pull in our configuration file
Config = ConfigParser.ConfigParser()
Config
Config.read("/opt/duoauthproxy/conf")

#getting verbose here...but list out the sections found
Config.sections()
