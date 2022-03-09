import os, sys
import time
import argparse
import json
import datetime, dateutil
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Experiment Info",
        epilog = "Record meta information on experiment.",
        add_help = "How to use",
        prog = "python experi.py <arguments>")

    parser.add_argument('-t','--type', choices=['Migration', 'Foraging', 'other'],
                        help = "General type of experiment.")
    parser.add_argument('-d', '--date', default = 'today', type = str,
                        help = "Date of experiment [DEFAULT: today]. Format Must be ISO: 'YYYY-MM-DD'.")
    parser.add_argument('-s','--species', choices=['T.rugatulus', 'T.curvispinosus', 'other'],
                        help = "Species used in experiment.")
    parser.add_argument('-r','--recording_size', type = float,
                        help = "Size of recording")   
    
    args = vars(parser.parse_args())
    
    # Collect the arguments.
    exp_type = args['type']
    exp_date = args['date']
    exp_spp  = args['species']
    exp_size = args['recording_size']
    
    # handling date input
    if exp_date == 'today':
        date = datetime.datetime.now().strftime("%Y-%m-%d")
    else:
        date_temp = datetime.date.fromisoformat(exp_date)
        date = date_temp.strftime("%Y-%m-%d")
           
    meta = {
        "date": date,
        "exp_type": exp_type,
        "species": exp_spp,
        "File Size (TB)": exp_size,
        }
    
    # file name formatting
    fn = f"T_{exp_spp[2:5]}_{exp_type}_{exp_date}.json"
    json_object = json.dumps(meta, indent = 4)
    
    with open(fn, "w") as outfile:
        outfile.write(json_object)
   