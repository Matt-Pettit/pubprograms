# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


import os, webbrowser, pyautogui, time

i = 0

def printer():
    print("""

 ██████╗ ███████╗ ██████╗  ██████╗ ██╗   ██╗███████╗███████╗███████╗██████╗
██╔════╝ ██╔════╝██╔═══██╗██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██╔══██╗
██║  ███╗█████╗  ██║   ██║██║  ███╗██║   ██║█████╗  ███████╗███████╗██████╔╝
██║   ██║██╔══╝  ██║   ██║██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██╔══██╗
╚██████╔╝███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████║███████║██║  ██║
 ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝

██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

By Matt Pettit
Make sure your browser always downloads to the same folder, click enter and go on to the site, it will give you 3 seconds
    """)

def data():
    folder =  str(input("File path for download folder(include last slash): "))
    beg = str(input("Game name(uscities for example): "))
    i = 0
    while True:
        try:
            input('Click enter to start')
            time.sleep(4)
            pyautogui.hotkey('ctrl', 's')
            pyautogui.typewrite(str(beg)+(str(i)))
            pyautogui.press('enter')
            time.sleep(2)
            filename = folder+(str(beg))+(str(i))+'.html'

            print(filename)
            myfile = open(filename, "r")
            data=myfile.readlines()
            data = ''.join(data)


            startstr = str('https://maps.google.com/maps/@')
            endstr = str('source=apiv3" title="Click')

            start =int(data.find(startstr))
            end = int(data.find(endstr))

            out = (data[start: end]+"source=apiv3")
            webbrowser.open(out)
            print(out)

        except:
            print("There was an error, check that you inputed the path correctly without quotation marks.")
        i = i + 1



def main():
    printer()
    data()

main()
