class Square(object):
  # Returns a Square object whose letter position is *letter* and number position is *number*, an is either occupied or not by a chess piece.
  def __init__(self, letter, number, piece = None):
    self.letter = letter
    self.number = number
    self.position = [letter, number]
    self.piece = piece

class ChessBoard:

  # Creates a chessboard.
  def __init__(self):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = [1,2,3,4,5,6,7,8]
    squares = [] # Array representing all the squares on the board.

    for letter in letters:
      for number in numbers:
        squares.append(Square(letter, number, None))
    self.squares = squares

  # Places the piece on the proper square on the board.
  def setup(self, pieces):
    for square in self.squares:
      for piece in pieces:
        if (square.position == piece.currentPosition):
            square.piece = piece

  # Returns the empty squares on the board.
  def empty_squares(self):
    emptySquares = []
    for square in self.squares:
      if square.piece == None:
        emptySquares.append(square.position)
    return emptySquares

  def possibleMoves(self, pieces):
    for piece in pieces:
      #piece.possiblemoves()

class ChessPiece(object):
  def __init__(self, color):
    self.color = color


class King(ChessPiece):
  def __init__(self, currentPosition):
    self.currentPosition = currentPosition
   
  #def possiblemoves(self):
    
    

class Queen(ChessPiece):
  def __init__(self, currentPosition):
    self.currentPosition = currentPosition

class Rook(ChessPiece):
  def __init__(self, currentPosition):
    self.currentPosition = currentPosition

class Bishop(ChessPiece):
  def __init__(self, currentPosition):
    self.currentPosition = currentPosition

class Knight(ChessPiece):
  def __init__(self, currentPosition):
    self.currentPosition = currentPosition

class Pawn(ChessPiece):
  def __init__(self, currentPosition):
    self.currentPosition = currentPosition



def Game(configuration):
  board = ChessBoard()
  board.setup(configuration)
  board.possibleMoves(configuration)

  empty = board.empty_squares()
  print(empty)

def main():

  # Initializes chess pieces
  wKing = King(["E", 1])
  wQueen = Queen(["D", 1])
  wRook1 = Rook(["A", 1])
  wRook2 = Rook(["H", 1])
  wBishop1 = Bishop(["F", 1])
  wBishop2 = Bishop(["F", 1])
  wKnight1 = Knight(["B", 1])
  wKnight2 = Knight(["G", 1])
  wPawn1 = Pawn(["A",2])
  wPawn2 = Pawn(["B",2])
  wPawn3 = Pawn(["C",2])
  wPawn4 = Pawn(["D",2])
  wPawn5 = Pawn(["E",2])
  wPawn6 = Pawn(["F",2])
  wPawn7 = Pawn(["G",2])
  wPawn8 = Pawn(["H",2])

  bKing = King(["E", 8])
  bQueen = Queen(["D", 8])
  bRook1 = Rook(["A", 8])
  bRook2 = Rook(["H", 8])
  bBishop1 = Bishop(["C", 8])
  bBishop2 = Bishop(["F", 8])
  bKnight1 = Knight(["B", 8])
  bKnight2 = Knight(["G", 8])
  bPawn1 = Pawn(["A",7])
  bPawn2 = Pawn(["B",7])
  bPawn3 = Pawn(["C",7])
  bPawn4 = Pawn(["D",7])
  bPawn5 = Pawn(["E",7])
  bPawn6 = Pawn(["F",7])
  bPawn7 = Pawn(["G",7])
  bPawn8 = Pawn(["H",7])

  player1 = [wKing]
  player2 = [bKing] 

  # Setting the color of the piece.
  for piece in player1:
    piece.color = "White"
    
  for piece in player2: 
    piece.color = "Black"

  # Testing with two pieces on the board.
  configuration = [wKing, bKing]

  Game(configuration)

main()