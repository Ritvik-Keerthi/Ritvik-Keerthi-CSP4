# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
# imports from other .py files
# Main Menu
from week0 import swap
from week0 import matrix
from week0 import ship
from week1 import infodbloops
from week2 import fungame


main_menu = [
  
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu0 = [
    ["Serial Num", "week0/serialnum.py"],
    ["Tree", "week0/tree.py"],
    ["Ship", ship.shippy],
    ["Swap", swap.swapTester],
    ["Matrix", matrix.matrixTester2],
]

sub_menu1 = [
    ["InfoDBLists", "week1/infodblists.py"],
    ["InfoDBLoops", infodbloops.main],
    ["Fibonacci", "week1/fibonacci.py"]
]

sub_menu2 = [
    ["Factorial", "week2/factorial.py"],
    ["Math Imperative + OOP", "week2/math.py"],
    ["Extra Cred Palindrome", "week2/palindrome.py"],
    ["FunGame", fungame.fungame]
]

border = "=" * 25
banner = f"\n{border}\nChoose one of the options: \n{border}"


def menu():
    title = "Ritvik's Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0 Serial Num, Tree, Ship, Swap, Matrix", submenu0])
    menu_list.append(["Week 1 Lists, Loops, Fibonacci", submenu1])
    menu_list.append(["Week 2 Factorial, Math, Hangman", submenu2])
    buildMenu(title, menu_list)


def submenu0():
    title = "\nRitvik's Submenu" + banner
    buildMenu(title, sub_menu0)

def submenu1():
    title = "\nRitvik's Submenu" + banner
    buildMenu(title, sub_menu1)

def submenu2():
    title = "\nRitvik's Submenu" + banner
    buildMenu(title, sub_menu2)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()


