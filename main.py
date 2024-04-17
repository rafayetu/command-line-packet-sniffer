#!/usr/bin/python

from modules import messages, sniffer


def print_packets(_packets, _range1, _range2):
    for n in range(_range1, _range2 + 1):
        p = _packets[n]
        p.get_packet_info()


if __name__ == '__main__':
    msg = messages.MessageBox()
    ps = sniffer.PacketSniffer()

    choice = msg.ask_choice("PrimaryChoice")
    if choice == 1:
        # file_name		=	msg.get_input("FileName")
        packet_number = msg.get_number("PacketNumber")

        packets = ps.capture_packets(packet_number)

        choice_2 = msg.ask_choice("SecondChoice")

        if choice_2 == 1:
            while True:
                choice_3 = msg.ask_choice("ThirdChoice")
                range1, range2 = 1, packet_number
                if choice_3 == 0:
                    break
                elif choice_3 == 3:
                    ranges = msg.get_range("Range", packet_number)
                    range1, range2 = min(ranges), max(ranges)
                elif choice_3 == 2:
                    range2 = msg.get_number("Packet", packet_number)
                    range1 = range2

                print_packets(packets, range1, range2)
        elif choice_2 == 0:
            pass
