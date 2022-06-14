from impacket import ImpactDecoder
from impacket import ImpactPacket
import socket
ipheader = ImpactPacket.IP()
icmpheader = ImpactPacket.ICMP()

def welcome():
    #Dependency Check
    try: 
        from impacket import ImpactDecoder
    except ImportError:
        print("Impacket library is missing (Run", "pip install impacket)")
        exit(1)
    #Welcome Prompt
    print("Welcome to ICMP Attack Suite!", "1. Set ICMP Parameters", "2. Set ICMP Payload", "3. Start Attack", "4. Exit", sep='\n', end='\n')
    sel1 = input("Your Selection: ")
    if(sel1 == "1"):
        icmpparams()
    elif(sel1 == "2"):
        payloads()
    elif(sel1 == "3"):
        exploit()
    elif(sel1 == "4"):
         exit()
    else:
        print("Invalid Option ")

def icmpparams():
    setIP()
    setICMP()

def payloads():
    

def exploit():
    print("Add Exploit Block here")

def setIP():
    dst = input("Enter Victim IP address")
    host = socket.gethostname()
    src = socket.gethostbyname(host)
    ipheader.set_ip_dst(dst)
    ipheader.set_ip_src(src)
    return(ipheader)

def setICMP():
    icmpheader.set_icmp_type(icmpheader.ICMP_ECHO)
    

def main():
    welcome()

if __name__ == "__main__":
    main()