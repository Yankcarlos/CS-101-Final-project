import random
#to clear the terminal  
import os
class board:
  def __init__(self):
   self.hits = 16
   self.scount = 0
   self.board = []
   self.rows_cols = {'row':[],'col':[]}
   self.win = False
   self.create_board()
  count = 0

  def create_board(self):
   cords_C = [' A',' B',' C',' D',' E',' F',' G',' H',' I',' J']
   for i in range(11):
       row = []
       for j in range(11):
           row.append('🟦')
       self.board.append(row)
   self.board[0][1:11] = cords_C
   for n in range(11):
     ns = str(n)
     self.board[n][0] = ns + ' '
     self.board[10][0] = '10'
         
  def show_board(self):
      for row in self.board:
          for item in row:
              print(item, end=" ")
          print()
              
  def place_ships(self,ship,row,col,dir):
   count = {"Carrier":0,"Battleship":1,"Destroyer":2,"Submarine":2,"Patrol boat":3,}
   #place ships horizontaly and make sure ships won't overlap  
   if dir == 'H':  
    try:
        while count[ship] < 5:
         count[ship] += 1
         while col < 1:
           col += 1
         while self.board[row][col] == '🟩':
          col += 1
         else:
          self.board[row][col] = '🟩'
          col -= 1
    except:
         while count[ship] < 5:
          count[ship] += 1
          while col > 10:
            col -= 1
          while self.board[row][col] == '🟩':
           col -= 1
          else:
           self.board[row][col] = '🟩'
           col += 1
    #place ships virtacly and make sure ships wont overlap
   elif dir == 'V': 
    try:
     while count[ship]  < 5:
        count[ship] += 1
        while row < 1:
          row += 1
        while self.board[row][col] == '🟩':
         row += 1
        else:
          self.board[row][col] = '🟩'
          row -= 1
    except:
        while count[ship] < 5:
         count[ship] += 1
         while row > 10:
          row -= 1
         while self.board[row][col] == '🟩':
          row -= 1
         else:
          self.board[row][col] = '🟩'
          row -= 1     
          
  #places computers ships and makes sure it doesent cause an Error        
  def cp_place(self):
   row = random.randint(1,10) 
   col = random.randint(1,10) 
   rdir = random.randint(1,2)
   if rdir == 1:
     dir = 'H'
     #only blocks rows for horizantal placements 
     self.rows_cols['row'].append(row)
   else:
     dir = 'V'
     #only blocks coloms for vertical placements 
     self.rows_cols['col'].append(col)  
  #checks for duplicates in the list of row and col placements and makes sure there arent any
   myset = {"rows":set(self.rows_cols['row']),"cols":set(self.rows_cols['col'])}
   if len(self.rows_cols['row']) == len(myset['rows']) and dir == 'H' or len(self.rows_cols['col']) == len(myset['cols']) and dir == 'V':  
    cp.place_ships(ships,row,col,dir)
    cp_board_copy.place_ships(ships,row,col,dir)  
   else:
    #removes the duplicate and calls the function again so that the code countinues to run
     try: 
      self.rows_cols['row'],['col'].pop(row,col)
     except:
      self.cp_place() 
             
  #checks if you have or havent hit that spot already and counts the hits from the player and computer
  def attack(self,row,col):
   if self == player_1 and cp.board[row][col] == '🟥' or cp.board[row][col] == '⬜':
       print('You already hit that spot') 
       self.loop()
   elif self == cp and player_1.board[row][col] == '🟥' or player_1.board[row][col] == '⬜':
      self.loop()
   else:
    if self == player_1:
     if cp.board[row][col] == '🟩':
       cp.board[row][col] = '🟥'
       cp_board_copy.board[row][col] = '🟥'
       self.hits += 1
       self.switch()
     elif cp.board[row][col]  == '🟦':
       cp.board[row][col] = '⬜'
       cp_board_copy.board[row][col] = '⬜'
       self.switch()
    else:
      if player_1.board[row][col] == '🟩':
       player_1.board[row][col] = '🟥'
       self.hits += 1
       self.switch()
      elif player_1.board[row][col]  == '🟦':
       player_1.board[row][col] = '⬜'
       self.switch()
   
  #Hides the enemys ships on the fake board 
  def hide(self):
   crow = -1
   for row in self.board:
    crow += 1
    ccol = 0
    for item in row: 
      if item == '🟩': 
        self.board[crow][ccol] = '🟦'
        ccol += 1
      else:
        ccol += 1
   print('Enemy board')
   self.show_board()
        
  def wins(self):
   if self.hits == 17:
    self.win = True
  
  def changing_ships(self):
   global ships
   self.scount += 1
   if self.scount == 1:
      ships = "Carrier"
   elif self.scount == 2:
      ships = "Battleship"
   elif self.scount == 3:
      ships = "Destroyer"
   elif self.scount == 4:
      ships = "Submarine"
   else:
      ships = "Patrol boat"
  
  def switch(self): 
   board.count += 1
   if self == cp:
     self = player_1
   else:
     self = cp
   if board.count == 1:
     self.place_ship()
   else:
     self.loop()
     
  def start(self):
      os.system('cls')
      print('''        
   B B B B        A       T T T T T   T T T T T   L          E E E E E     S S S S   H       H    I    P P P P     S S S S 
  B       B     A   A         T           T       L          E           S           H       H    I    P       P  S
  B       B   A       A       T           T       L          E           S           H       H    I    P       P  S
  B B B B     A A A A A       T           T       L          E E E         S S S     H H H H H    I    P P P P      S S S
  B       B   A       A       T           T       L          E                   S   H       H    I    P                  S
  B       B   A       A       T           T       L          E                   S   H       H    I    P                  S
  B B B B     A       A       T           T       L L L L L  E E E E E   S S S S     H       H    I    P          S S S S 
  ''')
      s = input('Type Y to start or N to cancel: ') 
      s = s.upper()
      if s == 'Y':
       self.place_ship()
      elif s == 'N':
        pass
      else:
        print('You didnt type one of the options')
        self.start()
        
  def place_ship(self):
   cords = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
   if self == player_1:
    for s in range(5):
      self.changing_ships()
      os.system('cls')
      self.show_board()
      #row choice
      row = input('What row would you like to place the ' + ships + ' 1-10: ')
      while row.isdigit() == False:
        print('You didnt type a number between 1 and 10')
        row = input('What row would you like to place the ' + ships + ' 1-10: ')
      else:
        row = int(row)
        while row > 10 or row < 1:
         row = input('What row would you like to place the ' + ships + ' 1-10: ')
         while row.isdigit() == False:
          print('You didnt type a number between 1 and 10')
          row = input('What row would you like to place the ' + ships + ' 1-10: ')
         else:
          row = int(row)
        else:
        #col choice
          Cchoice = input('What colom would you like to place ' + ships + " A-J: ")
          Cchoice = Cchoice.upper()
          while Cchoice not in cords:
            print('You didnt type one of the letters ')
            Cchoice = input('What colom would you like to place ' + ships + " A-J: ")
            Cchoice = Cchoice.upper()
          else:
           col = cords[Cchoice]
        #dir choice
           dir = input('What direction would you like to place the ship horizontally or vertically type V or H: ')
           dir = dir.upper()
           while dir != 'V' and dir != 'H':
            print('You didnt put in a correct direction type either V OR H' )
            dir = input('What direction would you like to place the ship horizontally or vertically type V or H: ')
            dir = dir.upper()
           else:
            self.place_ships(ships,row,col,dir)
    self.switch()
   #starts the loop for the computer to place its ships
   else:
    for sc in range(5):
     self.changing_ships()
     self.cp_place()
    self.switch()
       
  def loop(self):
   cords = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10}
   self.wins()
   if self == player_1 and player_1.win == False:
    os.system('cls')
    print('Your board')
    player_1.show_board()
    cp_board_copy.hide()
    row = input('What row would you like to attack the 1-10: ')
    while row.isdigit() == False:
      print('You didnt type a number between 1 and 10')
      row = input('What row would you like to attack the 1-10: ')
    else:
      row = int(row)
      while row > 10 or row < 1:
       row = input('What row would you like to attack the 1-10: ')
       while row.isdigit() == False:
        print('You didnt type a number between 1 and 10')
        row = input('What row would you like to attack the 1-10: ')
       else:
        row = int(row)
      else:
        Cchoice = input('What colom would you like to attack A-J: ')
        Cchoice = Cchoice.upper()
        while Cchoice not in cords:
          print('You didnt type one of the letters ')
          Cchoice = input('What colom would you like to attack A-J: ')
          Cchoice = Cchoice.upper()
        else:
         col = cords[Cchoice]
         self.attack(row,col)
    #The computer for attacking very simple could be improved 
   elif self == cp and cp.win == False :
      row = random.randint(1,10) 
      col = random.randint(1,10) 
      self.attack(row,col) 
   else:
     if player_1.win == True:
      os.system('cls')
      print('You won')
      print('Your board')
      player_1.show_board()
      print('enemy board')
      cp.show_board()
      #play again option
      rs = input('Do you want play agian type Y or N: ')
      rs = rs.upper()
      if rs == 'Y':
       player_1.restart()
      elif rs == 'N':
        pass
     else:
      os.system('cls')
      print('You lost')
      print('Your board')
      player_1.show_board()
      print('Enemy board')
      cp.show_board()
      #play again option
      rs = input('Do you want try agian type Y or N: ')
      rs = rs.upper()
      if rs == 'Y':
       player_1.restart()
      elif rs == 'N':
        pass
      
  #Clearing everything from previous game    
  def restart(self):
    for i in range(2):
     self.board =[]
     cp_board_copy.board = []
     self.hits = 0
     self.scount = 0
     self.rows_cols = {'row':[],'col':[]}
     self.create_board()
     self == cp
    cp_board_copy.create_board()
    player_1.start()
    
player_1 = board()
cp = board()
cp_board_copy = board()
player_1.start()