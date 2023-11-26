
import PIL 
from PIL import Image
import urllib.request
import io,sys
print(PIL.PILLOW_VERSION)
URL = sys.argv[1] #link of the file
f = io.BytesIO(urllib.request.urlopen(URL).read())
img = Image.open(f)
print(img.size)
pix = img.load()
print(pix[2,5])
img= img.show()
