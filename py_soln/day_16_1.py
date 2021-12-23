from functools import reduce

class Packet:
    def __init__(self, raw, sub_packets):
        self.raw = raw
        self.sub_packets = sub_packets

    def version(self):
        return int(self.raw[:3], 2)

    def aggregated_version(self):
        return self.version() + sum(p.aggregated_version() for p in self.sub_packets)

    def evaluate(self):
        pkt_type = int(self.raw[3:6], 2)
        if pkt_type == 0:
            return sum(self.evaluate_all())
        elif pkt_type == 1:
            return reduce(lambda a, b: a * b, self.evaluate_all(), 1)
        elif pkt_type == 2:
            return min(self.evaluate_all())
        elif pkt_type == 3:
            return max(self.evaluate_all())
        elif pkt_type == 4:
            parts = process_literal(6, self.raw)
            return int("".join(parts), 2)
        # always two sub packets
        elif pkt_type == 5:
            first, second = self.evaluate_all()
            return first > second
        elif pkt_type == 6:
            first, second = self.evaluate_all()
            return first < second
        elif pkt_type == 7:
            first, second = self.evaluate_all()
            return first == second
        else:
            raise Exception("Unknown Packet Type")

    def evaluate_all(self):
        for p in self.sub_packets:
            yield p.evaluate()


def process_literal(pointer, contents):
    parts = []
    while True:
        word = contents[pointer : pointer + 5]
        parts.append(word[1:])
        if word[0] == "0":
            break
        pointer += 5
    return parts


def parse_packet(pointer, packet):
    if pointer >= len(packet):
        raise Exception()
    initial = pointer
    type_id = packet[pointer + 3 : pointer + 6]

    sub_packets = []
    # Literal
    if int(type_id, 2) == 4:
        pointer += 6
        parts = process_literal(pointer, packet)
        pointer += 5 * len(parts)
    # Operator
    else:
        pointer += 6
        length_type = packet[pointer : pointer + 1]
        pointer += 1
        if length_type == "0":
            length_in_bits = int(packet[pointer : pointer + 15], 2)
            pointer += 15
            end_pointer = pointer + length_in_bits
            while pointer < end_pointer:
                next_packet = parse_packet(pointer, packet)
                pointer += len(next_packet.raw)
                sub_packets.append(next_packet)
        else:
            number_of_packets = int(packet[pointer : pointer + 11], 2)
            pointer += 11

            end_count = len(sub_packets) + number_of_packets
            while len(sub_packets) < end_count:
                next_packet = parse_packet(pointer, packet)
                pointer += len(next_packet.raw)
                sub_packets.append(next_packet)

    return Packet(packet[initial:pointer], sub_packets)

with open('../inputs/day_16_input.txt') as f:
    lines = f.readlines()

    hex_str = lines[0].strip()

    hex_map = {
        '0' : '0000',
        '1' : '0001',
        '2' : '0010',
        '3' : '0011',
        '4' : '0100',
        '5' : '0101',
        '6' : '0110',
        '7' : '0111',
        '8' : '1000',
        '9' : '1001',
        'A' : '1010',
        'B' : '1011',
        'C' : '1100',
        'D' : '1101',
        'E' : '1110',
        'F' : '1111'
    }

    binary_str = ''
    for c in list(hex_str):
        binary_str += hex_map[c]


    packet = parse_packet(0, binary_str)
    print(packet.aggregated_version())
    print(packet.evaluate())

