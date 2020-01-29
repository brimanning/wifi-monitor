import subprocess
import time

oldAddresses = []

while True:
    p = subprocess.Popen("arp-scan -l", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    if output:
        newAddresses = []
        for line in output.splitlines():
            if (line.startswith("192")):
                newAddresses.append(line[line.index(":")-2:line.rindex(":")+3])
        
        for address in newAddresses:
            if address not in oldAddresses:
                print "New device joined: " + address

        for address in oldAddresses:
            if address not in newAddresses:
                print "Device left: " + address

        oldAddresses = newAddresses
    else:
        print "Error: " + err

    time.sleep(5)