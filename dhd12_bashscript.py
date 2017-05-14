# import modules
print "spooling up"
import ConfigParser
import os
import socket

# read configuration file into the script
print "pulling variables from authproxy.cfg"
# we need some if/or here to determine if the config file is in the proper location
# perhaps "did you move configuration file?" "if so, what's the new path?"

#engage the config parser to pull in our configuration file
#need to adjust path to config file to default
Config = ConfigParser.ConfigParser()
Config.read("authproxy.cfg")

# Define some functions for tests

# Define a function to pull in configuration attributes
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

# Define a function to test AD host connectivity
def DuoAcDirTest(ad_host):
    try:
        ad_ping_response = os.system("ping -c 1 " + ad_host)
        if ad_ping_response == 0:
            ad_reachable = True
        else:
            ad_reachable = False
    except:
        print 'DuoAcDirTest Failed!'
    return ad_reachable

# define host locations
# This section needs to be logic'd to only search attributes included
# Perhaps we need to create a list of included variables for later tests' logic
localhost = "127.0.0.1"
if Config.has_section("ad_client") == True:
    if DuoAcDirTest(ConfigSectionMap("ad_client")['host']) == True:
        print 'Active Directory Reachable'
    else:
        print 'Active Directory NOT Reachable'



#time to test a port
#ldap_port = 443

#print "are we listening for 1812?"
#socket_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket_test.settimeout(2)                                      #2 Second Timeout
#result = socket_test.connect_ex((ad_host,ldap_port))
#if result == 0:
#  print 'port OPEN'
#else:
 # print 'port CLOSED, connect_ex returned: '+str(result)

  #testing the features of github desktop
  #further testing y'all
