import re
from sql import *

def handle_arp( DB, SWITCHER, file = 'C:\\Users\\yangh\\Desktop\\py\\showHost\\conf\\arp.txt'):
    L = []
    with open(file, 'r') as f:
        for line in f.readlines():
            ipre = re.search("(\d+\.){3}\d+", line)
            macre = re.search("([0-9a-zA-Z]{4}\.){2}[0-9a-zA-Z]{4}", line)
            if not macre:
                print('[info]ip address: '+ipre.group()+' has Incomplete mac address')
                DB._insert(ipre.group(),'','',SWITCHER,'mac Incomplete')
                continue
            else:
                d = {'ip':ipre.group(),'mac':macre.group()}
                L.append(d)
    return L

def handle_port(L, DB ,SWITCHER, file = 'C:\\Users\\yangh\\Desktop\\py\\showHost\\conf\\mac.txt'):
    for row in L:
        with open(file, 'r') as f:
            for line in f.readlines():
                macre = re.search("([0-9a-zA-Z]{4}\.){2}[0-9a-zA-Z]{4}", line)
                portre = re.search("[PGFTECRS].+[a-z0-9]$", line)
                if row['mac'] == macre.group():
                    if portre and portre.group() != 'Router':
                        print('ip address: '+row['ip']+' mac address: '+row['mac']+' port: '+portre.group())
                        DB._insert(row['ip'],row['mac'],portre.group(),SWITCHER,'')
                        continue
                    if not portre:
                        print('[info]ip address: '+row['ip']+' mac address: '+row['mac']+' no entries in mac table')
                        DB._insert(row['ip'],row['mac'],'',SWITCHER,'no entries in mac table')
                        continue
                    else:
                        continue
def check(ip, mac):
    #res = select ip mac
    if res:
        return True
    else:
        return False

if __name__ == '__main__':
    DB = sql()
    arplist = handle_arp(DB,1)
    handle_port(arplist,DB,1)
    DB._commit()
