class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        if xCenter < x1:
            xNear = x1 - xCenter
        elif xCenter > x2:
            xNear = xCenter - x2
        else:
            xNear = 0

        if yCenter < y1:
            yNear = y1 - yCenter
        elif yCenter > y2:
            yNear = yCenter - y2
        else:
            yNear = 0

        nearest_distance_square = xNear ** 2 + yNear ** 2

        if nearest_distance_square > radius ** 2:
            return False
        else:
            return True
