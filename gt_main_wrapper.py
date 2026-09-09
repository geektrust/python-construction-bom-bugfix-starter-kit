import sys
from main import Main


def call_main():
    """
    ***********************************************
    * This is the driver code. Don't change it!!!
    * *********************************************

    Format of the 'args' array: `<Input array> | <Target>`
    Example: ["2, 7, 11, 15 | 9"]

    The code evaluator will execute this code by using the command:
    python main.py "2, 7, 11, 15 | 9"

    So the value of the variable 'input' will be the string: "2, 7, 11, 15 | 9"
    """
    if len(sys.argv) < 2:
        raise ValueError("No command line arguments passed")

    commands = sys.argv[1:]
    main = Main()

    for command in commands:
        main.handle(command)


if __name__ == "__main__":
    call_main()
