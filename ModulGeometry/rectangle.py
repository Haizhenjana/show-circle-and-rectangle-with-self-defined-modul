# Create a new Rectangle class for creating a rectangle object
class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='b'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        # this method shows the rectangle graph
        import matplotlib.pyplot as plt
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()