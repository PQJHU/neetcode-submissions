class CountSquares:

    def __init__(self):
        self.points = dict()

    def add(self, point: list[int]) -> None:
        point = tuple(point)
        self.points[point] = self.points.get(point, 0) + 1


    def count(self, point: list[int]) -> int:
        """
        Search through the points to first find the diagonal point, and then the other two points
        diagonal (px, py) has the property: | qx - px| = |qy - py|
        and the other two points are (px, qy) and (qx, py)
        """
        counter = 0
        qx, qy = point[0], point[1]
        for (px, py), d_count in self.points.items():
            if abs(qx - px) == abs(qy - py) and qx != px and qy != py:
                # search the other two points
                c_points = [(qx, py), (px, qy)]
                counter += d_count * self.points.get(c_points[0], 0) * self.points.get(c_points[1], 0)
        return counter
