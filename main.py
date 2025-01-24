import json

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

abbreviations = {
    "L": "HIT_LIGHT",
    "M": "HIT_MEDIUM",
    "H": "HIT_HARD",
    "D": "DRAW",
    "P": "PUNCH",
    "B": "BEND",
    "U": "UPSET",
    "S": "SHRINK"
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

def full_calculate(target, final_moves):
    new_target = target
    for i in final_moves:
        i = i.upper()
        if(i == "HIT"):
            new_target -= buttons["HIT_LIGHT"]
        else:
            new_target -= buttons[i]


    moves = calculate(new_target)

    return prettify_moves(moves)

def sum_abbreviated_moves(abbr):
    sum = 0
    for i in abbr:
        i = i.upper()
        sum += buttons[abbreviations[i]]
    return sum


def main():
    while(1):
        command = input(">").split(" ")
        
        if(command[0] == "solve"):
            
            if(command[1] == "item"):
                pass
            else:
                target = int(command[1])
                final_moves = command[2:]
                print(full_calculate(target, final_moves))

        elif(command[0] == "calc"):
            print(sum_abbreviated_moves(command[1]))


    full_calculate(70, ["BEND", "DRAW", "DRAW"])
    

z
if(__name__ == "__main__"):
    main()
