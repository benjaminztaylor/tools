import cv2
import numpy as np

max_block_size = 5000
max_offset = 100
tb_block_value = 'Block size'
tb_offset_value = 'Offset Value'
window_name = 'Adaptive Threshold'

img_path_00 = 'test-images/17-57-59.000-resize-00050-gray.png'
src = cv2.imread(img_path_00)

# print error with invalid image path
if src is None:
    print(f'Input error: {img_path_00}')
    exit(0)
    
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# resize imgs
src = cv2.resize(src_gray, (640, 480))
    

def track_adaptive_thresh(val):

    offset_val = cv2.getTrackbarPos(tb_offset_value, window_name)

    block_size = cv2.getTrackbarPos(tb_block_value, window_name)
    block_size = max(3, block_size)
    
    if (block_size % 2 == 0):
            block_size  += 1
    
    thresh = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, offset_val)        
    cv2.imshow(window_name, thresh)

# name window
cv2.namedWindow(window_name)

# Add trackbars
cv2.createTrackbar(tb_block_value, window_name , 0, max_block_size, track_adaptive_thresh)
cv2.createTrackbar(tb_offset_value, window_name , 0, max_offset, track_adaptive_thresh)


track_adaptive_thresh(3)
cv2.waitKey()