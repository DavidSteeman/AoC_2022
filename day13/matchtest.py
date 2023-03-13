from math import inf

def mc(l, r):
    print(f"Matching {l} and {r}")
    match l, r:
        case [[], x]: print("left empty")
        case [x, []]: print("right empty") 
        case [[int(i), *lr], [int(j), *rr]]: print(f"{i} <= {j} : {i <= j}"); mc(lr, rr)
        case [[int(i), *lr], [[], *rr]]: print("Right list empty."); mc(lr, rr)
        case [[int(i), *lr], [list(l), *rr]]: mc([i], l); mc(lr, rr)
        case [[], *lr], [int(j), *rr]: print("Left list empty"); mc(lr, rr)
        case [list(l), *lr], [int(j), *rr]: mc(l, [j]); mc(lr, rr)
        
mc([1, 2, 3, 5], [6, 2, [1], []])