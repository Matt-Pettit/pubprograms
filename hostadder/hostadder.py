#!/usr/bin/python
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

import sys,os,time


def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

def strandler(line,ip):
    currentline = str(line)
    currentline = currentline[len(ip):len(currentline)]
    if 'www.' not in currentline:
        currentline = 'www.'+currentline
    return(currentline)


def infohost():
    helpmessage = ('Use format: hostadder.py "original_file" "add_file" "ip"')
    try:
        hostfile = str(sys.argv[1])

    except:
        sys.exit('There was an error with the format you entered, use the help arguement for the correct format.')
    if hostfile == 'help':
        sys.exit(helpmessage)
    else:
        try:
            host = open(hostfile,'r')
            global writeto
            writeto = open(hostfile,'a')
            return(host)
        except:
            sys.exit('Original file does exist')



def infoip():
    try:
        ip = str(sys.argv[3])
    except:
        print('No IP given, using default(127.0.0.1)')
        ip = '127.0.0.1'
    return(ip)


def infoadd():
    try:
        addfile = str(sys.argv[2])
    except:
        sys.exit('There was an error with the format you entered, use the help arguement for the correct format.')
    try:
        add = open(addfile,'r')
        return(add)
    except:
        sys.exit('Add file does exist')



def builder(hostfile,addfile,ip):
    original = []
    originaldom = []
    new = []
    newdom = []
    newdom1 = []
    new1 = []
    replace1 = []
    replacedom1 = []

    for line in hostfile:
        #print(line)
        spaceloc = line.find(' ')
        lineip = (line[0:spaceloc])
        linedom = (line[spaceloc+1: len(line)])

        original.append(lineip)
        originaldom.append(linedom)
        #print(linedom.split())

    for line2 in addfile:
        spaceloc = line2.find(' ')
        line2ip = (line2[0:spaceloc])
        line2dom = (line2[spaceloc+1: len(line2)])

        new.append(line2ip)
        newdom.append(line2dom)
        #print(line2dom.split())


    for i in range(int(len(new))):
        if new[i] not in original:
            new1.append(new[i])
            newdom1.append(newdom[i])
        elif (new[i] in original) and (newdom[i] not in originaldom):
            replace1.append(new[i])
            replacedom1.append(newdom[i])
    #print('add: ',new1,newdom1)
    #writefunction to add things to list
    #print('replace: ',replace1,replacedom1)

    for i in range(len(hostfile)):
        spaceloc = hostfile[i].find(' ')
        lineip = (hostfile[i][0:spaceloc])
        if lineip in replace1:





    #print(original)
    #print(new)
    #print(newitems)

    #for item in newitems:
        #print(line)
    #return(newitems)

def main():
    start = time.time()
    hostfile =infohost()
    addfile = infoadd()
    ip= infoip()
    newitems = builder(hostfile,addfile,ip)
    end = time.time()
    timeittook = str(round((end - start), 2))
    #print(str(len(newitems))+' Hosts added in '+timeittook+' secs.')


main()
