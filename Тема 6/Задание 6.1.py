class Parallelepiped:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def countBaseSquare(self):
        return self.width * self.length

    def countWidthSideSquare(self):
        return self.height * self.width

    def countLengthSideSquare(self):
        return self.height * self.length

    def countVolume(self):
        return self.width * self.length * self.height

    @staticmethod
    def info():
        print('__init__ ' + 'countBaseSquare ' + 'countWidthSideSquare ' + 'countLengthSideSquare ' + 'countVolume')