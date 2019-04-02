#!/usr/bin/python
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

import sys, os, getopt, traceback, datetime
import requests
try:
    import xml.parsers.expat
except:
    print "No xml expat library - fatal error"
    sys.exit(1)

sections = (u"title",u"link",u"description")
in_section, section = "", ""

def exception():
    exc_string = ""
    try:
        typ, value, tb = sys.exc_info()
        info = traceback.extract_tb(tb)
        filename, lineno, function, text = info[-1] # last line only
        exc_string = "%s:%d: %s: %s (in %s)" % (filename, lineno, typ.__name__, str(value), function)
    finally:
        typ = value = tb = None # clean up
    return exc_string


def start_element(name, attrs):
    global section, in_section, sections
    if name in sections:
        in_section = name

def end_element(name):
    global section, in_section, sections
    if name in sections:
        section = section.split("<p>",1)[0].strip()
        print section
        if in_section == u"title":
            print "="*len(section)
        section = u""
        in_section = ""
        print

def char_data(data):    # not using this for now ...
    global section, in_section, sections
    if not data: return
    if not in_section: return
    section = section + data


def main():

    # get the data
    url = 'https://www.tecmint.com/feed/'
    headers = {'accept': 'application/xml;q=0.9, */*;q=0.8'}
    response = requests.get(url, headers=headers)
    xmldata = response.text
    p = xml.parsers.expat.ParserCreate()
    p.StartElementHandler = start_element
    p.EndElementHandler = end_element
    p.CharacterDataHandler = char_data
    px = p.Parse(xmldata) 


if __name__ == "__main__":
    main()

