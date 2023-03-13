

with open('day13/input1', 'r') as file_handle:
    pairs = [list(map(eval, p.split('\n'))) 
             for p in file_handle.read().strip().split('\n\n')]

def unpack_list(l):
    if len(l) > 0:
        if type(l[0]) == list:
            return unpack_list(l[0])
    return l

# def compare(left, right):
#     print(f"Comparing {left} and {right}")
#     match [left, right]:
#         case [[], [*rest]]: print("Left empty"); return 1
#         case [[*rest], []]: print("Right empty"); return -1
#         case [[int(i)], [int(j)]] if i == j: return "tie"
#         case [[int(i), *ll], [int(j), *rr]] if i == j: return compare(ll, rr)
#         case [[int(i), *ll], [int(j), *rr]]: print(f"{i} < {j} = {i < j}"); return i < j
#         case [[int(i), *ll], [list(r), *rr]]:
#             inner_result = compare([i], r)
#             return inner_result if inner_result != "tie" else compare(ll, rr)
#         case [[list(l), *ll], [int(j), *rr]]:
#             inner_result = compare(l, [j])
#             return inner_result if inner_result != "tie" else compare(ll, rr)             
#         case [[list(l), *ll], [list(r), *rr]]:
#             inner_result = compare(l, r)
#             return inner_result if inner_result != "tie" else compare(ll, rr) 

def compare(left, right):
    print(f"Comparing {left} and {right}")
    match [left, right]:
        case [[], _]: print("left list empty"); return True
        case [_, []]: print("right list empty"); return False
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

i = 1
right_orders = []
for pair in pairs:
    if compare(*pair):
        print(f"Pair {i} is in the right order!")
        right_orders.append(i)
    else:
        print(f"Pair {i} is not in the right order!")
    i += 1

print(right_orders)
print(sum(right_orders))
    