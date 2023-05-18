logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


dic = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    print(logo)
    n1 = float(input("what's the first number: "))
    game = True

    while game:
        # print([symbol for symbol in dic])
        for sym in dic:
            print(sym)
        symbl = input("pick on operation: ")
        n2 = float(input("what's the next number: "))

        fun = dic[symbl]

        Result = fun(n1, n2)
        print(f"{n1} {symbl} {n2} = {Result}")

        go_on = input(
            f"Type 'Y' to continue with {Result}, or 'S' to start new calculation, or 'N' to exit: "
        ).lower()

        if go_on == "y":
            # If 'Y', start the calculation with previous result.
            n1 = Result
            game = True
        elif go_on == "s":
            # If 'S', start the new calculation.
            game = True
            calculator()
        else:
            game = False


calculator()
