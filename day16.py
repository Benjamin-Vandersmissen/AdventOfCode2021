hex_data = open("day16").read()

hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9':'1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D' : '1101', 'E': '1110', 'F': '1111'}

bin_data = ""
for hex in hex_data:
    bin_data += hex_to_bin[hex]
all_version_numbers = 0


def bin_to_int(bin):
    dec = 0
    for i in range(len(bin)-1, -1,-1):
        if bin[i] == '1':
            dec += pow(2, (len(bin) - 1)-i)

    return dec


class Packet:
    def __init__(self, packet_number, packet_type):
        global all_version_numbers
        self.packet_number = bin_to_int(packet_number)
        all_version_numbers += self.packet_number
        self.packet_type = bin_to_int(packet_type)
        self.sub_packets = []
        self.number_data = 0

    def process(self):
        global bin_data
        number_data = ''
        if self.packet_type == 4:
            while True:
                temp = bin_data[:5]
                number_data += temp[1:]
                if bin_data[0] == '0':
                    bin_data = bin_data[5:]
                    break
                bin_data = bin_data[5:]
            self.number_data = bin_to_int(number_data)

        else:
            length_type = bin_data[0]
            bin_data = bin_data[1:]
            if length_type == '0':
                bit_length = bin_to_int(bin_data[:15])
                bin_data = bin_data[15:]
                original_length = len(bin_data)
                while original_length - len(bin_data) < bit_length:
                    self.sub_packets.append(create_packet())

            else:
                nr_packets = bin_to_int(bin_data[:11])
                bin_data = bin_data[11:]
                for i in range(nr_packets):
                    self.sub_packets.append(create_packet())


def create_packet():
    global bin_data
    packet_number = bin_data[:3]
    bin_data = bin_data[3:]
    packet_type = bin_data[:3]
    bin_data = bin_data[3:]
    packet = Packet(packet_number, packet_type)
    packet.process()
    return packet


def calculate(packet):
    if len(packet.sub_packets) == 0:
        return packet.number_data
    else:
        values = []
        for sub_packet in packet.sub_packets:
            if sub_packet.packet_type == 4:
                values.append(sub_packet.number_data)
            else:
                values.append(calculate(sub_packet))

        if packet.packet_type == 0:
            return sum(values)
        if packet.packet_type == 1:
            retval = 1
            for val in values:
                retval *= val
            return retval
        if packet.packet_type == 2:
            return min(values)
        if packet.packet_type == 3:
            return max(values)
        if packet.packet_type == 5:
            return values[0] > values[1]
        if packet.packet_type == 6:
            return values[0] < values[1]
        if packet.packet_type == 7:
            return values[0] == values[1]


packet = create_packet()


def day16_1():
    print(all_version_numbers)


def day16_2():
    print(calculate(packet))


day16_2()