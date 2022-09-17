
class Coordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, coordinate):
        x_diff = (self.x - coordinate.x)**2
        y_diff = (self.y - coordinate.y)**2
        
        return (x_diff + y_diff)**0.5

if __name__ == '__main__':
    point_1 = Coordinate(2, 4)
    point_2 = Coordinate(9, -5)

    print(point_1.distance(point_2))