with open('day13/input1', 'r') as file_handle:
    packets = [eval(p)
               for p in file_handle.read().strip().split('\n')
               if len(p) > 0]

packets.extend([[[2]], [[6]]])

def unpack_list(l):
    if len(l) > 0:
        if type(l[0]) == list:
            return unpack_list(l[0])
    return l

def compare(left, right):
    # print(f"Comparing {left} and {right}")
    match [left, right]:
        case [[], _]: return True
        case [_, []]: return False
        case [[int(i)], [int(j)]] if i == j: return "tie"
        case [[int(i), *ll], [int(j), *rr]] if i == j: return compare(ll, rr)
        case [[int(i), *ll], [int(j), *rr]]: return i < j
        case ([[int(l), *ll], [list(r), *rr]] | 
              [[list(l), *ll], [int(r), *rr]] |
              [[list(l), *ll], [list(r), *rr]]):
            l = [l] if type(l) == int else l
            r = [r] if type(r) == int else r
            listcompare = compare(l, r)
            return compare(ll, rr) if listcompare == 'tie' else listcompare             

ordered_packets = [packets[0]]
for packet in packets[1:]:
    pos = -1
    for i in range(len(ordered_packets)):
        other_packet = ordered_packets[i]
        if compare(packet, other_packet):
            pos = i
            break
    if pos > -1:
        ordered_packets = ordered_packets[:pos] + [packet] + ordered_packets[pos:]
    else:
        ordered_packets.append(packet)


div1 = ordered_packets.index([[2]]) + 1
div2 = ordered_packets.index([[6]]) + 1
print(div1 * div2)
    