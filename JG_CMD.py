# coding: utf8
import os
import time
import urllib as url, urllib2
import platform as platf
import requests as rq
from itertools import product
import sys
import getopt
import argparse
from colorama import init
init ( strip=not sys.stdout.isatty () )  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
import zipfile
from random import randint





def startupmsg():
    print("JG CMD [Version 2.0] \n(2018-2019) JG Corporation.")


def jg(com):
    os.system(com)








def JGCMD():

            input1 = raw_input("JG_CMD >")

            #start der funktionen

            if input1 == "info":
                                a = platf.system()
                                b = platf.release()


                                print("Operating System: " + str(a) + "")
                                print("         Release: " + str(b) + "")
                                print("      Process-ID: " + str(os.getpid())+"\n\n")






            elif input1 == "help":
                x = "WEBVIEW          Zeigt den Quellcode jeder beliebiger Webseite an.\nINFO             Shows some intressting infos\nhack             Hidden part of this program\nascii-art        Have fun with some ascii art\nwordlist         Sehr einfach wordlisten erstellen.\ngoogle-hacking   Make google very helpful and much more easier for you\nadmin-finder     Finds admin panel on website\ncrazy            A rainbow color window *o*"

                print("---NEW OPTIONS---")
                print(str ( x )+ "\n")
                time.sleep(0.2)


            elif input1 == "webview":
                            input2 = raw_input("Website: ")
                            try:
                                r = rq.get(input2)
                                print(r.text)
                            except:
                                print("Website not found !\nMaybe you forgot to write http:// or https:// ?!")



            elif input1 == "._.":
                a = 0
                b = 20
                try:
                   os.system ( "START a.mp3" )
                except:
                   pass
                while a < b:
                      print"!!!YOU FOUND AN EASTEREGG!!!"
                      a += 1


            elif input1 == "hack":
                 print("---------PASSWORD---------\n")
                 input3 = raw_input("Password: ")
                 if input3 == "TopSecretPasswort":
                               print("Success!\n\n")
                               print("Which package do you want to download?\n\n(1)Pentest-Tools\n(2)Anonymous-Browsing-Pack\n")
                               input4 = raw_input("JGCMD|Hidden|Download=> ")
                               if input4 == "1":
                                   print "Dont stop the program while working..."
                                   time.sleep( 2 )
                                   os.system("mkdir Pentest-Tools")
                                   start = os.getcwd ()
                                   print(start + "\Pentest-Tools\johntheripper.zip")
                                   path = start + "\Pentest-Tools\johntheripper.zip"

                                   url.urlretrieve ( "http://www.openwall.com/john/h/john179w2.zip", path )

                                   try:
                                       print(start + "\Pentest-Tools\metasploitframework-latest.msi")
                                       path = start + "\Pentest-Tools\metasploitframework-latest.msi"

                                       url.urlretrieve ("https://windows.metasploit.com/metasploitframework-latest.msi", path)
                                   except:
                                       pass

                                   try:
                                       print(start + "\Pentest-Tools\VegaSetup64.exe")
                                       path = start + "\Pentest-Tools\VegaSetup64.exe"

                                       url.urlretrieve ( "https://dist.subgraph.com/downloads/VegaSetup64.exe", path )
                                   except:
                                       pass

                                   try:
                                       print(start + "\Pentest-Tools\Wireshark-win64-2.4.4.exe")
                                       path = start + "\Pentest-Tools\Wireshark-win64-2.4.4.exe"

                                       url.urlretrieve("https://1.eu.dl.wireshark.org/win64/Wireshark-win64-2.4.4.exe", path)
                                   except:
                                       pass

                                   try:
                                       print(start + "\Pentest-Tools\THC-Hydra.zip")
                                       path = start + "\Pentest-Tools\THC-Hydra.zip"

                                       url.urlretrieve ( "https://github.com/Xyl2k/Hydra-GUI/archive/master.zip", path )
                                   except:
                                       pass

                                   try:
                                       print(start + "\Pentest-Tools\\aircrack-ng-1.2-rc4-win.zip")
                                       path = start + "\Pentest-Tools\\aircrack-ng-1.2-rc4-win.zip"

                                       url.urlretrieve ( "https://download.aircrack-ng.org/aircrack-ng-1.2-rc4-win.zip", path )
                                   except:
                                       pass

                                   try:
                                       print(start + "\Pentest-Tools\\beef-0.4.6.1.zip")
                                       path = start + "\Pentest-Tools\\beef-0.4.6.1.zip"
                                       url.urlretrieve ( "https://github.com/beefproject/beef/archive/beef-0.4.6.1.zip",path )
                                   except:
                                       pass

                                   try:
                                       print(start + "\Pentest-Tools\\burp-suite-community-edition.exe")
                                       path = start + "\Pentest-Tools\\burp-suite-community-edition.exe"

                                       url.urlretrieve ("https://portswigger.net/burp/releases/download?product=community&version=1.7.30&type=windowsx64", path )
                                   except:
                                       pass

                                   print("---FINISHED---")

                               elif input4 == "2":
                                   print "Dont stop the program while working..."
                                   time.sleep(2)
                                   os.system ("mkdir Anonymous-Browsing-Pack")
                                   start = os.getcwd()
                                   print(start + "\Anonymous-Browsing-Pack\\torbrowser-install-7.5_en-US.exe")
                                   path = start + "\Anonymous-Browsing-Pack\\torbrowser-install-7.5_en-US.exe"

                                   url.urlretrieve ( "https://www.torproject.org/dist/torbrowser/7.5/torbrowser-install-7.5_en-US.exe", path )

                                   try:
                                       print(start + "\Anonymous-Browsing-Pack\\torchat-windows-0.9.9.553.zip")
                                       path = start + "\Anonymous-Browsing-Pack\\torchat-windows-0.9.9.553.zip"

                                       url.urlretrieve (
                                           "https://github.com/downloads/prof7bit/TorChat/torchat-windows-0.9.9.553.zip", path )
                                   except:
                                       pass

                                   try:
                                       print(start + "\Anonymous-Browsing-Pack\opera-setup.exe")
                                       path = start + "\Anonymous-Browsing-Pack\opera-setup.exe"

                                       url.urlretrieve ("https://www.opera.com/computer/thanks?ni=stable&os=windows", path )
                                   except:
                                       pass

                                   try:
                                       print(start + "\Anonymous-Browsing-Pack\macchanger.zip")
                                       path = start + "\Anonymous-Browsing-Pack\macchanger.zip"

                                       url.urlretrieve ("http://dl.cdn.chip.de/downloads/12960879/SMAC-MAC.zip?cid=54500055&platform=chip&1517075053-1517082553-74ff89-B-739943b61a06ce1412cf0f72bb951fb4", path )
                                   except:
                                       pass

                 else:
                     print("Wrong Password!!!!")


            elif input1 == "cool":
                  print "Jap das was du nicht bist...loser"


            elif input1 == "ascii-art":
                list = ["3-d","3x5","5lineoblique","acrobatic","alligator","alligator2","alphabet","avatar","banner","banner3-D","banner3","banner4","barbwire","basic","bell","big","bigchief","binary","block","bubble","bulbhead","calgphy2","caligraphy","catwalk","chunky","coinstak","colossal","computer","contessa","contrast","cosmic","cosmike","cricket","cyberlarge","cybermedium","cybersmall","diamond","digital","doh","doom","dotmatrix","drpepper","eftichess","eftifont","eftipiti","eftirobot","eftitalic","eftitalic","eftiwall","eftiwater","epic","fourtops","fuzzy","goofy","gothic","graffiti","hollywood","invita","isometric1","isometric2","isometric3","isometric4","italic","ivrit","jazmine","jerusalem","katakana","kban","larry3d","lcd","lean","letters","linux","lockergnome","madrid","marquee","maxfour","mike","mini","mirror","mnemonic","morse","moscow","nancyj-fancy","nancyj-underlined","nancyj","nipples","ntgreek","o8","ogre","pawp","peaks","pebbles","pepper","poison","puffy","pyramid","rectangles","relief","relief2","rev","roman","rot13","rounded","rowancap","rozzo","runic","runyc","sblood","script","serifcap","shadow","short","slant","slide","slscript","small","smisome1","smkeyboard","smscript","smshadow","smslant","smtengwar","speed","stampatello","standard","starwars","stellar","stop","straight","tanja","tengwar","term","thin","threepoint","ticks","ticksslan","tinker-toy","tombstone","trek","tsalagi","twopoint","univers","usaflag","weird"]
                print "Type in your text:"
                text_input = raw_input("==> ")
                print "\nFont:"

                print "Fonts:\n3-d\n3x5\n5lineoblique\nacrobatic\nalligator\nalligator2\nalphabet\navatar\nbanner\nbanner3-D\nbanner3\nbanner4\nbarbwire\nbasic\nbell\nbig\nbigchief\nbinary\nblock\nbubble\nbulbhead\ncalgphy2\ncaligraphy\ncatwalk\nchunky\ncoinstak\ncolossal\ncomputer\ncontessa\ncontrast\ncosmic\ncosmike\ncricket\ncyberlarge\ncybermedium\ncybersmall\ndiamond\ndigital\ndoh\ndoom\ndotmatrix\ndrpepper\neftichess\neftifont\neftipiti\neftirobot\neftitalic\neftitalic\neftiwall\neftiwater\nepic\nfourtops\nfuzzy\ngoofy\ngothic\ngraffiti\nhollywood\ninvita\nisometric1\nisometric2\nisometric3\nisometric4\nitalic\nivrit\njazmine\njerusalem\nkatakana\nkban\nlarry3d\nlcd\nlean\nletters\nlinux\nlockergnome\nmadrid\nmarquee\nmaxfour\nmike\nmini\nmirror\nmnemonic\nmorse\nmoscow\nnancyj-fancy\nnancyj-underlined\nnancyj\nnipples\nntgreek\no8\nogre\npawp\npeaks\npebbles\npepper\npoison\npuffy\npyramid\nrectangles\nrelief\nrelief2\nrev\nroman\nrot13\nrounded\nrowancap\nrozzo\nrunic\nrunyc\nsblood\nscript\nserifcap\nshadow\nshort\nslant\nslide\nslscript\nsmall\nsmisome1\nsmkeyboard\nsmscript\nsmshadow\nsmslant\nsmtengwar\nspeed\nstampatello\nstandard\nstarwars\nstellar\nstop\nstraight\ntanja\ntengwar\nterm\nthin\nthreepoint\nticks\nticksslan\ntinker-toy\ntombstone\ntrek\ntsalagi\ntwopoint\nunivers\nusaflag\nweird\n"

                wert =input("==>")
                print "\nFont color:\n1)red\n2)blue\n3)green\n4) yellow\n5) grey\n"
                color = ["red","blue","green","yellow","grey"]
                font_color_input = int(input("==> "))
                font_color_input -= 1

                print "\nBackground color color:\n1)red\n2)blue\n3)green\n4) yellow\n5) grey\n6) no_background_color"
                color_bg = ["on_red", "on_blue", "on_green", "on_yellow", "on_grey"]
                bg_color_input = int ( input ( "==> " ) )
                bg_color_input -= 1
                if font_color_input != 6:
                         cprint ( figlet_format (text_input, font= list[wert]),color[font_color_input], color_bg[bg_color_input], attrs=['bold'] )
                else:
                    cprint ( figlet_format ( text_input, font=list[wert] ), color[font_color_input],attrs=['bold'] )


            elif input1 == "wordlist":


                    a = '0123456789'

                    b = "abcdefghijklmnopqrstuvwxyz"

                    c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

                    d = "!$%&/()=?`*#~+-"

                    e = "0123456789abcdefghijklmnopqrstuvwxyz"

                    f = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

                    g = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

                    h = "0123456789!$%&/()=?`*#~+-"

                    i = "abcdefghijklmnopqrstuvwxyz!$%&/()=?`*#~+-"

                    j = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&/()=?`*#~+-"

                    k = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&/()=?`*#~+-"


                    print("1)"+str(a))
                    print("2)"+str(b))
                    print("3)"+str(c))
                    print("4)"+str(d))
                    print("5)"+str(e))
                    print("6)"+str(f))
                    print("7)"+str(g))
                    print("8)"+str(h))
                    print("9)"+str(i))
                    print("10)"+str(j))
                    print("11)" + str ( k ))

                    choosebrute = raw_input ( "==> " )

                    if choosebrute == "1":
                      print "Safe on .txt documtent?"
                      print"(y)es               (n)o"
                      file_input = raw_input("==> ")
                      if file_input == "y":
                          file = open ("wordlist.txt", "w")
                          length_input = int ( raw_input ( "Length: " ) )
                          length_input += 1
                          for length in range ( 1, length_input ):
                              to_attempt = product ( a, repeat=length )
                              for attempt in to_attempt:
                                  print(''.join ( attempt ))
                                  file.write(''.join ( attempt )+"\n")

                      else:
                          length_input = int(raw_input("Length: "))
                          length_input += 1
                          for length in range ( 1, length_input):
                              to_attempt = product( a, repeat=length )
                              for attempt in to_attempt:
                                      print(''.join ( attempt ))

                    elif choosebrute == "2":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( 1, length_input ):
                                to_attempt = product ( b, repeat=length )
                                for attempt in to_attempt:
                                    print(''.join ( attempt ))
                                    file.write ( ''.join ( attempt ) + "\n" )


                        else:
                            length_input = int ( raw_input ( "Length: " ) )
                            length_input += 1
                            for length in range ( 1, length_input):
                                to_attempt = product( b, repeat=length )
                                for attempt in to_attempt:
                                        print(''.join ( attempt ))

                    elif choosebrute == "3":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( 1, length_input):
                                to_attempt = product( c, repeat=length )
                                for attempt in to_attempt:
                                          print(''.join ( attempt ))
                                          file.write ( ''.join ( attempt ) + "\n" )

                        else:
                            length_input = int ( raw_input ( "Length: " ) )
                            length_input += 1
                            for length in range ( 1, length_input ):
                                to_attempt = product ( c, repeat=length )
                                for attempt in to_attempt:
                                    print(''.join ( attempt ))


                    elif choosebrute == "4":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( 1, length_input):
                                to_attempt = product( d, repeat=length )
                                for attempt in to_attempt:
                                        print(''.join ( attempt ))
                                        file.write ( ''.join ( attempt ) + "\n" )

                        else:
                            length_input = int ( raw_input ( "Length: " ) )
                            length_input += 1
                            for length in range ( 1, length_input ):
                                to_attempt = product ( d, repeat=length )
                                for attempt in to_attempt:
                                    print(''.join ( attempt ))


                    elif choosebrute == "5":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( 1, length_input):
                                to_attempt = product( e, repeat=length )
                                for attempt in to_attempt:
                                        print(''.join ( attempt ))
                                        file.write ( ''.join ( attempt ) + "\n" )

                        else:
                          length_input = int ( raw_input ( "Length: " ) )
                          length_input += 1
                          for length in range ( 1, length_input ):
                              to_attempt = product ( e, repeat=length )
                              for attempt in to_attempt:
                                  print(''.join ( attempt ))

                    elif choosebrute == "6":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( f, length_input):
                                to_attempt = product( f, repeat=length )
                                for attempt in to_attempt:
                                   print(''.join ( attempt ))
                                   file.write ( ''.join ( attempt ) + "\n" )

                        else:
                          length_input = int ( raw_input ( "Length: " ) )
                          length_input += 1
                          for length in range ( 1, length_input ):
                              to_attempt = product ( f, repeat=length )
                              for attempt in to_attempt:
                                  print(''.join ( attempt ))

                    elif choosebrute == "7":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( 1, length_input):
                                to_attempt = product( g, repeat=length )
                                for attempt in to_attempt:
                                        print(''.join ( attempt ))
                                        file.write ( ''.join ( attempt ) + "\n" )

                        else:
                          length_input = int ( raw_input ( "Length: " ) )
                          length_input += 1
                          for length in range ( 1, length_input ):
                              to_attempt = product ( g, repeat=length )
                              for attempt in to_attempt:
                                  print(''.join ( attempt ))



                    elif choosebrute == "8":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( 1, length_input):
                                 to_attempt = product( h, repeat=length )
                                 for attempt in to_attempt:
                                        print(''.join ( attempt ))
                                        file.write ( ''.join ( attempt ) + "\n" )

                        else:
                            length_input = int ( raw_input ( "Length: " ) )
                            length_input += 1
                            for length in range ( 1, length_input ):
                                to_attempt = product ( h, repeat=length )
                                for attempt in to_attempt:
                                    print(''.join ( attempt ))


                    elif choosebrute == "9":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( i, length_input):
                                to_attempt = product( f, repeat=length )
                                for attempt in to_attempt:
                                        print(''.join ( attempt ))
                                        file.write ( ''.join ( attempt ) + "\n" )
                        else:
                            length_input = int ( raw_input ( "Length: " ) )
                            length_input += 1
                            for length in range ( 1, length_input ):
                                to_attempt = product ( i, repeat=length )
                                for attempt in to_attempt:
                                    print(''.join ( attempt ))


                    elif choosebrute == "10":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( 1, length_input):
                                to_attempt = product( j, repeat=length )
                                for attempt in to_attempt:
                                        print(''.join ( attempt ))
                                        file.write ( ''.join ( attempt ) + "\n" )

                        else:
                            length_input = int ( raw_input ( "Length: " ) )
                            length_input += 1
                            for length in range ( 1, length_input ):
                                to_attempt = product ( j, repeat=length )
                                for attempt in to_attempt:
                                    print(''.join ( attempt ))


                    elif choosebrute == "11":
                        print "Safe on .txt documtent?"
                        print"(y)es               (n)o"
                        file_input = raw_input ( "==> " )
                        if file_input == "y":
                            file = open ( "wordlist.txt", "w" )
                            length_input = int(raw_input("Length: "))
                            length_input += 1
                            for length in range ( 1, length_input):
                                 to_attempt = product( k, repeat=length )
                                 for attempt in to_attempt:
                                         print(''.join ( attempt ))
                                         file.write ( ''.join ( attempt ) + "\n" )
                        else:
                            length_input = int ( raw_input ( "Length: " ) )
                            length_input += 1
                            for length in range ( 1, length_input ):
                                to_attempt = product ( k, repeat=length )
                                for attempt in to_attempt:
                                    print(''.join ( attempt ))


                    else:
                        pass

            elif input1 == "zip-cracker":
                zipfilename = 'a.zip'
                dictionary = 'dictionary.txt'

                password = None
                zip_file = zipfile.ZipFile ( zipfilename )

                a = 0
                x = "0123456789abcdefghijklmnopqrstuvwxyz"

                while a != 1:
                           for length in range ( 1, 9 ):
                                to_attempt = product ( x, repeat=length )
                                for attempt in to_attempt:
                                    print(''.join ( attempt ) + "\n")
                                    password = ''.join ( attempt ) + "\n"



                           try:


                                 zip_file.extractall ( pwd=password )
                                 password = 'Password found: %s' % password
                                 a += 1
                           except:
                                pass



            elif input1 == "admin-finder":

                tempa = 0
                tempb = -1

                target = raw_input ( "TARGET: " )
                list1 = ["admin.php", "admin.html", "index.php", "login.php", "login.html", "administrator", "admin",
                         "adminpanel", "cpanel", "login", "wp-login.php", "administrator", "admins", "logins",
                         "admin.asp", "login.asp", "adm/", "admin/", "admin/account.html", "admin/login.html",
                         "admin/login.htm", "admin/controlpanel.html", "admin/controlpanel.htm",
                         "admin/adminLogin.html", "admin/adminLogin.htm", "admin.htm", "admin.html", "adminitem/",
                         "adminitems/", "administrator/", "administrator/login.%EXT%", "administrator.%EXT%",
                         "administration/", "administration.%EXT%", "adminLogin/", "adminlogin.%EXT%",
                         "admin_area/admin.%EXT%", "admin_area/", "admin_area/login.%EXT%", "manager/", "superuser/",
                         "superuser.%EXT%", "access/", "access.%EXT%", "sysadm/", "sysadm.%EXT%", "superman/",
                         "supervisor/", "panel.%EXT%", "control/", "control.%EXT%", "member/", "member.%EXT%",
                         "members/", "user/", "user.%EXT%", "cp/", "uvpanel/", "manage/", "manage.%EXT%", "management/",
                         "management.%EXT%", "signin/", "signin.%EXT%", "log-in/", "log-in.%EXT%", "log_in/",
                         "log_in.%EXT%", "sign_in/", "sign_in.%EXT%", "sign-in/", "sign-in.%EXT%", "users/",
                         "users.%EXT%", "accounts/", "accounts.%EXT%", "bb-admin/login.%EXT%", "bb-admin/admin.%EXT%",
                         "bb-admin/admin.html", "administrator/account.%EXT%", "relogin.htm", "relogin.html",
                         "check.%EXT%", "relogin.%EXT%", "blog/wp-login.%EXT%", "user/admin.%EXT%", "users/admin.%EXT%",
                         "registration/", "processlogin.%EXT%", "checklogin.%EXT%", "checkuser.%EXT%",
                         "checkadmin.%EXT%", "isadmin.%EXT%", "authenticate.%EXT%", "authentication.%EXT%",
                         "auth.%EXT%", "authuser.%EXT%", "authadmin.%EXT%", "cp.%EXT%", "modelsearch/login.%EXT%",
                         "moderator.%EXT%", "moderator/", "controlpanel/", "controlpanel.%EXT%", "admincontrol.%EXT%",
                         "adminpanel.%EXT%", "fileadmin/", "fileadmin.%EXT%", "sysadmin.%EXT%", "admin1.%EXT%",
                         "admin1.html", "admin1.htm", "admin2.%EXT%", "admin2.html", "yonetim.%EXT%", "yonetim.html",
                         "yonetici.%EXT%", "yonetici.html", "phpmyadmin/", "myadmin/", "ur-admin.%EXT%", "ur-admin/",
                         "Server.%EXT%", "Server/", "wp-admin/", "administr8.%EXT%", "administr8/", "webadmin/",
                         "webadmin.%EXT%", "administratie/", "admins/", "admins.%EXT%", "administrivia/",
                         "Database_Administration/", "useradmin/", "sysadmins/", "sysadmins/", "admin1/",
                         "system-administration/", "administrators/", "pgadmin/", "directadmin/", "staradmin/",
                         "ServerAdministrator/", "SysAdmin/", "administer/", "LiveUser_Admin/", "sys-admin/", "typo3/",
                         "panel/", "cpanel/", "cpanel_file/", "platz_login/", "rcLogin/", "blogindex/", "formslogin/",
                         "autologin/", "manuallogin/", "simpleLogin/", "loginflat/", "utility_login/", "showlogin/",
                         "memlogin/", "login-redirect/", "sub-login/", "wp-login/", "login1/", "dir-login/",
                         "login_db/", "xlogin/", "smblogin/", "customer_login/", "UserLogin/", "login-us/",
                         "acct_login/", "bigadmin/", "project-admins/", "phppgadmin/", "pureadmin/", "sql-admin/",
                         "radmind/", "openvpnadmin/", "wizmysqladmin/", "vadmind/", "ezsqliteadmin/", "hpwebjetadmin/",
                         "newsadmin/", "adminpro/", "Lotus_Domino_Admin/", "bbadmin/", "vmailadmin/", "Indy_admin/",
                         "ccp14admin/", "irc-macadmin/", "banneradmin/", "sshadmin/", "phpldapadmin/", "macadmin/",
                         "administratoraccounts/", "admin4_account/", "admin4_colon/", "radmind-1/", "Super-Admin/",
                         "AdminTools/", "cmsadmin/", "SysAdmin2/", "globes_admin/", "cadmins/", "phpSQLiteAdmin/",
                         "navSiteAdmin/", "server_admin_small/", "logo_sysadmin/", "power_user/",
                         "system_administration/", "ss_vms_admin_sm/", "bb-admin/", "panel-administracion/",
                         "instadmin/", "memberadmin/", "administratorlogin/", "adm.%EXT%", "admin_login.%EXT%",
                         "panel-administracion/login.%EXT%", "pages/admin/admin-login.%EXT%", "pages/admin/",
                         "acceso.%EXT%", "admincp/login.%EXT%admincp/", "adminarea/", "admincontrol/",
                         "affiliate.%EXT%", "adm_auth.%EXT%", "memberadmin.%EXT%", "administratorlogin.%EXT%",
                         "modules/admin/", "administrators.%EXT%", "siteadmin/", "siteadmin.%EXT%", "adminsite/",
                         "kpanel/", "vorod/", "vorod.%EXT%", "vorud/", "vorud.%EXT%", "adminpanel/", "PSUser/",
                         "secure/", "webmaster/", "webmaster.%EXT%", "autologin.%EXT%", "userlogin.%EXT%",
                         "admin_area.%EXT%", "cmsadmin.%EXT%", "security/", "usr/", "root/", "secret/",
                         "admin/login.%EXT%", "admin/adminLogin.%EXT%", "moderator.php", "moderator.html",
                         "moderator/login.%EXT%", "moderator/admin.%EXT%", "yonetici.%EXT%", "0admin/", "0manager/",
                         "aadmin/", "cgi-bin/login%EXT%", "login1%EXT%", "login_admin/", "login_admin%EXT%",
                         "login_out/", "login_out%EXT%", "login_user%EXT%", "loginerror/", "loginok/", "loginsave/",
                         "loginsuper/", "loginsuper%EXT%", "login%EXT%", "logout/", "logout%EXT%", "secrets/",
                         "super1/", "super1%EXT%", "super_index%EXT%", "super_login%EXT%", "supermanager%EXT%",
                         "superman%EXT%", "superuser%EXT%", "supervise/", "supervise/Login%EXT%", "super%EXT%"]

                r = rq.get ( 'http://' + target )
                a = str ( r.url )
                b = a.split ( "w" )
                counter1 = -1
                list2 = [len(list1)]

                if b[0] == "https://":
                    protocol = "https://"

                else:
                    protocol = "http://"
                try:
                    while tempb <= len ( list1 ):
                        tempb += 1
                        code = protocol + target + "/" + ''.join ( list1[tempb] )

                        try:
                            urllib2.urlopen ( code )
                            a = "[+] " + code
                            print(a)
                            counter1 += 1
                            list2[counter1] = a

                        except:
                            print("[-] " + code)
                except:
                       pass

                print"\n~~~~~~~~Possible_Admin_Urls~~~~~~~~"
                counter1 = -1
                try:
                   while counter1  <= len(list2):
                         counter1 += 1
                         print list2[counter1]
                except:
                      pass

                print "Finished \n"

            elif input1 == "google-hacking":

                print"--------SELECT---------\n1)Find SQL-Injectable Websites\n2)Find some Files\n3)Find Files containing Passwords\n"

                searchLink = "https://www.google.com/search?q="

                input_google = int ( raw_input ( "==>" ) )

                if input_google == 1:
                    sql_lookup = "inurl:\".php?id=\"##\"You have an error in your SQL syntax\""
                    sql_lookup = sql_lookup.replace ( "##", "%20" )
                    command = "start " + searchLink + sql_lookup
                    print command
                    os.system ( command )

                elif input_google == 2:
                    print "----------------------\n 1).pdf [PDF]\n 2).docx [Wordfile]\n 3).ppt [Powerpoint]\n 4).swf [Adobe Flash]\n 5).ps [Adobe PostScript]\n 6).dwf [Autodesk Design Web Format]\n 7).kml [Google Earth]\n 8).gpx [GPS eXchange Format]\n 9).hwp[Hancom Hanword]\n 10).html[HTML]\n11).xls [Microsoft Excel]\n12).odp [OpenOffice presentation]\n13).ods [OpenOffice spreadsheet]\n14).odt [OpenOffice text]\n15).rtf [Rich Text Format]\n16).svg [Scalable Vector Graphics]\n17).tex [TeX/LaTeX]\n18).txt [Text]\n19).bas [Basic source code]\n20).c [C]\n21).cpp [C++]\n22).cs [C#]\n23).java [Java source code]\n24).pl [Perl source code]\n25).py [Python source code]\n26).wml [Wireless Markup Language]\n27).xml [XML]"

                    files = ["pdf", "docx", "ppt", "swf", "ps", "dwf", "kml", "gpx", "hwp", "html", "xls", "odp", "ods","odt", "rtf", "svg", "tex", "txt", "bas", "c", "cpp", "cs", "java", "pl", "py", "wml","xml"]
                    input_filefinder = int ( raw_input ( "==> " ) )
                    input_filefinder -= 1
                    print files[input_filefinder]
                    print "\nFilename:"
                    file_name = str ( raw_input ( "==>" ) )
                    file_name = file_name.replace ( " ", "%20" )
                    command = "start " + searchLink + "filetype:" + files[input_filefinder] + "%20" + file_name
                    print(command)
                    os.system ( command )

                elif input_google == 3:
                    command = "start " + searchLink + '\"password.xlsx\"' + '%20ext:xlsx'
                    print("Tab1 (Password-Tabellen) : " + command)
                    os.system ( command )
                    time.sleep ( 1 )
                    command = "start " + searchLink + 'filetype:env%20intext:REDIS_PASSWORD'
                    print("Tab2 (Password-Liste) : " + command)
                    os.system ( command )


            elif input1 == "crazy":
                 x = 0
                 v = 0
                 speed = raw_input("[slow | medium | fast | triggered]: ")
                 os.system ( "cls" )
                 if speed == "slow":
                     while x != 1:
                         a = randint ( 0, 70 )
                         time.sleep ( 0.4 )
                         os.system ( "color " + str ( a ) )
                 elif speed == "medium":
                     while x != 1:
                         a = randint ( 0, 70 )
                         time.sleep ( 0.2 )
                         os.system ( "color " + str ( a ) )
                 elif speed == "fast":
                     while x != 1:
                         a = randint ( 0, 70 )
                         time.sleep ( 0.1 )
                         os.system ( "color " + str ( a ) )
                 elif speed == "triggered":
                     while x != 1:
                         a = randint ( 0, 70 )
                         os.system ( "color " + str ( a ) )
                 else:
                     print("Type in slow medium fast or triggered (there are no more options ._.)")





            else:
                try:
                    jg(input1)

                except:
                      print "That's no avaible command..."


def start():

		while(1):
		    try:
            JG_CMD.startupmsg()
            time.sleep(1)
            JG_CMD.JGCMD()
            except:
			print""



start()
