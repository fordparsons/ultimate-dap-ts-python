# import modules
print "spooling up"
import ConfigParser
import os
import subprocess
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

# Define a function to test network reachability
def DuoPingTest(ping_host):
    try:
        if subprocess.call(
            ['ping', '-q', '-c', '1', ping_host],
            stdout=open(os.devnull, 'wb')) == 0:
            ping_host_reachable = True
        else:
            ping_host_reachable = False

    except subprocess.CalledProcessError:
        print 'DuoPingTest Failed!'

    return ping_host_reachable


# Define a function to test port openness
def DuoPortTest(host,port):
    try:
        socket_test = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket_test.settimeout(2)
        if socket_test.connect_ex((host,port)) == 0:
            port_open = True
        else:
            port_open = False
    except:
        print 'DuoPortTest Failed!'

    return port_open

# Static variable definitions
localhost = "127.0.0.1"
ldap_port = 443
radius_port = 1812

# AD Test Sequence
if Config.has_section("ad_client") == True:
    print 'ad_client found, testing host reachability'

    # Network Reachability Test
    if DuoPingTest(ConfigSectionMap("ad_client")['host']) == True:
        print 'Active Directory Reachable'
    else:
        print 'Active Directory NOT Reachable'

    # Port Test
    if DuoPortTest(ConfigSectionMap("ad_client")['host'],ldap_port) == True:
        print 'ldap port is open'
    else:
        print 'ldap port is closed'
