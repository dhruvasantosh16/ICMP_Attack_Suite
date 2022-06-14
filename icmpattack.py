from encodings import utf_8
from impacket import ImpactDecoder
from impacket import ImpactPacket
import socket
ipheader = ImpactPacket.IP()
icmpheader = ImpactPacket.ICMP()
payload = "Standard Reverse Shell"

def welcome():
    #Dependency Check
    try: 
        from impacket import ImpactDecoder
    except ImportError:
        print("Impacket library is missing (Run", "pip install impacket)")
        exit(1)
    #Welcome Prompt
    print('\n', "Welcome to ICMP Attack Suite!", '\n', "ICMP Parameters", '\n', sep='\n')
    setICMP()

def payloads():
    print("Payload Selection", '\n', "1. Reverse Shell", "2. OS Fingerprinting", "3. Ping", "4. Back to Main Menu", '\n', sep='\n')
    pl = input("Selection: ")
    if (pl == "1"):
        print('\n', "Select OS", '\n', "1. POSIX System", "2. Windows System", '\n', sep='\n')
        plsel = input("Selection: ")
        if (plsel == "1"):
            print("Python Reverse Shell Command for Linux")
        elif (plsel == "2"):
            print("Python Reverse Shell Command for Windows")
        else:
            print("Invalid Option")
    else:
        print("Invalid Option")
    payload_b = bytes(payload, encoding="utf_8")
    icmpheader.contains(ImpactPacket.Data(payload_b))
    ipheader.contains(icmpheader)
    print(ipheader)

def exploit():
    

def setICMP():
    dst = input("Enter Victim IP address: ")
    print('\n')
    host = socket.gethostname()
    src = socket.gethostbyname(host)
    ipheader.set_ip_dst(dst)
    ipheader.set_ip_src(src)
    icmpheader.set_icmp_type(icmpheader.ICMP_ECHO)
    payloads()
    
def main():
    welcome()

if __name__ == "__main__":
    main()