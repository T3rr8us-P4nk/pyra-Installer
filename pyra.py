import os,sys
import random
from time import sleep
os.system("clear")
sleep(2)
os.system("clear")
print(""" \033[1;35;40m
   _________________
 <[ Welcome To Pyr4 ]>
   -----------------


   \033[1;32;40m
                ,aadd"'    `"bbaa,.
            ,ad8888P'          `Y8888ba,
         ,a88888888              88888888a,
       a88888888888              88888888888a
     a8888888888888b,          ,d8888888888888a
    d8888888888888888b,_    _,d8888888888888888b
   d88888888888888888888888888888888888888888888b
  d8888888888888888888888888888888888888888888888b
 I888888888888888888888888888888888888888888888888I
,88888888888888888888888888888888888888888888888888,
I8888888888888888PY8888888PY88888888888888888888888I
8888888888888888"  "88888"  "88888888888888888888888
8::::::::::::::'    `:::'    `:::::::::::::::::::::8
Ib:::::::::::"        "        `::::::' `:::::::::dI
`8888888888P            Y88888888888P     Y88888888'
 Ib:::::::'              `:::::::::'       `:::::dI
  Yb::::"                  ":::::"           "::dP
   Y88P                      Y8P               `P
    Y'                        "
                                `:::::::::::;8"
       "888888888888888888888888888888888888"
         `"8;::::::::::::::::::::::::::;8"'
            `"Ya;::::::::::::::::::;aP"'
                ``""YYbbaaaaddPP""''

  \033[1;31;40m   >>>>>>>>>>>>>>> 𝐏𝐲𝐫𝟒-𝐓𝐨𝐨𝐥 <<<<<<<<<<<<<<<<
     >>>>>>>>>>>>> Total Tools = 100+ <<<<<<<<
""")
# Tool Option
sleep(2)
print(" ")
print(" ")
print(" ")
print("\033[1;34;40m Select Tool :")
print("\033[1;32;40m[1] EvilGinX")
print("[2] PhishX")
print("[3] HiddenEye")
print("[4] ShellPhish")
print("[5] SocialPhish")
print("[6] Weeman")
print("[7] BlackEye")
print("[8] Zphisher")
print("[9] Nexphisher")
print("[10] AdvPhishing")
print("[11] Hydra")
print("[12] BruteX")
print("[13] Facebook-Cracker")
print("[14] Facebook-BruteForce")
print("[15] Firecrack")
print("[16] FBbrute")
print("[17] Fbb")
print("[18] Fb-Cracker")
print("[19] BRUTEFORCEnew")
print("[20] Instahack")
print("[21] Instabrute")
print("[22] Instainsane")
print("[23] Instax")
print("[24] Phoneifoga")
print("[25] Instashell")
print("[26] BruteSpray")
print("[27] Cupp")
print("[28] Lazybee")
print("[29] Wordlistor")
print("[30] GobinWordGenerator")
print("[31] Pass-Gen")
print("[32] Crunch")
print("[33] Indonesian-wordlist")
print("[34] Nmap")
print("[35] RouterSploit")
print("[36] Nikto")
print("[37] Recon-ng")
print("[38] Nscan")
print("[39] RED_HAWK")
print("[40] SQLmap")
print("[41] Cyberscan")
print("[42] TMscanner")
print("[43] Owscan")
print("[44] XAttacker")
print("[45] Xsssniper")
print("[46] ReconDog")
print("[47] Striker")
print("[48] Skipfish")
print("[49] Rang3r")
print("[50] Sublis3r")
print("[51] ReconSpider")
print("[52] wpscan")
print("[53] wascan")
print("[54] Zarp")
print("[55] HeartbleedScanner")
print("[56] Angry Fuzzer")
print("[57] CMSmap")
print("[58] Wpseku")
print("[59] CMSeek Suit")
print("[60] CheckUrl")
print("[61] Knockpy")
print("[62] A2SV-ssl-vul-scan")
print("[63] Smbscanner")
print("[64] Visql")
print("[65] Wordpresscan")
print("[66] SQLiv")
print("[67] SQLmapte")
print("[68] Easymap")
print("[69] Gasmask")
print("[70] Kill shot")
print("[71] Astronmap")
print("[72] Nosql")
print("[73] Click-jacking")
print("[74] Maxsubdofinder")
print("[75] Wifite")
print("[76] Wifite2")
print("[77] Wifiphisher")
print("[78] Aircrack-ng")
print("[79] Wifi-BruteForce")
print("[80] Autopixie")
print("[81] Ehtools")
print("[82] Trape")
print("[83] Seeker")
print("[84] Locator")
print("[85] Firefly")
print("[86] Saycheese")
print("[87] Grabcam")
print("[88] Camphish")
print("[89] WishPhish")
print("[90] IPCS")
print("[91] Sayhellow")
print("[92] Lockphish")
print("[93] Hacklock")
print("[94] Cam-Hackers")
print("[95] CCTV")
print("[96] IP-Geolocation")
print("[97] Crips")
print("[98] IP-Tracer")
print("[99] IP-Attack")
print("[100] IP-Tracker")
print("[101] IP-FY")
print("[102] Metasploit")
print("[103] Beef")
print("[104] PhoneSploit")
print("[105] Websploit")
print("[106] A-Rat")
print("[107] The FatRat")
print("[108] Viel-Evasion")
print("[109] Evil-Droid")
print("[110] TMvenom")
print("[111] Duck-Droid")
print("[112] Ghost-Framework")
print("[113] Commix")
print("[114] Parat")
print("[115] MSF-Pg")
print("[116] AndroBugs_Framework")
print("[117] Weevely")
print("[118] John The Ripper")
print("[119] TBomb")
print("[120] Quack")
print("[121] Hbomb")
print("[122] Email-Bomber")
print("[123] Tool-X")
print("[124] Onex")
print("[125] Dark-Fly")
print("[126] Lazymux")
print("[127] LazyScript")
print("[128] Thechoice")
print("[129] GoldenEye")
print("[130] D-Tect")
print("[131] PiPhish")
print("[132] Hulk")
print("[133] DDOS-Attack")
print(" ")
print("[00] Exit")

# Take input from the user
print(" ")
choice = input("\033[1;31;40mEnter choice: \033[1;32;40m")

# Installation
# EvilGinX
if choice == "1":
        print(os.system("git clone https://github.com/kgretzky/evilginx"))
        print (os.system("mv evilginx ~"))
# PhishX:
if choice == "2":
    print (os.system("https://github.com/kucuksemsiyelicocuk/WeebSec-PhishX"))
    print (os.system("mv PhishX ~"))
# HiddenEye:
if choice == "3":
    print (os.system("git clone https://github.com/DarkSecDevelopers/HiddenEye.git"))
    print (os.system("mv HiddenEye ~"))
# Shellphish:
if choice == "4":
    print (os.system("git clone https://github.com/jaykali/shellphish"))
    print (os.system("mv shellphish ~"))
# SocialFish:
if choice == "5":
    print (os.system("git clone https://github.com/UndeadSec/SocialFish.git"))
    print (os.system("mv SocialFish ~"))
# weeman:
if choice == "6":
    print (os.system("git clone https://github.com/samyoyo/weeman.git"))
    print (os.system("mv weeman ~"))
# BlackEye:
if choice == "7":
    print (os.system("git clone https://github.com/An0nUD4Y/blackeye"))
    print (os.system("mv blackeye ~"))
# Zphisher:
if choice == "8":
    print (os.system("git clone git://github.com/htr-tech/zphisher.git"))
    print (os.system("mv zphisher ~"))
# Nexphisher:
if choice == "9":
    print (os.system("git clone https://github.com/htr-tech/nexphisher"))
    print (os.system("mv nexphisher ~"))
# ADV phishing:
if choice == "10":
    print (os.system("git clone https://github.com/Ignitetch/AdvPhishing.git"))
    print (os.system("mv AdvPhishing ~"))
# Hydra:
if choice == "11":
    print (os.system("cd && apt install hydra"))
 # BruteX:
if choice == "12":
    print (os.system("git clone https://github.com/1N3/BruteX"))
    print (os.system("mv BruteX ~"))
# facebook-cracker:
if choice == "13":
    print (os.system("git clone https://github.com/Ha3MrX/facebook-cracker"))
    print (os.system("mv facebook-cracker ~"))
# Facebookbruteforce:
if choice == "14":
    print (os.system("git clone https://github.com/IAmBlackHacker/Facebook-BruteForce"))
    print (os.system("mv Facebook-BruteForce ~"))
# Firecrack:
if choice == "15":
    print (os.system("git clone https://github.com/Ranginang67/Firecrack"))
    print (os.system("mv Firecrack ~"))
# FBbrute:
if choice == "16":
    print (os.system("git clone https://github.com/Gameye98/FBBrute"))
    print (os.system("mv FBBrute ~"))
# fbb:
if choice == "17":
    print (os.system("git clone https://github.com/Cabdulahi/fbb"))
    print (os.system("mv fbb ~"))
# FB-cracker:
if choice == "18":
    print (os.system("git clone https://github.com/kaitolegion/FB-Cracker"))
    print (os.system("mv FB-Cracker ~"))
# Bruteforcernew:
if choice == "19":
    print (os.system("git clone https://github.com/FR13ND8/BRUTEFORCEnew"))
    print (os.system("mv BRUTEFORCEnew ~"))
# Instahack:
if choice == "20":
    print (os.system("git clone https://github.com/fuck3erboy/instahack"))
    print (os.system("mv instahack ~"))
# Instabrute:
if choice == "21":
    print (os.system("git clone https://github.com/Ha3MrX/InstaBrute"))
    print (os.system("mv InstaBrute ~"))
# Instainsane:
if choice == "22":
    print (os.system("git clone https://github.com/umeshshinde19/instainsane"))
    print (os.system("mv instainsane ~"))
# Instax:
if choice == "23":
    print (os.system("git clone https://github.com/dhasirar/instax.git"))
    print (os.system("mv instax ~"))
# Phoneifoga
if choice == "24":
    print (os.system("git clone https://github.com/abhinavkavuri/PhoneInfoga"))
    print (os.system("mv PhoneInfoga ~"))
# Instashell:
if choice == "25":
    print (os.system("git clone https://github.com/F33Z/instashell.git"))
    print (os.system("mv instashell ~"))
# Brutespray:
if choice == "26":
    print (os.system("git clone https://github.com/x90skysn3k/brutespray"))
    print (os.system("mv brutespray ~"))
# cupp:
if choice == "27":
    print (os.system("git clone https://github.com/Mebus/cupp"))
    print (os.system("mv cupp ~"))
# Lazybee:
if choice == "28":
    print (os.system("git clone https://github.com/noob-hackers/lazybee"))
    print (os.system("mv lazybee ~"))
# Wordlister:
if choice == "29":
    print (os.system("git clone https://github.com/4n4nk3/Wordlister"))
    print (os.system("mv Wordlister ~"))
# GoblinWordGenerator:
if choice == "30":
    print (os.system("git clone https://github.com/UndeadSec/GoblinWordGenerator.git"))
    print (os.system("mv GoblinWordGenerator ~"))
# Passgen:
if choice == "31":
    print (os.system("git clone https://github.com/Broham/PassGen"))
    print (os.system("mv PassGen ~"))
# crunch:
if choice == "32":
    print (os.system("git clone https://github.com/crunchsec/crunch"))
    print (os.system("mv crunch ~"))
# Indonation wordlist:
if choice == "33":
    print (os.system("git clone https://github.com/geovedi/indonesian-wordlist"))
    print (os.system("mv indonesian-wordlist ~"))

# nmap:
if choice == "34":
    print (os.system("apt install nmap"))
    print ("Type nmap your nmap will be started")
 # Routersploit
if choice == "35":
    print (os.system("git clone https://github.com/threat9/routersploit"))
    print (os.system("mv routersploit ~"))
# Nicto:
if choice == "36":
    print (os.system("git clone https://github.com/sullo/nikto"))
    print (os.system("mv nikto ~"))
# Recon ng:
if choice == "37":
    print (os.system("git clone https://github.com/lanmaster53/recon-ng"))
    print (os.system("mv recon-ng ~"))
# Nscan:
if choice == "38":
    print (os.system("git clone https://github.com/Anon-Divyanth/Nscan"))
    print (os.system("mv Nscan ~"))
# red hawk:
if choice == "39":
    print (os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK"))
    print (os.system("mv RED_HAWK ~"))
# Sqlmap:
if choice == "40":
    print (os.system("git clone https://github.com/sqlmapproject/sqlmap.git"))
    print (os.system("mv sqlmap ~"))
# Cyberscan:
if choice == "41":
    print (os.system("git clone https://github.com/medbenali/CyberScan.git"))
    print (os.system("mv CyberScan ~"))
# Tmscanner:
if choice == "42":
    print (os.system("git clone https://github.com/TechnicalMujeeb/TM-scanner.git"))
    print (os.system("mv TM-scanner ~"))
# OWScan:
if choice == "43":
    print (os.system("git clone https://github.com/Gameye98/OWScan"))
    print (os.system("mv OWScan ~"))
# XAttacker:
if choice == "44":
    print (os.system("git clone https://github.com/Moham3dRiahi/XAttacker.git"))
    print (os.system("mv XAttacker ~"))
# xsssniper:
if choice == "45":
    print (os.system("git clone https://github.com/gbrindisi/xsssniper"))
    print (os.system("mv xsssniper ~"))
# ReconDog:
if choice == "46":
    print (os.system("git clone https://github.com/s0md3v/ReconDog"))
    print (os.system("mv ReconDog ~"))
# Striker:
if choice == "47":
    print (os.system("git clone https://github.com/s0md3v/Striker"))
    print (os.system("mv Striker ~"))
# Skipfish:
if choice == "48":
    print (os.system("git clone https://github.com/spinkham/skipfish"))
    print (os.system("mv skipfish ~"))
# rang3r:
if choice == "49":
    print (os.system("git clone https://github.com/floriankunushevci/rang3r"))
    print (os.system("mv rang3r ~"))
# sublis3r:
if choice == "50":
    print (os.system("git clone https://github.com/aboul3la/Sublist3r.git"))
    print (os.system("mv Sublist3r ~"))
# reconspider:
if choice == "51":
    print (os.system("git clone https://github.com/bhavsec/reconspider.git"))
    print (os.system("mv reconspider ~"))
# wpscan:
if choice == "52":
    print (os.system("gem install bundler"))
    print (os.system("bundle install"))
    print (os.system("git clone https://github.com/wpscanteam/wpscan.git"))
    print (os.system("mv wpscan ~"))
# Wascan:
if choice == "53":
    print (os.system("git clone https://github.com/m4ll0k/WAScan.git"))
    print (os.system("mv WAScan ~"))
# Zarp:
if choice == "54":
    print (os.system("git clone git://github.com/hatRiot/zarp.git"))
    print (os.system("mv zarp ~"))
# Heartbleed:
if choice == "55":
    print (os.system("git clone https://github.com/TechnicalMujeeb/HeartBleed"))
    print (os.system("mv HeartBleed ~"))
# angryFuzzer:
if choice == "56":
    print (os.system("git clone https://github.com/ihebski/angryFuzzer.git"))
    print (os.system("mv angryFuzzer ~"))
# CMsmap:
if choice == "57":
    print (os.system("git clone https://github.com/Dionach/CMSmap"))
    print (os.system("mv CMSmap ~"))
# wpseku:
if choice == "58":
    print (os.system("git clone https://github.com/m4ll0k/WPSeku.git"))
    print (os.system("mv WPSeku ~"))
# CMSeek:
if choice == "59":
    print (os.system("git clone https://github.com/Tuhinshubhra/CMSeeK"))
    print (os.system("mv CMSeeK ~"))
# CheckUrl:
if choice == "60":
    print (os.system("git clone https://github.com/UndeadSec/checkURL.git"))
    print (os.system("mv checkURL ~"))
# Knockpy:
if choice == "61":
    print (os.system("git clone https://github.com/guelfoweb/knock.git"))
    print (os.system("mv knock ~"))
# a2sv:
if choice == "62":
    print (os.system("git clone https://github.com/hahwul/a2sv.git"))
    print (os.system("mv a2sv ~"))
# smbscanner:
if choice == "63":
    print (os.system("git clone https://github.com/TechnicalMujeeb/smb-scanner"))
    print (os.system("mv smb-scanner ~"))
# viSQL:
if choice == "64":
    print (os.system("git clone https://github.com/Marcel0Sousa/script-viSQL"))
    print (os.system("mv viSQL ~"))
# wordpresscan:
if choice == "65":
    print (os.system("git clone https://github.com/swisskyrepo/Wordpresscan.git"))
    print (os.system("mv Wordpresscan ~"))
# SQliv:
if choice == "66":
    print (os.system("git clone https://github.com/the-robot/sqliv.git"))
    print (os.system("mv sqliv ~"))
# sqlmate:
if choice == "67":
    print (os.system("git clone https://github.com/UltimateHackers/sqlmate"))
    print (os.system("mv sqlmate ~"))
# Easymap:
if choice == "68":
    print (os.system("git clone https://github.com/Cvar1984/Easymap"))
    print (os.system("mv Easymap ~"))
# gasmask:
if choice == "69":
    print (os.system("git clone https://github.com/twelvesec/gasmask"))
    print (os.system("mv gasmask ~"))
# Killshot:
if choice == "70":
    print (os.system("git clone https://github.com/bahaabdelwahed/killshot"))
    print (os.system("mv killshot ~"))
# Astronmap:
if choice == "71":
    print (os.system("git clone https://github.com/Gameye98/AstraNmap"))
    print (os.system("mv AstraNmap ~"))
# nosql:
if choice == "72":
    print (os.system("git clone  https://github.com/codingo/NoSQLMap"))
    print (os.system("mv NoSQLMap ~"))
# Click-jacking:
if choice == "73":
    print (os.system("git clone https://github.com/D4Vinci/Clickjacking-Tester"))
    print (os.system("mv Clickjacking-Tester ~"))
# Maxsubdofinder:
if choice == "74":
    print (os.system("git clone https://github.com/maxteroit/MaxSubdoFinder"))
    print (os.system("mv MaxSubdoFinder ~"))
# Wifite:
if choice == "75":
    print (os.system("wget https://raw.github.com/derv82/wifite/master/wifite.py"))
    print (os.system("mv wifite.py ~"))
# Wifite2:
if choice == "76":
    print (os.system("git clone https://github.com/derv82/wifite2.git"))
    print (os.system("mv wifite2 ~"))
# wifiphisher:
if choice == "77":
    print (os.system("git clone https://github.com/wifiphisher/wifiphisher.git"))
    print (os.system("mv wifiphisher ~"))
# aircrack-ng:
if choice == "78":
    print (os.system("apt install root-repo"))
    print (os.system("apt install aircrack-ng"))
    print ("Then Type sudo airmon-ng")
# wifi-bruteforcer:
if choice == "79":
    print (os.system("git clone https://github.com/faizann24/wifi-bruteforcer-fsecurify"))
    print (os.system("mv wifi-bruteforcer ~"))
# Autopixie:
if choice == "80":
    print (os.system("git clone https://github.com/nxxxu/AutoPixieWps"))
    print (os.system("mv AutoPixieWps ~"))
# ehtools:
if choice == "81":
    print (os.system("git clone https://github.com/entynetproject/ehtools"))
    print (os.system("mv ehtools ~"))
# Trape:
if choice == "82":
    print (os.system("git clone https://github.com/jofpin/trape.git"))
    print (os.system("mv trape ~"))
# seeker:
if choice == "83":
    print (os.system("git clone https://github.com/thewhiteh4t/seeker.git"))
    print (os.system("mv seeker ~"))
# Locator:
if choice == "84":
    print (os.system("git clone https://github.com/thelinuxchoice/locator"))
    print (os.system("mv locator ~"))
# Firefly:
if choice == "85":
    print (os.system("git clone https://github.com/M3-SEC/firefly.git"))
    print (os.system("mv firefly ~"))
# Saycheese:
if choice == "86":
    print (os.system("git clone https://github.com/Anonymous3-SIT/saycheese"))
    print (os.system("mv saycheese ~"))
# Grabcam:
if choice == "87":
    print (os.system("git clone https://github.com/noob-hackers/grabcam"))
    print (os.system("mv grabcam ~"))
# camphish:
if choice == "88":
    print (os.system("git clone https://github.com/techchipnet/CamPhish"))
    print (os.system("mv CamPhish ~"))
# WishFish:
if choice == "89":
    print (os.system("git clone https://github.com/kinghacker0/WishFish"))
    print (os.system("mv WishFish ~"))
# IPCS:
if choice == "90":
    print (os.system("git clone https://github.com/kancotdiq/ipcs"))
    print (os.system("mv ipcs ~"))
# Sayhellow:
if choice == "91":
    print (os.system("git clone https://github.com/d093w1z/sayhello"))
    print (os.system("mv sayhello ~"))
# lockphish:
if choice == "92":
    print (os.system("git clone https://github.com/JasonJerry/lockphish"))
    print (os.system("mv lockphish ~"))
# Hacklock:
if choice == "93":
    print (os.system("git clone https://github.com/noob-hackers/hacklock"))
    print (os.system("mv hacklock ~"))
# cam-Hackers:
if choice == "94":
    print (os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers"))
    print (os.system("mv Cam-Hackers ~"))
# CCTV:
if choice == "95":
    print (os.system("git clone https://github.com/GUNAWAN18ID/cctv"))
    print (os.system("mv cctv ~"))
# IP-Geolocation:
if choice == "96":
    print (os.system("git clone https://github.com/maldevel/IPGeoLocation"))
    print (os.system("mv IPGeoLocation ~"))
# crips:
if choice == "97":
    print (os.system("git clone https://github.com/Manisso/Crips.git"))
    print (os.system("mv Crips ~"))
# IP-Tracer:
if choice == "98":
    print (os.system("git clone https://github.com/rajkumardusad/IP-Tracer.git"))
    print (os.system("mv IP-Tracer ~"))
# IP-Attack:
if choice == "99":
    print (os.system("git clone https://github.com/Bhai4You/Ip-Attack"))
    print (os.system("mv Ip-Attack ~"))
# IP-Tracker:
if choice == "100":
    print (os.system("git clone git://github.com/htr-tech/track-ip.git"))
    print (os.system("mv track-ip ~"))
# IP-FY:
if choice == "101":
    print (os.system("git clone https://github.com/T4P4N/IP-FY"))
    print (os.system("mv IP-FY ~"))
# Metasploit:
if choice == "102":
    print (" NOTE: It takes over 30 Minutes for installation ")
    x = input(" If U want to install metasploit [y/n] : ")
    if x == "y" or x == "Y":
       print (os.system("pkg install unstable-repo"))
       print (os.system("pkg install metasploit"))
       print (" Type \" msfconsole \" your metasploit will be started")
    else:
       exit()
# Beef:
if choice == "103":
    print (os.system("git clone https://github.com/beefproject/beef"))
    print (os.system("mv beef ~"))
# Phonesploit:
if choice == "104":
    print (os.system("git clone https://github.com/Zucccs/PhoneSploit"))
    print (os.system("mv PhoneSploit ~"))
# websploit:
if choice == "105":
    print (os.system("git clone https://github.com/websploit/websploit.git"))
    print (os.system("mv websploit ~"))
# A-Rat:
if choice == "106":
    print (os.system("git clone https://github.com/Xi4u7/A-Rat"))
    print (os.system("mv A-Rat ~"))
# The FatRat:
if choice == "107":
    print (os.system("git clone https://github.com/Screetsec/TheFatRat.git"))
    print (os.system("mv TheFatRat ~"))
# viel-Evasion:
if choice == "108":
    print (os.system("git clone https://github.com/Veil-Framework/Veil-Evasion.git"))
    print (os.system("mv Veil-Evasion ~"))
# Evil-Droid:
if choice == "109":
    print (os.system("git clone https://github.com/M4sc3r4n0/Evil-Droid.git"))
    print (os.system("mv Evil-Droid ~"))
# TMvenom:
if choice == "110":
    print (os.system("git clone https://github.com/TechnicalMujeeb/tmvenom.git"))
    print (os.system("mv tmvenom ~"))
# Duck-Droid:
if choice == "111":
    print (os.system("git clone https://github.com/T4Termux/Duck_Droid.git"))
    print (os.system("mv Duck_Droid ~"))
# Ghost-Framework:
if choice == "112":
    print (os.system("git clone https://github.com/entynetproject/ghost"))
    print (os.system("mv ghost ~"))
# Commix:
if choice == "113":
    print (os.system("git clone https://github.com/commixproject/commix.git"))
    print (os.system("mv commix ~"))
# Parat:
if choice == "114":
    print (os.system("git clone https://github.com/micle-fm/Parat"))
    print (os.system("mv Parat ~"))
# MSF-Pg:
if choice == "115":
    print (os.system("git clone https://github.com/haxzsadik/MSF-Pg"))
    print (os.system("mv MSF-Pg ~"))
# AndroBugs_Framework:
if choice == "116":
    print (os.system("git clone https://github.com/AndroBugs/AndroBugs_Framework"))
    print (os.system("mv AndroBugs_Framework ~"))
# Weevely:
if choice == "117":
    print (os.system("git clone https://github.com/sunge/Weevely"))
    print (os.system("mv Weevely ~"))
if choice == "118":
    print (os.system("git clone https://github.com/magnumripper/JohnTheRipper.git"))
    print (os.system("mv JohnTheRipper ~"))
# Tbomb:
if choice == "119":
    print (os.system("git clone https://github.com/TheSpeedX/TBomb.git"))
    print (os.system("mv TBomb ~"))
# Quack:
if choice == "120":
    print (os.system("git clone https://github.com/entynetproject/quack"))
    print (os.system("mv quack ~"))
# Hbomb:
if choice == "121":
    print (os.system("git clone https://github.com/HoneyPots0/HBomb"))
    print (os.system("mv HBomb ~"))
# Email-Bomber:
if choice == "122":
    print (os.system("git clone https://github.com/mohinparamasivam/Email_Bomber.git"))
    print (os.system("mv Email_Bomber ~"))
# Tool-X
if choice == "123":
    print (os.system("git clone https://github.com/rajkumardusad/Tool-X.git"))
    print (os.system("mv Tool-X ~"))
# onex:
if choice == "124":
    print (os.system("git clone https://github.com/rajkumardusad/onex.git"))
    print (os.system("mv onex ~"))
# Dark-fly:
if choice == "125":
    print (os.system("git clone https://github.com/Ranginang67/DarkFly-Tool"))
    print (os.system("mv DarkFly-Tool ~"))
# Lazymux:
if choice == "126":
    print (os.system("git clone https://github.com/Gameye98/Lazymux"))
    print (os.system("mv Lazymux ~"))
# Lazyscript:
if choice == "127":
    print (os.system("git clone https://github.com/TechnicalMujeeb/Termux-Lazyscript.git"))
    print (os.system("mv Termux-Lazyscript ~"))
# Thechoice:
if choice == "128":
    print (os.system("git clone https://github.com/thelinuxchoice/thechoice"))
    print (os.system("mv thechoice ~"))
# GoldenEye:
if choice == "129":
    print (os.system("git clone https://github.com/jseidl/GoldenEye"))
    print (os.system("mv GoldenEye ~"))
# D-tect:
if choice == "130":
    print (os.system("git clone https://github.com/shawarkhanethicalhacker/D-TECT-1"))
    print (os.system("mv D-TECT-1 ~"))
# PiPhish
if choice == "131":
   print (os.system("git clone https://github.com/ridwanirawan/PiPhish"))
   print (os.system("mv PiPhish ~"))
# Hulk
if choice == "132":
    print (os.system("git clone https://github.com/grafov/hulk"))
    print (os.system("mv hulk ~"))
# Ddos-Attack:
if choice == "133":
    print (os.system("git clone https://github.com/Ha3MrX/DDos-Attack"))
    print (os.system("mv DDos-Attack ~"))

# Exit
if choice == "00":
        exit()