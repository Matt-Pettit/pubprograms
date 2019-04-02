#!/usr/bin/python
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#https://stackoverflow.com/questions/19842752/finding-a-string-multiple-times-in-another-string-python
# thanks to user: vitiral for multifind code
import sys,os
import requests



def multifind(string, value, start = 0, stop = None):
    values = []
    while True:
        found = string.find(value, start, stop)
        if found == -1:
            break
        values.append(found)
        start = found + 1
    return values


def valfinder(string,xmldata):
    return(multifind(xmldata, string))

def printer(titles,descs,links):
    for i in range(len(links)):
            print(titles[i])
            print('='*len(titles[i])+'\n')
            print(descs[i]+'\n')
            print(links[i]+'\n')

def finder(xmldata, string1,string2):
    list1 = []
    wordbegvalstr = string1
    wordendvalstr = string2
    wordbegval = valfinder(wordbegvalstr,xmldata)
    wordendval = valfinder(wordendvalstr,xmldata)
    for i in range(len(wordbegval)):
            mainstring = (xmldata[wordbegval[i]+(len(wordbegvalstr)):wordendval[i]])

            if string1 == '<title>':
                    list1.append(mainstring+':')
            else:
                    list1.append(mainstring)
    if string1 == '<description>':
            descsfinal= []
            list1.remove(list1[0])
            for word in list1:
            #currentdesc = descs[i]
                    loc = (word.find('&lt;p&gt;&lt;div'))
                    currentdesc = word[0:loc]
                    descsfinal.append(currentdesc)
            return(descsfinal)
    else:
            list1.remove(list1[0])
            list1.remove(list1[0])
            list1.remove(list1[len(list1)-1])
            return(list1)



def slashdotMain():
    url = 'https://www.tecmint.com/feed/'
    headers = {'accept': 'application/xml;q=0.9, */*;q=0.8'}
    response = requests.get(url, headers=headers)
    xmldata = response.text
    titles = finder(xmldata,'<title>','</title>')
    links = finder(xmldata,'<link>','</link>')
    descs = finder(xmldata, '<description>', '</description>')
    finalprint = []
    #print(titles)
    #print(links)
    #print(descs)
    for i in range(len(titles)):
            finalprint.append(titles[i])
            finalprint.append(descs[i])
            finalprint.append(links[i])
    return(finalprint)



if __name__ == "__main__":
    print(slashdotMain())
