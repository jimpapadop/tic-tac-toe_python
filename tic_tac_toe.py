import sys
board=["-", "-" ,"-",
       "-", "-" ,"-",
       "-", "-" ,"-"]
p = [0,1,2,3,4,5,6,7,8]
iX = [0,0,0,0,0,0,0,0,0]
iO = [0,0,0,0,0,0,0,0,0]
u = False

def display_board():
    print("|" + board[0]+ "|"+ board[1]+ "|" + board[2]+ "|")
    print("|" + board[3]+ "|"+ board[4]+ "|" + board[5]+ "|")
    print( "|" + board[6]+ "|"+ board[7]+ "|" + board[8]+ "|")

#check win condition for player 1

#check horizontal lines
def horx():  
  i = 0
  while i<9:
    if iX[i]+iX[i+1]+iX[i+2] == 3:
     print("player1 won")
     sys.exit()
    i+=3

#check vertical lines
def verx():  
  v=0
  while v<3:
    if iX[v]+iX[v+3]+iX[v+6] == 3:
     print("player1 won")
     sys.exit()
   
    v+=1

#check the diagonals
def diagx():  
   if iX[0]+iX[4]+iX[8] == 3:
     print("player1 won")
     sys.exit()
   elif iX[2]+iX[4]+iX[6] == 3:
      print("player1 won")
      sys.exit()

#check win condition for player 2

#check horizontal lines
def horo():
  i = 0
  while i<9:
    if iO[i]+iO[i+1]+iO[i+2] == 3:
     print("player2 won")
     sys.exit() 
    i+=3

#check vertical lines
def vero():
  v=0
  while v<3:
    if iO[v]+iO[v+3]+iO[v+6] == 3:
     print("player2 won")
     sys.exit()
   
    v+=1

       
#check the diagonals
def diago():
   if iO[0]+iO[4]+iO[8] == 3:
     print("player2 won")
     sys.exit()
   elif(iO[2]+iO[4]+iO[6] == 3) :
      print("player2 won")
      sys.exit()


def player1():
  position = input("Please p1 insert a position from 1-9: ")
  position = int(position) - 1  #shifts the variable position by one to the left
  if position in p :  

   board[position] = "X"
   
   display_board()
   p.remove(position)  #erases the taken positions of the board
   iX[position] = 1 
   horx()  
   verx()
   diagx()
   
  else: 
      print("this position is already taken")
      return player1()
  #win_check()
  
  if (p==[]):    #tie check
   print("this is a tie")
   sys.exit()
  
 
  player2()

def player2():
  position = input("Please p2 insert a position from 1-9: ")
  position = int(position) - 1   #shifts the variable position by one to the left   
  if position in p :  

   board[position] = "O"  

   display_board()
   p.remove(position)  #erases the taken positions of the board 
   iO[position]=1
   horo()
   vero()
   diago()
  else :
    print("this position is already taken")
    return player2()
  


  player1()


def play_game():
  display_board()
  player1()


play_game()
