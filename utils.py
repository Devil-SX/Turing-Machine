from turing_machine import *

move_dic = {
    "l": "LEFT",
    "r": "RIGHT",
    "": "STAY",
    "s": "STOP",
    "e": "ERROR"
}


write_dic = {
    "0": "CLEAN",
    "1": "WRITE"
}

def load_machine(file_path:str) -> TuringMachine:
    global move_dic, write_dic
    turing_machine = TuringMachine()

    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i in range(1,len(lines)): # 跳过第一行
            line = lines[i]
            l = line.strip().split(',')
            # State,NextState0,Action0,Move0,NextState1,Action1,Move1
            this = int(l[0])
            next0 = int(l[1])
            actw0 = Write_Action[write_dic[l[2]]]
            actm0 = Move_Action[move_dic[l[3]]]
            next1 = int(l[4])
            actw1 = Write_Action[write_dic[l[5]]]
            actm1 = Move_Action[move_dic[l[6]]]
            status = Status(this, actm0, actw0, next0, actm1, actw1, next1)
            turing_machine.add_status(status)

    return turing_machine

def load_tape(file_path:str) -> list:
    with open(file_path, 'r') as file:
        content = file.read()

    binary_list = [int(char) for char in content]

    return binary_list