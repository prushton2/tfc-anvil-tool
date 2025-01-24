buttons = {
    "HIT_LIGHT"  : -3,
    "HIT_MEDIUM" : -6,
    "HIT_HARD"   : -9,
    "DRAW"       :-15,

    "PUNCH"      :  2,
    "BEND"       :  7,
    "UPSET"      : 13,
    "SHRINK"     : 16
}

# Really dont know how to do these kind of algs, so im kinda brute forcing here

hit_shortcuts = [
    [],
    ["HIT_MEDIUM", "BEND"], #1
    ["PUNCH"], #2

    ["PUNCH"], #3
    ["UPSET", "SHRINK"], #4
    
    ["PUNCH"], #5
    ["PUNCH"], #6
    
    ["BEND"], #7
    ["BEND", "BEND", "HIT_MEDIUM"], #8

    ["BEND", "PUNCH"], #9
    ["UPSET", "HIT_LIGHT"], #10

    ["UPSET", "HIT_HARD", "BEND"], #11
    ["DRAW", "SHRINK", "UPSET"], #12

    ["UPSET"], #13
    ["BEND", "BEND"], #14

    ["UPSET", "PUNCH"], #15
    ["SHRINK"], #16

]

def calculate(target):
    accumulator = 0
    moves = []

    while (accumulator != target):

        delta = target - accumulator
        
        if (delta > 16):
            accumulator += 16
            moves.append("SHRINK")
        
        else:
            shortcut = hit_shortcuts[delta]
            
            for i in shortcut:
                moves.append(i)
                accumulator += buttons[i]

    return moves



def prettify_moves(moves):
    output = ""
    previous = ""
    number = 1
    for i in moves:
        if(i == previous):
            number += 1
            continue
        
        if(previous != ""):
            output += previous + " x" + str(number) + "\n"
            number = 1
        previous = i

    output += previous + " x" + str(number)
    
    return output

def main():
    target = 70
    final_moves = ["DRAW", "DRAW", "BEND"]

    new_target = target
    for i in final_moves:
        if(i == "HIT"):
            new_target -= buttons["HIT_LIGHT"]
        else:
            new_target -= buttons[i]


    moves = calculate(new_target)

    print(prettify_moves(moves))


if(__name__ == "__main__"):
    main()