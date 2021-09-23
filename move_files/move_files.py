import os
import glob
import shutil

# path to the folders contain
paths = 'input/*'
folders = glob.glob(paths)

# this will change based off of the files you want to move
ffmt = 'png'
fmt_split = 'frame_'


def Mover(folders, ffmt, fmt_split):
    """ folders: path to folders
        ffmt: format of the image files within the folders
        fmt_split: images files must share a naming convention.
    """
    for folder in folders:

        images = glob.glob('{}/*.{}'.format(folder, ffmt))
        
        for i, img in enumerate(images):
            # img name

            img_name = os.path.basename(img)

            # create separate folders for each frame
            frame_num = img.split('frame_')[1].split('.')[0]
            
            # create names for each folder based on number of items
            dest_folder = '{}/{}{}'.format('output', fmt_split, frame_num)

            if not os.path.isdir(dest_folder):
                os.mkdir(dest_folder)

            new_dir_path = '{}/{}'.format(dest_folder, img_name)
            shutil.move(img, new_dir_path)


Mover(folders, ffmt, fmt_split)