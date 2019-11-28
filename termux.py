# -*- coding: UTF-8 -*-
#Woooyy goblog mau recode??!!!
#semoga yang ngerecode sial trus, jomblo selamanya
#bangsat kau
#muka lo kayak monyet, coba ngaca
#hargai dong kontol ..bikin tidak sesusah memakai
import os
import sys
import time
#warna
a = "\033[90m"
m = "\033[91m"
h = "\033[92m"
k = "\033[93m"
b = "\033[94m"
u = "\033[95m"
l = "\033[96m"
p = "\033[97m"

def tik():
	muter = ['[\]    ','[/]    ','[-]    ','[\]    ','[/]    ','[-]    ','[\]    ','[/]    ','[-]    ','[\]    ','[/]    ','[-]    ','[\]    ','[/]    ','[-]    ','[\]    ','[/]    ','[-]    ','[\]    ','[-]    ','[\]    ','[/]    ','[-]    ','[\]    ','[/]    ','[-]    ','[\]    ','[/]    ','[-]    ','[\]    ']
	for o in muter:
		print(m+"\r  ╠\033[94m• \033[90mTunggu\033[96m "+o),;sys.stdout.flush();time.sleep(0.1)

def nyerat(mmk):
    for kntl in mmk + '\n':
        sys.stdout.write(kntl)
        sys.stdout.flush()
        time.sleep(0.003)
        
def nulis(mmk):
    for kntl in mmk + '\n':
        sys.stdout.write(kntl)
        sys.stdout.flush()
        time.sleep(0.1)
        
def lanjt():
   time.sleep(1)
   os.system('clear')
   print " "
   print u+"..::\033[94m| \033[90mInstall Bahan Dulu Agar Gak \033[91mError \033[94m|\033[95m::.."
   print b+"•═══════════════════════════════════════════•"
   print "    \033[92m1. \033[93mLogin Ke Tool"
   print "    \033[92m2. \033[93mInstall Bahan"
   print "    \033[92m3. \033[93mExit"
   print b+"•═══════════════════════════════════════════•"
   po = raw_input(k+" [ \033[92m? \033[93m]\033[95m•\033[93m> ")   
   if po in ['1'] :
   	mulai()
   if po in ['2'] :
   	instalbahan()   	
   else:
   	exit
   
def instalbahan():
	os.system("pkg install lolcat")
	os.system("pip2 install lolcat")
	os.system("pkg install figlet")
	os.system("pkg install neofetch")
	os.system('clear')
	print h+"\n\n\n\n  install bahan selesai"
	print u+"\n      langsung login ke tool aja"
	time.sleep(3)
	lanjt()
	
def mnb():
   nyerat(b+"\n  ╭═══════════════════════════════════════════════════╮")
   nyerat(m+"•\033[94m─║\033[95m  _______ _______ _______ _______ _     _ _     _  \033[94m║─\033[91m•")
   nyerat(b+"  ║     \033[95m|    |______ |_____/ |  |  | |     |  \___/ \033[94m  ║")
   nyerat(b+"  ║    \033[95m |    |______ |    \_ |  |  | |_____| _/   \_  \033[94m║")
   nyerat(m+"•\033[94m─║                                                   ║─\033[91m•")
   nyerat(b+"  ╰═══════════════════════════════════════════════════╯ \n")
def banner():
    os.system("clear")
    print "\033[97m"
    nyerat(b+"       [ \033[92mW O W\033[94m ]    \033[96m--==\033[91m| \033[90mMemperganteng Termux \033[91m|\033[96m==--")
    nyerat(m+" ██████   \033[93m/\033[95m_______ _______ _______ _______ _     _ _     _")
    nyerat(m+"██ ██ ██ \033[93m/ \033[95m   |    |______ |_____/ |  |  | |     |  \___/ ")
    nyerat(m+"████████ \033[95m     |    |______ |    \_ |  |  | |_____| _/   \_")
    nyerat(m+"████  ██ ")
    nyerat(m+" ██████  \033[94m╔═\033[93m• \033[90mCoded By \033[92mDin-zUgex95 ")
    print u+"  /║\    \033[94m║   \033[93m• \033[90mYoutube \033[93m: \033[92mDin-zUgex95 "
    time.sleep (0.4)
    print u+"   ║     \033[94m║ \033[93m  • \033[90mGithub \033[93m :\033[92m https://github.com/Din-zUgex95"
    time.sleep(0.4)
    print u+"  / \    \033[94m║"
    print m+"✠\033[94m═╦══════╩═════════════════════════════════════════════\033[91m✠"
    time.sleep(0.3)
    print b+"  ║ \033[95m[\033[92m1\033[95m]\033[93m Logo Termux       \033[94m║ \033[95m[\033[92m4\033[95m]\033[93m Black Hat"
    time.sleep(0.2)
    print b+"  ║ \033[95m[\033[92m2\033[95m]\033[93m Logo Handphone    \033[94m║ \033[95m[\033[92m5\033[95m]\033[93m Tampilan Naga"
    time.sleep(0.1)
    print b+"  ║ \033[95m[\033[92m3\033[95m]\033[93m Biasa Tapi Keren  \033[94m║ \033[95m[\033[92m6\033[95m]\033[93m Tampilan Kucing"
    time.sleep(0.1)
    print m+"✠\033[94m═╬════════════════════════════════════════════════════\033[91m✠"
def pilih():
  try:
 
    pl = raw_input("\033[94m  ╚═══\033[93m•\033[95m>\033[92m ")
    if pl in ['1'] :
        logotermux()
    elif pl in ['2'] :
        logohp()
    elif pl in ['3'] :
        tampilbiasa()
    elif pl in ['4'] :
    	blackhat()
    elif pl in ['5'] :
    	naga()
    elif pl in ['6'] :
    	sioren()
    else:
 	time.sleep(1)
        print "      \n \033[95m• \033[91mPilih Yang Bener Cok\033[93m ..!!!\n"
        time.sleep(2)
        mulai()

  except KeyboardInterrupt:
    print "Keluar dari program..."
    sys.exit()
    
def mulai():
    banner()
    pilih()
def lgulg():
	os.system("echo  '       LOGIN ULANG UNTUK MELIHAT HASIL'|lolcat")
	
#TERMUX
	
def logotermux():
    os.system("clear")
    mnb()
    print b+"•\033[91m═╦═══════════════════════════════════════════════\033[94m•"
    nama = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Ditampilan  \033[93m: '))
    prompt = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Diprompt    \033[93m: '))
    print b+"•\033[91m═╬═══════════════════════════════════════════════\033[94m•"
    time.sleep(1)
    tik()
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\necho '\033[91m✵\033[95m════════════════════════════════════════════════════════════════════\033[91m✵'")
    ugex.write("\necho")
    ugex.write("\necho '        \033[94m████████\033[91m╗\033[94m███████\033[91m╗\033[94m██████\033[91m╗\033[94m ███\033[91m╗   \033[94m███\033[91m╗\033[94m██\033[91m╗   \033[94m██\033[91m╗\033[94m██\033[91m╗  \033[94m██\033[91m╗'")
    ugex.write("\necho '        ╚══\033[94m██\033[91m╔══╝\033[94m██\033[91m╔════╝\033[94m██\033[91m╔══\033[94m██\033[91m╗\033[94m████\033[91m╗ \033[94m████\033[91m║\033[94m██\033[91m║   \033[94m██\033[91m║╚\033[94m██\033[91m╗\033[94m██\033[91m╔╝'")
    ugex.write("\necho '           \033[94m██\033[91m║   \033[94m█████\033[91m╗  \033[94m██████\033[91m╔╝\033[94m██\033[91m╔\033[94m████\033[91m╔\033[94m██\033[91m║\033[94m██\033[91m║   \033[94m██\033[91m║ ╚\033[94m███\033[91m╔╝'")
    ugex.write("\necho '           \033[94m██\033[91m║   \033[94m██\033[91m╔══╝  \033[94m██\033[91m╔══\033[94m██\033[91m╗\033[94m██\033[91m║╚\033[94m██\033[91m╔╝\033[94m██\033[91m║\033[94m██\033[91m║   \033[94m██\033[91m║ \033[94m██\033[91m╔\033[94m██\033[91m╗'")
    ugex.write("\necho '           \033[94m██\033[91m║   \033[94m███████\033[91m╗\033[94m██\033[91m║  \033[94m██\033[91m║\033[94m██\033[91m║ ╚═╝ \033[94m██\033[91m║╚\033[94m██████\033[91m╔╝\033[94m██\033[91m╔╝ \033[94m██\033[91m╗'")
    ugex.write("\necho '           \033[91m╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝'")
    ugex.write("\necho")
    ugex.write("\necho '\033[91m✵\033[95m═╦══════════════════════════════════════════════════════════════════\033[91m✵'")
    ugex.write("\necho '  \033[95m╚══\033[94m[\033[92m"+nama+"\033[94m]'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print m+"\n  ╠\033[94m• \033[92mBERHASIL"
    time.sleep(0.3)
    nulis(m+"  ╚\033[94m• \033[90mSubscribe My Chanel \033[95mDin-zUgex95")
    time.sleep(1)
    print " "
    lgulg()
    print " "
   
#GAMBAR HAPE 
 
def logohp():
    os.system("clear")
    mnb()
    print b+"•\033[91m═╦═══════════════════════════════════════════════\033[94m•"
    nama = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Ditampilan  \033[93m: '))
    prompt = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Diprompt    \033[93m: '))
    print b+"•\033[91m═╬═══════════════════════════════════════════════\033[94m•"
    time.sleep(1)
    tik()
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\necho '\033[91m╭═════════════╮'")
    ugex.write("\necho '\033[91m║   \033[90m• ════    \033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║   \033[94m╭═════════════════════════\033[91m✪'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║   \033[94m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m╠\033[94m───╣  \033[91m≼\033[93m••\033[92m "+nama+" \033[93m••\033[91m≽'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║   \033[94m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║   \033[94m╰═════════════════════════\033[91m✪'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║\033[90m█████████████\033[91m║'")
    ugex.write("\necho '\033[91m║ \033[92m<   \033[96m ✖    \033[92m> \033[91m║'")
    ugex.write("\necho '\033[91m╰═════════════╯'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print m+"\n  ╠\033[94m• \033[92mBERHASIL"
    time.sleep(0.3)
    nulis(m+"  ╚\033[94m• \033[90mSubscribe My Chanel \033[95mDin-zUgex95")
    time.sleep(1)
    print " "
    lgulg()
    print " "
    
#BIASA    
    
def tampilbiasa():
    os.system("clear")
    mnb()
    print b+"•\033[91m═╦═══════════════════════════════════════════════\033[94m•"
    nama = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Ditampilan  \033[93m: '))
    prompt = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Diprompt    \033[93m: '))
    print b+"•\033[91m═╬═══════════════════════════════════════════════\033[94m•"
    time.sleep(1)
    tik()
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear")
    ugex.write("\necho '\033[94m©\033[91m═════════════════════════════\033[94m©'")
    ugex.write("\necho '\033[93m   ✪ \033[90mUser\033[93m : \033[92m"+nama+"'")
    ugex.write("\necho '\033[93m      ✪ \033[90m"+nama+"\033[93m ✪'")
    ugex.write("\necho '\033[94m©\033[91m═════════════════════════════\033[94m©'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print m+"\n  ╠\033[94m• \033[92mBERHASIL"
    time.sleep(0.3)
    nulis(m+"  ╚\033[94m• \033[90mSubscribe My Chanel \033[95mDin-zUgex95")
    time.sleep(1)
    print " "
    lgulg()
    print " "
   
#BLACKHAT:v
 
def blackhat():
    os.system("clear")
    mnb()
    print b+"•\033[91m═╦═══════════════════════════════════════════════\033[94m•"
    nama = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Ditampilan  \033[93m: '))
    prompt = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Diprompt    \033[93m: '))
    print b+"•\033[91m═╬═══════════════════════════════════════════════\033[94m•"
    time.sleep(1)
    tik()
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear") 
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\necho '\033[92m ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀    ██░ ██  ▄▄▄     ▄▄▄█████▓'")
    ugex.write("\necho '\033[92m▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒    ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒'")
    ugex.write("\necho '\033[92m▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░    ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░'")
    ugex.write("\necho '\033[92m▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄    ░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ '")
    ugex.write("\necho '\033[92m░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄   ░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░ '")
    ugex.write("\necho '\033[92m░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒    ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░   '")
    ugex.write("\necho '\033[92m▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ▒ ░▒░ ░  ▒   ▒▒ ░   ░    '")
    ugex.write("\necho ' \033[92m░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░     ░  ░░ ░  ░   ▒    ░ '")
    ugex.write("\necho ' \033[92m░          ░  ░     ░  ░░ ░      ░  ░       ░  ░  ░      ░  ░        '")
    ugex.write("\necho '\033[92m      ░                  ░     \033[91m "+nama+"'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print m+"\n  ╠\033[94m• \033[92mBERHASIL"
    time.sleep(0.3)
    nulis(m+"  ╚\033[94m• \033[90mSubscribe My Chanel \033[95mDin-zUgex95")
    time.sleep(1)
    print " "
    lgulg()
    print " "                             

#NAGA

def naga():
    os.system("clear")
    mnb()
    print b+"•\033[91m═╦═══════════════════════════════════════════════\033[94m•"
    nama = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Ditampilan  \033[93m: '))
    prompt = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Diprompt    \033[93m: '))
    print b+"•\033[91m═╬═══════════════════════════════════════════════\033[94m•"
    time.sleep(1)
    tik()
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear") 
    ugex.write("\necho")
    ugex.write("\necho '\033[95m                      ______________'")
    ugex.write("\necho '                ,===:.,            `-._'")
    ugex.write("\necho '                `:.`---.__         `-._'")
    ugex.write("\necho '                  `:.     `--.         `.'")
    ugex.write("\necho '                    \.        `.         `.'")
    ugex.write("\necho '            (,,(,    \.         `.   ____,-`.,'")
    ugex.write("\necho '         (,      `/   \.   ,--.___`.'")
    ugex.write("\necho '     ,  ,  ,--.   `,   \. ;`'")
    ugex.write("\necho '      `{\033[91mD\033[95m,{     \  :    \ ;  \033[92m"+nama+"'")
    ugex.write("\necho ' \033[95m       V,,     /  /    //'")
    ugex.write("\necho '        j;;    /  ,  ,-//.    ,---.      ,'")
    ugex.write("\necho '        \;    /  ,  /  _  \  /  _  \   , /'")
    ugex.write("\necho '              \   `   / \  `   / \  `.  /'")
    ugex.write("\necho '               `.___,/   `.__,/   `.__,/'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print m+"\n  ╠\033[94m• \033[92mBERHASIL"
    time.sleep(0.3)
    nulis(m+"  ╚\033[94m• \033[90mSubscribe My Chanel \033[95mDin-zUgex95")
    time.sleep(1)
    print " "
    lgulg()
    print " "           
  
#KOCHENG
  
def sioren():
    os.system("clear")
    mnb()
    print b+"•\033[91m═╦═══════════════════════════════════════════════\033[94m•"
    nama = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Ditampilan  \033[93m: '))
    prompt = str(raw_input('  \033[91m╠\033[94m•\033[95m> \033[92mNama Buat Diprompt    \033[93m: '))
    print b+"•\033[91m═╬═══════════════════════════════════════════════\033[94m•"
    time.sleep(1)
    tik()
    time.sleep(1)
    ugex = open("bash.bashrc", "w")
    ugex.write("clear") 
    ugex.write("\necho")
    ugex.write("\necho '\033[93m .--.'")
    ugex.write("\necho ' `-. \             /\_ '")
    ugex.write("\necho '    \ \           /  \033[91ma\033[93m`.'")
    ugex.write("\necho '\033[93m     \ \__..---../  ,__/'")
    ugex.write("\necho '      \   \033[90mkocheng   \033[93m|'")
    ugex.write("\necho '      |  \033[90m  oren \033[93m   /'")
    ugex.write("\necho '      /\ \-~~~-`\ \ \  \033[92m"+nama+"'")
    ugex.write("\necho '    \033[93m /_/_/_      \_\_\_'")
    ugex.write("\necho '   \033[93m  \_\___)      \__)_)\'")
    ugex.write("\necho")
    ugex.write("\necho")
    ugex.write("\n\nPS1='\033[1;34m\]╭───\[\033[1;31m\][ \[\033[1;33m\]"+prompt+"\[\033[1;34m\]•\[\033[1;30m\]\w\[\033[1;31m\] ]")
    ugex.write("\n\[\033[1;34m\]╰──╼\[\033[1;31m\]✠\[\033[1;32m\] '")
    ugex.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print m+"\n  ╠\033[94m• \033[92mBERHASIL"
    time.sleep(0.3)
    nulis(m+"  ╚\033[94m• \033[90mSubscribe My Chanel \033[95mDin-zUgex95")
    time.sleep(1)
    print " "
    lgulg()
    print " "           
    
    
    
    
if __name__=='__main__':
  lanjt()
