import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 


if __name__ == "__main__":
    img = mpimg.imread('home/turtlebot/Pictures/success.png')
    plt.imshow(img)
    plt.show()

"""    
with Image.open('home/turtlebot/Pictures/success.png') as img:
    img.show()
"""