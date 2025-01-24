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

    ["PUNCH", "HIT_MEDIUM", "BEND"], #3
    ["BEND", "HIT_LIGHT"], #4
    
    ["PUNCH", "PUNCH", "HIT_MEDIUM", "BEND"], #5
    ["PUNCH", "PUNCH", "PUNCH"], #6
    
    ["BEND"], #7
    ["BEND", "BEND", "HIT_MEDIUM"], #8

    ["BEND", "PUNCH"], #9
    ["UPSET", "HIT_LIGHT"], #10

    ["UPSET", "HIT_HARD", "BEND"], #11
    ["UPSET", "HIT_LIGHT", "PUNCH"], #12

    ["UPSET"], #13
    ["BEND", "BEND"], #14

    ["UPSET", "PUNCH"], #15
    ["SHRINK"], #16

]

def verify_shortcuts():
    for index, i in enumerate(hit_shortcuts):
        sum = 0
        for j in i:
            sum += buttons[j]
        if(sum != index):
            print("FAILED", index, i, "(got "+str(sum)+")")


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
    verify_shortcuts()
    while(1):
        command = input(">").split(" ")
        
        if(command[0] == "solve"):
            
            if(command[1] == "item"):
                with open("tool_dict.json", "r") as f:
                    j = json.loads(f.read())
                    print(full_calculate(j[command[2]]["work"], j[command[2]]["last_hits"]))
            else:
                target = int(command[1])
                final_moves = command[2:]
                print(full_calculate(target, final_moves))

        elif(command[0] == "calc"):
            print(sum_abbreviated_moves(command[1]))

        elif(command[0] == "save"):
            j = {}
            with open("tool_dict.json", "r") as f:
                j  = json.loads(f.read())

            j[command[1]] = {
                "work": int(command[2]),
                "last_hits": command[3:]
            }

            with open("tool_dict.json", "w") as f:
                f.write(json.dumps(j))


    full_calculate(70, ["BEND", "DRAW", "DRAW"])
    

if(__name__ == "__main__"):
    main()
