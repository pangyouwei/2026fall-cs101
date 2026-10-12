class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        doubles = maxDoubles

        while target != 1:
            if doubles > 0:
                if target % 2 == 0:
                    target //= 2
                    moves += 1
                    doubles -= 1
                else:
                    target -= 1
                    moves += 1
            else:
                moves += target - 1
                target = 1

        return moves
