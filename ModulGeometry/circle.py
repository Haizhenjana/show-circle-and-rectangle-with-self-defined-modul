# Create a class Circle
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='red'):
        self.radius = radius
        self.color = color 
    
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    def drawCircle(self):
        # this method shows the circle graph
        import matplotlib.pyplot as plt
        circle = plt.Circle((0, 0), radius=self.radius, fc=self.color)
        # create a object reference to the circle, not the image of the circle itself
        plt.gca().add_patch(circle)
        # gives a reference to the current axes and adds the shape to the graph
        plt.axis('scaled')
        # gives appropriate scaling that you specify for the shape. the default value is 1.0 vertivally and horizontally
        plt.show()
        # show the circle graph