import os, sys
import argparse
import json
import glob
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "json concat",
        epilog = "Concatenating json files",
        add_help = "How to use",
        prog = "python json_concat.py <arguments>")
    parser.add_argument("-i", "--directory", required = True,
        help = "Path to directory")
    
    args = vars(parser.parse_args())
    
    # Load all json files in directory
    par_dir = args['directory']
    
    input_files = glob.glob(f'{par_dir}/*.json')
    
    # Create an empty Pandas DataFrame
    df = pd.DataFrame(columns=list(json.load(open(input_files[0])).keys()))
    
    for idx, f in enumerate(input_files):
        with open(f) as js_f:
            # load json data
            js_d = json.load(js_f)
            
            img_path   = js_d['img_path']
            img_name   = js_d['img_name']
            shape      = js_d['shape']
            block_size = js_d['block_size']
            offset     = js_d['offset']
            date       = js_d['date']
            
            # append json data to df
            df.loc[idx] = [img_path, img_name, shape, block_size, offset, date]
            
    # save concat json as csv
    df.to_csv(f'{par_dir}/concat-json.csv')