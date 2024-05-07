import math

class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()

class RoundPeg:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

class SquarePeg:
    def __init__(self, width):
        self.width = width

    def get_width(self):
        return self.width

class SquarePegAdapter(RoundPeg):
    def __init__(self, peg):
        self.peg = peg

    def get_radius(self):
        return self.peg.get_width() * math.sqrt(2) / 2


hole = RoundHole(5)
rpeg = RoundPeg(5)
print(hole.fits(rpeg))  # Vypíše: True

small_sqpeg = SquarePeg(5)
large_sqpeg = SquarePeg(10)


small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)
print(hole.fits(small_sqpeg_adapter))
print(hole.fits(large_sqpeg_adapter))