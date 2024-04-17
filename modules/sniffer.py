import socket
from protocols.data_link import *
from protocols.network import *
from protocols.transport import *
from messages import MessageBox

valid_protocols = ['TCP', 'UDP', 'ICMP']


class PacketSniffer(object):
    def __init__(self):
        super(PacketSniffer, self).__init__()
        self.conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        self.buff_size = 65535  # 2^16=65536
        self.msg = MessageBox()

    def capture_packets(self, max_packet):
        packets = {}
        self.msg.basic_info()
        packet_no = 1

        while packet_no <= max_packet:
            bytes_data, addr = self.conn.recvfrom(self.buff_size)
            packet = Packet(bytes_data, packet_no, self.msg)
            packets[packet_no] = packet
            if packet.ethernet.proto_title == 'EGP':
                packet_no += 1
        return packets


class Packet(object):
    """docstring for Packet"""

    def __init__(self, bytes_data, packet_no, msg):
        super(Packet, self).__init__()
        self.bytes_data = bytes_data
        self.packet_no = packet_no
        self.msg = msg
        self.ethernet = Ethernet(bytes_data)
        if self.ethernet.proto_title == 'EGP':
            self.ip = IPv4(self.ethernet.data)
            self.msg.basic_info(
                (self.packet_no, self.ip.proto_title, self.ip.src_ip, self.ip.target_ip, len(self.ip.data)))
            if self.ip.proto_title in valid_protocols:
                self.transport = self.get_transport(self.ip)

    @staticmethod
    def get_transport(ip):
        if ip.proto_title == 'TCP':
            return TCP(ip.data)
        elif ip.proto_title == 'UDP':
            return UDP(ip.data)
        elif ip.proto_title == 'ICMP':
            return ICMP(ip.data)

    def get_packet_info(self):
        packet_header = self.msg.headers['Packet'].format(self.packet_no)
        ethernet_msg = self.msg.headers['ETH'] % self.ethernet.msg_format
        ipv4_msg = self.msg.headers['IPv4'] % self.ip.msg_format

        if self.ip.proto_title in valid_protocols:

            transport_msg = self.msg.headers[self.ip.proto_title] % self.transport.msg_format

            print(packet_header + ethernet_msg + ipv4_msg + transport_msg)

        else:
            print(packet_header + ethernet_msg)
