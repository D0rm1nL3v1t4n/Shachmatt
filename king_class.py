from piece_class import Piece

class King(Piece):
    def CanMove(self,source,destination):
        xCoordChange = source[0] - destination[0]
        yCoordChange = source[1] - destination[1]
        illegalMoves = 0

        if abs(xCoordChange) > 1 or abs(yCoordChange) > 1:
            illegalMoves += 1
            print("The King cannot move to that spot!")

        if destination[2] == self.colour:
            illegalMoves += 1
            print("That is an illegal move, you already have a piece there!")

        if illegalMoves > 0:
            return False
        elif illegalMoves == 0:
            return True