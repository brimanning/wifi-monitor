import subprocess
import time

def get_connected_devices():
    p = subprocess.Popen("arp-scan -l", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    addresses = []
    if output:
        for line in output.splitlines():
            if (line.startswith("192")):
                addresses.append(line[line.index(":")-2:line.rindex(":")+3])
    else:
        print("Error: " + err)
    return addresses

old_addresses = get_connected_devices()

while True:
    new_addresses = get_connected_devices()
        
    for address in new_addresses:
        if address not in old_addresses:
            print("Device joined: " + address)

    for address in old_addresses:
        if address not in new_addresses:
            print("Device left  : " + address)

    old_addresses = new_addresses

    time.sleep(5)