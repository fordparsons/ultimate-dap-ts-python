# import modules
print "spooling up"
import ConfigParser
import os
import socket
from contextlib import closing
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

#define host locations
localhost = "127.0.0.1"
ad_host = ConfigSectionMap("ad_client")['host']
radius_host = ConfigSectionMap("radius_server_auto")['radius_ip_1']

#test network connectivity to ad host
ad_ping_response = os.system("ping -c 1 " + ad_host)

#and then check the response...
if ad_ping_response == 0:
  print "Active Directory is Reachable!"
else:
  print "Where's that Active Directory?"

#time to test a port
ldap_port = 443

print "are we listening for 1812?"
socket_test = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_test.settimeout(2)                                      #2 Second Timeout
result = socket_test.connect_ex((ad_host,ldap_port))
if result == 0:
  print 'port OPEN'
else:
  print 'port CLOSED, connect_ex returned: '+str(result)
