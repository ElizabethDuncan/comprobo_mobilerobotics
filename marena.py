import pickle
from PIL import Image

data = pickle.load( open("exampleArray.p", "rb"))
im = Image.open("mymap4.pgm")
im.convert(colors=256)
im.save("mymap4.jpg")
im_new = Image.open("mymap4.jpg")
pix = im_new.load()
print pix[0,0]
pix[0,0] = (255,0,0)
print im_new.size
print pix[0,0]
print len(data)