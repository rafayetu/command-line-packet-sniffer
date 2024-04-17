# A Network Packet Monitoring Tool - Packet Sniffing using Python

# Running the Program

To run the program, follow these steps from your terminal:

1. **Enter Root Mode:**
   - Switch to root mode by running:
     ```
     $ sudo su -
     ```
   - Then enter your password.

2. **Change Directory:**
   - Navigate to the directory where the program files are stored:
     ```
     $ cd ~/command-line-packet-sniffer
     ```

3. **Run the Python File:**
   - Execute the main program file:
     ```
     $ python main.py
     ```

4. **Choose an Option:**
   - After running the script, you will see a menu of options:
     ```
     Options:
     1. Capture packets and analyze it
     ```
   - Selecting option '1' will prompt you to enter the number of packets you want to capture or analyze. The capturing will then start.
   - If you choose option '1', it will provide another list of options after capturing data:
     ```
     Options:
     1. Print details of packets
     0. Exit
     ```
     - Selecting option '1' here will present further choices:
       ```
       Options:
       1. Print details of all packets
       2. Print details of a specific packet
       3. Print details of all packets in range
       0. Exit from option '1'
       ```


# Program Features:
	1. It can handle this protocols:
		Data Link Layer:	Ethernet
		Network Layer:		IPV4					[It can identify all the protocols given here but it can only give information of IPV4 protocol]
		Transport Layer:	TCP,UDP,ICMP			[It can identify all the protocols given here but it can only give information of TCP, UDP, ICMP protocol]
	2. It can print almost all the information of an packet.

# Code properties:
	1. It contains a11 source files.
	2. Python File:
		main.py 		:	It contains the main function where the program starts from.
		sniffer.py 		:	It contains PacketSniffer (Captures packets) and Packet (Every packet works as Packet object instances) object class.
		messages.py 	:	It contains MessageBox object class which handles all display messages related tasks.
		converter.py 	: 	It contains commonly used basic function tools
		data_link.py 	: 	It contains Data Link Layer protocol object classes (Ethernet)
		network.py 		: 	It contains Network Layer protocol object classes (IPv4)
		transport.py 	: 	It contains Transport Layer protocol object classes (TCP, UDP, ICMP)
	3. Executable File:
		main.py

# Dependencies
	1. Operating System : Ubuntu, Linux
	2. Platform : Python
	3. Libraries/Modules: socket, sys, struct		[all of these are built in modules of python] 
	4. Internet connection or Lan connection.

