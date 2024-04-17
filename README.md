# A Network Packet Monitoring Tool - Packet Sniffing using Python

To run the program do the following from terminal:
	1. Go to root mode
		-> $ sudo su -
		-> Then enter your password
	2. Then change the directory where the programm files are stored
		-> $ cd Directory/../../
	3. Run the python file
		-> $ python main.py build
	4. Choice option will come
		-> Options:
			1. Capture packets and analyze it
			->> Selecting option '1' will ask you for a the number of packets you want to capture or analyze. Then capturing will start.
			->> If you choose option '1' it will give you another list of options after capturing data. 
				->> Options:
						1. Print details of packets
						0. Exit
						->>> Selecting option '1' will give you another list of options.
						->>> Options:
							1. Print details of all packets
							2. Print details of a specific packet
							3. Print details of all packets in range
							0. Exit from option '1'

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
