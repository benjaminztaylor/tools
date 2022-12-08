# Assorted tools

## Remove formatted text

Copies and renames files in a new folder. Uses a constant character in file name for renaming.

**Use 1**: run in terminal: `python rmv_rname.py -i test_files/`

Keeps everything starting with last character of breaking constant (here the constant is "_C").

**Use 2**: run in terminal: `python rmv_rname.py -c "_C" -i test_files/`

## Move files (script)

Moving images for multiple cameras into folders based on frame number (rather than camera number).


## Thresholding GUI

Simple OpenCV GUI for finding adaptive thresholding parameters (block_size and offset).

### Dependencies

- Python == 3.7.7
- NumPy  == 1.19.2
- OpenCV == 3.4.2

### Use 

From the terminal:

`python sothresh.py -i IMAGEPATH`

Optional input parameters:

-b: BLOCKSIZE: changes the maximum blocksize
-o: OFFSET: changes the max offset