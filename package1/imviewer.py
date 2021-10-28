from skimage.viewer import ImageViewer
from skimage.io import imread

img = imread('/Home/turtlebot/Pictures/success.png') #path to IMG
view = ImageViewer(img)
view.show()
