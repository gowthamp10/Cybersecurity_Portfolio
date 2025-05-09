# Activity performed as part of Tcpdump: The Basics Room

- **Filtering** :
1. In order to filter packet capture of only icmp protocol. We can use command: tcpdump -r <filename> icmp | wc
2. In order to get the first 5 packets we can use the command: tcpdump -r <filename> -c 5 -n
here -c -> count, -n -> don't resolve IP
3. In order to get the IP address of the host that asked for the MAC address of 192.168.124.137. We can use command: tcpdump -r <filename> arp

- **Advanced Filtering** :
1. In order to get the number of packets having RST flag set we use the command: tcpdump -r <filename> "tcp[tcpflags] == tcp-rst" | wc
2. In order to get the IP address of the host which has sent data of length more than 15000 we can use the command: tcpdump -r <filename> -n greater 15000

- **Displaying Packets** :
1. In order to get the MAC address of the ARP request initiated by the host. We can use the command: tcpdump -r <filename> -e -q arp

