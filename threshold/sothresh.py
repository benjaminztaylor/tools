import os, sys
import time
import argparse
import json
import datetime, dateutil
from pathlib import Path
import cv2 as cv
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Sothresh",
        epilog = "Adaptive Thresholding GUI",
        add_help = "How to use",
        prog = "python sothresh.py <arguments>")
    parser.add_argument("-i", "--image", required = True,
        help = "Path to input image")
    parser.add_argument("-d", "--out_dir", 
                        default=Path(__file__).absolute().parent/ "ouput", 
                        type = Path, help = "path to output directory")
    parser.add_argument("-b", "--blocksize", default = 4999, type = int,
        help = "Maximum blocksize [DEFAULT: 4999].")
    parser.add_argument("-o", "--offset", default = 100, type = int,
        help = "Maximum offset [DEFAULT: 100].")
    
    args = vars(parser.parse_args())
    
    # Collect the arguments.
    max_block_size = args['blocksize']
    max_offset = args['offset']
    img_path = args['image']
    out_dir = args['out_dir']
    
    # if no output directory
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    tb_block_value = 'Block size'
    tb_offset_value = 'Offset Value'
    window_name = 'Adaptive Threshold'

    src = cv.imread(img_path)

    # print error with invalid image path
    if src is None:
        print(f'Input error: {img_path}')
        exit(0)
    
    # convert to grayscale
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    
    # resize image
    src = cv.resize(src_gray, (640, 480))
    
    # set font for parameters written on screen
    font = cv.FONT_HERSHEY_SIMPLEX
    
    def track_adaptive_thresh(val):

        offset_val = cv.getTrackbarPos(tb_offset_value, window_name)
        block_size = cv.getTrackbarPos(tb_block_value, window_name)
        block_size = max(3, block_size)
        
        if (block_size % 2 == 0):
                block_size  += 1
        
        thresh = cv.adaptiveThreshold(src, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, block_size, offset_val)
        # writes blocksize and offset to image
        thresh = cv.putText(thresh, f"Offset:{offset_val} || Block Size:{block_size}", (10, 20), font, 0.5, (0, 0, 0), 2)
        thresh = cv.putText(thresh, f"Offset:{offset_val} || Block Size:{block_size}", (10, 20), font, 0.5, (255,255,255), 1)
        # display the original with thresh
        frame = np.hstack((src, thresh))
        # display
        cv.imshow(window_name, frame)
        
        key = cv.waitKey(0)& 0xFF
        
        # key strokes
        if key == ord('s'):
            write_meta(img_path, block_size, offset_val)
            out_img_file = f'{out_dir}/thresh_{os.path.basename(img_path)}'
            cv.imwrite(out_img_file, thresh)
            cv.destroyAllWindows()
            cv.waitKey(1)
        
        elif key == ord('q'):
            cv.destroyAllWindows()
            cv.waitKey(1)



    def write_meta(img_path, block_size, offset_val):
        """Saves parameters found using GUI.

        Args:
            img_path (PATH):  path to image
            block_size (int): neighborhood size used in adaptive threshold
            offset_val (int): offset of mean used in adaptive thresholding
        """
        
        meta = {
            "img_path": img_path,
            "img_name": os.path.basename(img_path),
            "shape": cv.imread(img_path).shape,
            "block_size": block_size,
            "offset": offset_val,
            "date": datetime.datetime.now().strftime("%m-%d-%Y-%H-%M")
            }
        
        # file name formatting
        fn = str(out_dir) + '/' + meta['img_name'][:-4] + '_params_' + '.json'
        json_object = json.dumps(meta, indent = 4)
        
        with open(fn, "w") as outfile:
            outfile.write(json_object)
        
    # name window
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # Add trackbars
    cv.createTrackbar(tb_block_value, window_name , 0, max_block_size, track_adaptive_thresh)
    cv.createTrackbar(tb_offset_value, window_name , 0, max_offset, track_adaptive_thresh)

    track_adaptive_thresh(3)
    cv.waitKey()
    cv.destroyAllWindows()