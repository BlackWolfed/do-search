#!/usr/bin/env python3
# coding: utf-8
# Developed by : Mostafa Tamam (@blackwolf)
import string
import sys

# Check if we are running this on windows platform
is_windows = sys.platform.startswith('win')
# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'  # white
    try:
        import win_unicode_console, colorama

        win_unicode_console.enable()
        colorama.init()
        # Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'  # white


def no_color():
    global G, Y, B, R, W
    G = Y = B = R = W = ''


def banner():
    print("""%s
    
        d8888b.  .d88b.         .d8888. d88888b  .d8b.  d8888b.  .o88b. db   db 
        88  `8D .8P  Y8.        88'  YP 88'     d8' `8b 88  `8D d8P  Y8 88   88 
        88   88 88    88        `8bo.   88ooooo 88ooo88 88oobY' 8P      88ooo88 
        88   88 88    88 C8888D   `Y8b. 88~~~~~ 88~~~88 88`8b   8b      88~~~88 
        88  .8D `8b  d8'        db   8D 88.     88   88 88 `88. Y8b  d8 88   88 
        Y8888D'  `Y88P'         `8888Y' Y88888P YP   YP 88   YD  `Y88P' YP   YP %s%s
                        # Coded by : Mostafa Tamam (@blackwolf)
    """ % (R, W, Y))


banner()
print("Search for anything any time :)")
i = input("[*] What do you search : ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Google search Dorks
print("%s[+] Google search footprints " % G)
print("intext:'{}' OR intext:'{}' OR intext:'{}' OR intext:'{}'".format(i, i, i, i))
print("(ext:doc OR ext:docx OR ext:odt OR ext:pdf OR ext:rtf) intext'{}' OR intext:'{}'".format(i, i))
print("(ext:sxw OR ext:psw OR ext:ppt OR ext:pptx) intext'{}' OR intext:'{}'".format(i, i))
print("(ext:pps OR ext:csv OR ext:txt OR ext:xls) intext'{}' OR intext:'{}' ".format(i, i))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Social networks footprints
print("%s[+] Social networks footprints " % W)
print("site:facebook.com intext:'{}' OR intext:'{}' OR intext:'{}'".format(i, i, i))
print("site:twitter.com intext:'{}' OR intext:'{}' OR intext:'{}'".format(i, i, i))
print("site:linkedin.com intext:'{}' OR intext:'{}' OR intext:'{}'".format(i, i, i))
print("site:instagram.com intext:'{}' OR intext:'{}' OR intext:'{}'".format(i, i, i))
print("site:vk.com intext:'{}' OR intext:'{}' OR intext:'{}'".format(i, i, i))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Individual footprints
print("%s[+] Individual footprints" % B)
print("site:numinfo.net intext:'{}' OR intext:'{}' OR intext:'{}'".format(i, i, i))
print("site:sync.me intext:'{}' OR intext:'{}' OR intext:'{}'".format(i, i, i))
print("whocallsyou.de intext:'{}'".format(i))
print("site:pastebin.com intext:'{}' OR intext:'{}' OR intext:'{}'")
print("site:whycall.me intext:'{}' OR intext:'{}' OR intext:'{}'")
print("site:locatefamily.com intext:'{}' OR intext:'{}' OR intext:'{}'")
print("site:spytox.com intext:'{}'")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# Reputation footprints
print("%s[+] Reputation footprints" % Y)
print("site:uk.popularphotolook.com inurl:'{}'".format(i))
print("site:quinumero.info intext:'{}' OR intext:'{}'".format(i, i))
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
