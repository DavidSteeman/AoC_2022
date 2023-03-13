datatype item = Int of int
		      | IntList of item list


val pair = IntList [Int 6, IntList [Int 7, IntList []], IntList [Int 9], Int 1]

fun sum (ls) =
    case ls of
        IntList []      => 0 
      | IntList l::ls'  => case l of 
                                Int i       => i + sum(ls')
                              | IntList lst => sum(lst) + sum(ls')

val ans = sum(pair)
(* 
fun sum (ls) = 
    case ls of
        []      => 0
      | l::ls'  => l + sum(ls')

val ans = sum([1, 4, 5, 6, 7, 1]) *)

