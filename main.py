board=[' ' for _ in range(9)]
def printboard():
  print ("-------------")
  print ("|",board[0],"|", board[1],"|",board[2], "|")
  print ("-------------")
  print ("|",board[3],"|", board[4],"|",board[5], "|")
  print ("-------------")
  print ("|",board[6],"|", board[7],"|",board[8], "|")
  print ("-------------")

def checkwin():
  win= [[0,1,2], [3,4,5], [6,7,8],
      [0,3,6],[1,4,7],[2,5,8],
      [0,4,8],[2,4,6]]
  for i in win:
    if board[i[0]]==board[i[1]]==board[i[2]]!=" ":
      return True
  return False

def checktie():
  return " " not in board

def playgame():
  firstplayer ="X"
  while True:
    printboard()
    move=int(input("player " + firstplayer + ", enter your move.(0-8): "))
    if move<0 or move>8 or board[move]!=" ":
      print( "Invalid move try again." )
      continue

    board[move]=firstplayer
    if checkwin():
      printboard()
      print("Player" , firstplayer, " wins!")
      break

    if checktie():
      printboard()
      print("Its a tie!")
      break

    firstplayer="O" if firstplayer=="X" else "X"

playgame()
      
