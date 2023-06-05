from enum import Enum

class Write_Action(Enum):
  '''
  Turing Machine executes 3 write actions: write 0, write 1, dont change
  '''
  CLEAN = 0
  WRITE = 1


class Move_Action(Enum):
  '''
  Turing Machine executes 4 move actions: left, right, none and exit 
  '''
  LEFT = 0
  RIGHT = 1
  STAY = 2
  STOP = 3
  ERROR = 4


class Status:
  def __init__(self,  
               this:int,  
               actm0:Move_Action,
               actw0:Write_Action,
               next0:int, 
               actm1:Move_Action, 
               actw1:Write_Action,
               next1:int):
    self.status_number = this
    self.actionw0 = actw0 
    self.actionm0 = actm0
    self.next_status0 = next0
    self.actionw1 = actw1
    self.actionm1 = actm1
    self.next_status1 = next1


class TuringMachine:
  def __init__(self):
    self.head = 0
    self.tape = []
    self.status = 0
    self.table = {}

  def set_tape(self, tape:list):
    self.tape = tape

  def add_status(self, new_status:Status):
    self.table[new_status.status_number] = new_status

  def calculate(self):
    while True:
      read = self.tape[self.head]
      if read:
          next_status = self.status.next_status1
          actionw = self.status.actionw1
          actionm = self.status.actionm1
      else:
          next_status = self.status.next_status0
          actionw = self.status.actionw0
          actionm = self.status.actionm0

      if actionw == Write_Action.CLEAN:
          self.tape[self.head] = 0
      elif actionw == Write_Action.WRITE:
          self.tape[self.head] = 1
      
      if actionm == Move_Action.LEFT:
          self.head -= 1
      elif actionm == Move_Action.RIGHT:
          self.head += 1
      elif actionm == Move_Action.STOP:
          break
      elif actionm == Move_Action.ERROR:
          print("ERROR")
          break

      self.status = self.table[next_status]
    

  def run(self):
    print(f"The input tape is \t{self.tape}")
    self.head = 0
    self.status = self.table[0]
    self.calculate()
    print(f"The output tape is \t{self.tape}")