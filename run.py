from utils import load_machine
from utils import load_tape
from turing_machine import TuringMachine


if __name__ == "__main__":
    your_machine_path = "add.csv"
    your_tape_path = "tape.txt"

    turing_machine = load_machine(your_machine_path)
    turing_machine.set_tape(load_tape(your_tape_path))
    # turing_machine.set_tape([0, 1, 0, 1, 1, 1, 0, 0, 0, 0]) # or create type like this way
    turing_machine.run()
