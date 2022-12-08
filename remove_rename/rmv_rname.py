import os, sys
import glob
import argparse
import json
from pathlib import Path
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Remove portions of file name based on naming format.",
        epilog = "Rename files",
        add_help = "How to use",
        prog = "python rmv_rname.py <arguments>")
    parser.add_argument("-i", "--in_dir", required = True,
        help = "Path to directory containing files.")
    parser.add_argument("-d", "--out_dir", 
                        default=Path(__file__).absolute().parent/ "ouput", 
                        type = Path, help = "path to output directory")
    parser.add_argument("-c", "--constant", 
                    default="_C", 
                    type = str, help = "constant in file name to break on")
    args = vars(parser.parse_args())
    
    # Collect the arguments.
    str_constant = args['constant']
    in_dir = args['in_dir']
    out_dir = args['out_dir']
    
    all_files = glob.glob(f"{in_dir}*")
    # if no output directory
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        
    for f in all_files:
        fname = os.path.basename(f)
        nname = fname.split(str_constant)[-1]
        dest = f"{out_dir}/{str_constant[1]}{nname}"
        shutil.copy(f,dest)