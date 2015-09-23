class Square(object):
  # Returns a Square object.
  def __init__(self, letter, number, piece = None):
    self.letter = letter
    self.number = number
    self.position = [letter, number]
    self.piece = piece

  # Returns the color of the piece occupying a square.
  def occupied(self):
    if self.piece != None:
      return self.piece.color
    else:
      return False
  
  # Returns True if square is empty.
  def empty(self):
    if self.piece == None:
      return True
    else:
      return False


class ChessBoard:
  # Creates a chessboard.
  def __init__(self):
    letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    numbers = [1,2,3,4,5,6,7,8]
    squares = [] # Array representing all the squares on the board.
  
  # Creates 64 empty squares.  
    for letter in letters:
      for number in numbers:
        squares.append(Square(letter, number, None))
    self.squares = squares

  # Places the piece on the proper square on the board.
  def setup(self, pieces):
    for square in self.squares:
      for piece in pieces:
        if (square.position == piece.currentPosition):

            square.piece = piece # Sets the square's piece.
            piece.currentPosition = square # Sets the piece's square.

  # Returns the empty squares on the board.
  def empty_squares(self):
    emptySquares = []
    for square in self.squares:
      if square.piece == None:
        emptySquares.append(square.position)
    return emptySquares


class ChessPiece(object):
  # Returns a chess piece object with a color and a current position.
  def __init__(self, color, currentPosition):
    self.color = color
    self.currentPosition = currentPosition
    self.letter = currentPosition[0]
    self.number = currentPosition[1]
    self.possibleMoves = []

  # Checks if a given direction x ,y is a possible move.
  def move(self, chessBoard, currentSquare, x, y, repeat = None):
    for square in chessBoard.squares:

      # Can move to a given square if it is empty.
      if square.position == [chr(ord(currentSquare.letter) + x), currentSquare.number + y] and square.empty():
        self.possibleMoves.append(square.position)
        # Repeatedly checks in a certain direction if it is a possible move for a given square.
        if repeat == True:
          return self.move(chessBoard, square, x, y, repeat)

      # Can move to a given square if it is occupied by opponent's piece.
      elif square.position == [chr(ord(currentSquare.letter) + x), currentSquare.number + y] and (square.occupied() != self.color):
        self.possibleMoves.append(square.position)

  # Returns a formatted string of the piece's possible move.
  def print_move(self, pieceName):
    for move in self.possibleMoves:
      format = pieceName + " at <" + self.letter + ":" + str(self.number) + "> can move to <" + move[0] + ":" +str(move[1]) +">"
      print(format)


class Pawn(ChessPiece):
  def possible_moves(self, chessBoard, currentSquare):
    
    # White pieces can only move towards higher number positions.
    if self.color == "White":
      up = [self.letter, self.number + 1]
      twoUp = [self.letter, self.number + 2]
      rightUp = [chr(ord(self.letter) + 1), self.number + 1]
      leftUp = [chr(ord(self.letter) - 1), self.number + 1]
    
    # Black pieces can only move towards lower number positions.
    if self.color == "Black":
      up = [self.letter, self.number - 1]
      twoUp = [self.letter, self.number - 2]
      rightUp = [chr(ord(self.letter) - 1), self.number -1]
      leftUp = [chr(ord(self.letter) + 1), self.number - 1]

    for square in chessBoard.squares:

      # Can move up if square is empty.
      if square.position == up and square.empty():
        up_square = square.position
        self.possibleMoves.append(up_square)

      # Can move up two squares iff the square behind it is also empty.
      for move in self.possibleMoves:
        if (move == up_square) and square.position == twoUp and square.empty():
          self.possibleMoves.append(square.position)

      # Can move diagonal if it is occupied by opponent's piece.
      if (square.position == rightUp) and ((square.occupied() != False) and (square.occupied() != self.color)):
        self.possibleMoves.append(square.position)

      if (square.position == leftUp) and ((square.occupied() != False) and (square.occupied() != self.color)):
        self.possibleMoves.append(square.position)
    
    self.print_move("Pawn")


class Rook(ChessPiece):
  # Rook may move up, down, left, or right.
  def move_udlr(self, chessBoard, currentSquare, repeat = None):
    self.move(chessBoard, currentSquare, 0, 1, repeat)
    self.move(chessBoard, currentSquare, 0, -1, repeat)
    self.move(chessBoard, currentSquare, -1, 0, repeat)
    self.move(chessBoard, currentSquare, 1, 0, repeat)

  def possible_moves(self, chessBoard, currentSquare):
    self.move_udlr(chessBoard, currentSquare, True)
    self.print_move("Rook")


class Bishop(ChessPiece):
  # Bishop may move diagonal in all directions.
  def move_diagonal(self, chessBoard, currentSquare, repeat = None):
    self.move(chessBoard, currentSquare, 1, 1, repeat)
    self.move(chessBoard, currentSquare, 1, -1, repeat)
    self.move(chessBoard, currentSquare, -1, 1, repeat)
    self.move(chessBoard, currentSquare, -1, -1, repeat)

  def possible_moves(self, chessBoard, currentSquare):
    self.move_diagonal(chessBoard, currentSquare, True)
    self.print_move("Bishop")


class Knight(ChessPiece):
  # Knight may move in an L-shape in all directions for one square only.
  def possible_moves(self, chessBoard, currentSquare):
    self.move(chessBoard, currentSquare, 2, 1)
    self.move(chessBoard, currentSquare, 2, -1)
    self.move(chessBoard, currentSquare, -2, 1)
    self.move(chessBoard, currentSquare, -2, -1)
    self.move(chessBoard, currentSquare, 1, 2)
    self.move(chessBoard, currentSquare, -1, 2)
    self.move(chessBoard, currentSquare, 1, -2)
    self.move(chessBoard, currentSquare, -1, -2)
    self.print_move("Knight")


class Queen(Rook, Bishop):
  # Queen may move like a Rook or a Bishop.
  def possible_moves(self, chessBoard, currentSquare):
    self.move_diagonal(chessBoard, currentSquare, True)
    self.move_udlr(chessBoard, currentSquare, True)
    self.print_move("Queen")


class King(Rook, Bishop):
  # King may move like a Rook or a Bishop for one square only.
  def possible_moves(self, chessBoard, currentSquare):
    self.move_diagonal(chessBoard, currentSquare)
    self.move_udlr(chessBoard, currentSquare)
    self.print_move("King")


# Calls all the possible plays for a given player's pieces. 
def playChess(configuration, player):
  board = ChessBoard() # Initializes a board.
  board.setup(configuration) # Sets up board wih a given configuration.

  for piece in configuration: 
    if piece.color == player:
      piece.possible_moves(board, piece.currentPosition)


def main():
  # Initializes chess piece and color.
  whitePlayer = [

    Pawn("White", ["A", 2]),
    Pawn("White", ["B", 2]),
    Pawn("White", ["C", 2]),
    Pawn("White", ["D", 2]),
    Pawn("White", ["E", 2]),
    Pawn("White", ["F", 2]),
    Pawn("White", ["G", 2]),
    Pawn("White", ["H", 2]),
    Knight("White", ["B", 1]),
    Knight("White", ["G", 1]),
    Bishop("White", ["F", 1]),
    Bishop("White", ["C", 1]),
    Rook("White", ["A", 1]),
    Rook("White", ["H", 1]),
    Queen("White", ["D", 1]),
    King("White", ["E", 1])

    ]

  for piece in whitePlayer:
    piece.color = "White"

  blackPlayer = [

    Pawn("Black", ["A", 7]),
    Pawn("Black", ["B", 7]),
    Pawn("Black", ["C", 7]),
    Pawn("Black", ["D", 7]),
    Pawn("Black", ["E", 7]),
    Pawn("Black", ["F", 7]),
    Pawn("Black", ["G", 7]),
    Pawn("Black", ["H", 7]),
    Knight("Black", ["B", 8]),
    Knight("Black", ["G", 8]),
    Bishop("Black", ["F", 8]),
    Bishop("Black", ["C", 8]),
    Rook("Black", ["A", 8]),
    Rook("Black", ["H", 8]),
    Queen("Black", ["D", 8]),
    King("Black", ["E", 8])

    ]

  for piece in blackPlayer:
    piece.color = "Black"

  initialState = whitePlayer + blackPlayer # Testing with the initial state on the chessboard.
  player = "White"
  playChess(initialState, player)



main()