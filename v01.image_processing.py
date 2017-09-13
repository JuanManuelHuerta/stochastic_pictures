import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread('stinkbug.png')
#imgplot=plt.imshow(img)

th_cut=0.11
threshold_array=[]
for row in img:
    for cell in row:
        threshold_array.append(cell[0])
st=sorted(threshold_array)
threshold=st[int(len(st)*th_cut)]

an_img=[]
for row in img:
    a_row=[]
    for cell in row:
        if cell[0]<=threshold:
            cell=[0.01,0.01,0.01]
        else:
            cell=[0.9,0.9,0.9]
        a_row.append(cell)
    an_img.append(a_row)
            
imgplot=plt.imshow(an_img)



plt.show()


