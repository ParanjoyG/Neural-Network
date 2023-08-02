import cv2
import numpy as np

alpha = 1.1
beta = 25
gate = 'demonstration'

img = cv2.imread('lenna 200.png',0)
rows,cols = img.shape
#cv2.imshow("Original", img)
# cv2.imwrite(f'images/{gate}/Original.png', img)

# for x in range(1,5) :
#     array = cv2.imread(f'images/{gate}/output_{x}.png',0)
#     #cv2.imshow(f'Filter {x}', array)

#     for i in range(rows):
#         for j in range(cols):
#             img[i,j] = (array[i,j]/255)*img[i,j]
    
#     for a in range(img.shape[0]):
#         for b in range(img.shape[1]):
#             img[b,a] = np.clip(alpha*img[b,a] + beta, 0, 255)

#     #cv2.imshow(f'Result {x}', img)
#     cv2.imwrite(f'images/{gate}/Result {x}.png', img)




array = cv2.imread(f'images/demonstration/output_199.png',0)
cv2.imshow(f'Filter 4', array)

for i in range(rows):
    for j in range(cols):
        img[i,j] = (array[i,j]/255)*img[i,j]

cv2.imshow(f'Result 4', img)

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        img[y,x] = np.clip(alpha*img[y,x] + beta, 0, 255)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
        