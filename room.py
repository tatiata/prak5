class Win_Door:
     def __init__(self, x, y):
          self.square = x * y
class Room:
    def __init__(self, x, y, z):
        self.width = y
        self.lenght = x
        self.height = z
        self.wd = []
    def addWD(self, w, h):
        self.wd.append(Win_Door(w, h))
    def workSurface(self):
        square = 2 * self.height * (self.lenght + self.width)
        for i in self.wd:
            square -= i.square
        return square
    def wallpapers(self, a, b):
        if  self.workSurface()%(a*b) == 0:
            return self.workSurface() / (a*b)
        else:
            return self.workSurface()//(a*b) + 1
