import numpy as np
from PIL import Image
pil_im = Image.open('data/empire.jpg', 'r')
imshow(np.asarray(pil_im))
