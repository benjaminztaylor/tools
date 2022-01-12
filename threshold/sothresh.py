import argparse
import cv2
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Sothresh",
        epilog = "Adaptive Thresholding GUI",
        add_help = "How to use",
        prog = "python sothresh.py <arguments>")
    parser.add_argument("-i", "--image", required = True,
        help = "Path to input image")
    parser.add_argument("-b", "--blocksize", default = 4999, type = int,
        help = "Maximum blocksize [DEFAULT: 4999].")
    parser.add_argument("-o", "--offset", default = 100, type = int,
        help = "Maximum offset [DEFAULT: 100].")
    args = vars(parser.parse_args())

    # Collect the arguments.
    max_block_size = args['blocksize']
    max_offset = args['offset']
    img_path = args['image']
    
    tb_block_value = 'Block size'
    tb_offset_value = 'Offset Value'
    window_name = 'Adaptive Threshold'

    src = cv2.imread(img_path)

    # print error with invalid image path
    if src is None:
        print(f'Input error: {img_path}')
        exit(0)
        
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # resize imgs
    src = cv2.resize(src_gray, (640, 480))
        

    font = cv2.FONT_HERSHEY_SIMPLEX
    
    def track_adaptive_thresh(val):

        offset_val = cv2.getTrackbarPos(tb_offset_value, window_name)
        block_size = cv2.getTrackbarPos(tb_block_value, window_name)
        block_size = max(3, block_size)
        
        if (block_size % 2 == 0):
                block_size  += 1
        
        thresh = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, offset_val)
        # writes blocksize and offset to image
        thresh = cv2.putText(thresh, f"Offset:{offset_val} || Block Size:{block_size}", (10, 20), font, 0.5, (0, 0, 0), 2)
        thresh = cv2.putText(thresh, f"Offset:{offset_val} || Block Size:{block_size}", (10, 20), font, 0.5, (255,255,255), 1)
        cv2.imshow(window_name, thresh)

    # name window
    cv2.namedWindow(window_name)

    # Add trackbars
    cv2.createTrackbar(tb_block_value, window_name , 0, max_block_size, track_adaptive_thresh)
    cv2.createTrackbar(tb_offset_value, window_name , 0, max_offset, track_adaptive_thresh)


    track_adaptive_thresh(3)
    cv2.waitKey()