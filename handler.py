import re

def handle_arp(file = 'C:\\Users\\yangh\\Desktop\\py\\showHost\\conf\\arp.txt'):
    L = []
    with open(file, 'r') as f:
        for line in f.readlines():
            ipre = re.search("(\d+\.){3}\d+", line)
            macre = re.search("([0-9a-zA-Z]{4}\.){2}[0-9a-zA-Z]{4}", line)
            if not macre:
                print('[info]ip address: '+ipre.group()+' has Incomplete mac address')
                continue
            else:
                d = {'ip':ipre.group(),'mac':macre.group()}
                L.append(d)
    return L

def handle_port(L, file = 'C:\\Users\\yangh\\Desktop\\py\\showHost\\conf\\mac.txt'):
    for row in L:
        with open(file, 'r') as f:
            for line in f.readlines():
                macre = re.search("([0-9a-zA-Z]{4}\.){2}[0-9a-zA-Z]{4}", line)
                portre = re.search("[PGFTRS].+[a-z0-9]$", line)
                if row['mac'] == macre.group():
                    if portre:
                        print('ip address: '+row['ip']+' mac address: '+row['mac']+' port: '+portre.group())
                    else:
                        print('[info]ip address: '+row['ip']+' mac address: '+row['mac']+' has no port!')


arplist = handle_arp()
handle_port(arplist)