# Activity performed as part of Network Core Protocols Room

- **Pre-requesite** :
1. Start the machine provided for the room.

- **Tool Overview** :
1. Open Exercise.pcapng file in Wireshark.
2. Navigate to Statistics --> Capture File Properties to get details on the pcapng file.
3. Utilze the details to answer the questions on this section.

- **Packet Dissection** :
1. Open Exercise.pcapng file in Wireshark.
2. Utilize the goto option and navigate to packet number 38.
3. Check the name of the markup language after the HTTP layer(Application Layer) and markup language is mentioned in Application Data layer.
4. Check the Application Layer details for arrival date.
5. Check IP layer for TTL.
6. Check IP layer for payload size.
7. Check Application layer for e-Tag.

- **Packet Navigation** :
1. Open Exercise.pcapng file in Wireshark.
2. Using Find option, search for the string provided and check the artist 1 name.
3. Upon navigating to the packet 12's packet comments, we get to know its just a diversion. So, upon checking the Comments available in the file details and performing the task we can get the hash value.
4. Using the Fing option, search for the string specified and download file from the pcapng file using Export object option.
5. Naviagte to Analyze -> Expert Information and you can get number of warning packets.

- **Packet Filtering** :
1. Open Exercise.pcapng file in Wireshark.
2. Checkout the Protocol used as part of packet 4.
3. Upon filtering based on protocol the number of packets available to analyze.
4. Go to the packet number 33790, and check the stream data and consolidate the number of artists.
5. Using the same packet data find the artist 2 name.

