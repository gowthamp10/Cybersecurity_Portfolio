# Activity performed as part of Gobuster:The Basics Room 

- **Pre-requisite** :
1. Start the attack box and the target machine.

- **Environment and Setup** :
1. Command: "sudo nano /etc/resolv-dnsmasq". To open up the file named resolv-dnsmasq.
2. Insert nameserver <TargetIP> as the firstline.
3. Save the file(Ctrl+O) and exit the editor(Ctrl+X).
4. Re-start Dnsmasq service using the command:"/etc/init.d/dnsmasq restart".

- **Use Case: Directory and File Enumeration** :
1. Run the command:"gobuster dir --help". To navigate to help page of gobusters for the dir option. Check out the flag used for skipping tls verification.
2. Run the command:"gobuster dir -u www.offensivetools.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt". Provides list of all avialable directories in the url.
3. Run the command:"gobuster dir -u www.offensivetools.thm/secret -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .js --timeout 30". Provides list of all files and directories available on the url.
4. curl command:"curl <URL>". Get the flag.

- **Use Case: Subdomain Enumeration** :
1. Run the command:"gobuster dns --help". To get the help page of dns enumeration using gobuster.
2. Run the command:"gobuster dns -d offensivetools.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt". To get the all possible subdomains which are configured.

- **Use Case: Vhost Enumeration** :
1. Run the command:"gobuster vhost -u "http://10.10.248.52" --domain example.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain | grep "Status: 200"". To get all the vhosts on the <Targetdomain> and are return status as 200.
