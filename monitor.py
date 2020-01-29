import subprocess
import time

def getConnectedDevices():
    p = subprocess.Popen("arp-scan -l", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    addresses = []
    if output:
        for line in output.splitlines():
            if (line.startswith("192")):
                addresses.append(line[line.index(":")-2:line.rindex(":")+3])
    else:
        print "Error: " + err
    return addresses

oldAddresses = getConnectedDevices()

while True:
    newAddresses = getConnectedDevices()
        
    for address in newAddresses:
        if address not in oldAddresses:
            print "Device joined: " + address

    for address in oldAddresses:
        if address not in newAddresses:
            print "Device left  : " + address

    oldAddresses = newAddresses

    time.sleep(5)