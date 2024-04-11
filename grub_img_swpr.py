#!/usr/bin/python3
""" Grub Background Image Swapper 
    
    Copies a random image file to use as background image for Grub boot loader.

    Usage: python grub_background_image_swapper.py Image_Direcotry Grub_Background_Image_File_Name
    
    Note: Grub_Background_Image_File_Name should match file name specified in Grub config file.
"""
import sys
import os
import random
import shutil

# Directory for image files
imgDir = '/home/shared/images/' 
# Background image file path
backgroundImgFilePath = '/home/shared/images/grub-bg.jpg'
# Settings
settings = []

# Read the defaults in from the config file if found.
def getConfiguration():
    print('Getting defaults from configuration file.')

    if not os.path.exists('./default.cfg'):
        print('\'default.cfg\' file was not found. Using preset values.')
        return
    
    with open('./default.cfg') as config_file:
        print('\'default.cfg\' file was found. Reading configuration values.')
        for setting in config_file:
            valuePair = setting.split('=')
            if str('DEFAULT_IMAGE_DIRECTORY') == valuePair[0]: 
                print('Setting imgDir to: ' + valuePair[1].strip() + '.')
                imgDir = valuePair[1]                
            elif str('DEFAULT_BACKGROUND_IMAGE_FILE_PATH') == valuePair[0]:
                print('Setting backgroundImgFilePath to: ' + valuePair[1].strip() + '.' )
                backgroundImgFilePath = valuePair[1]

# Get a random(0-len(files)) file and cp it over to backgroundImageFile.
def main():
    print('Checking if imgDir exists.')
    if not os.path.exists(imgDir):
        print('Folder not found. Creating it.')
        os.path.mkdir(imgDir)
    else:
        print('Folder already exists.')
        
    files = os.listdir(imgDir)
    if len(files) == 0:
        print('No files were found in the imgDir.')
        return

    i = random.randrange(len(files))
    print('Copying file, ' + files[i] + ', to bg image.')
    shutil.copyfile(imgDir + files[i], backgroundImgFilePath)

# Set imgDir to first param, backgroundImgFilePath to second param
if __name__ == '__main__':
    getConfiguration()

    if len(sys.argv) == 3:
        print('backgroundImgFilePath and imgDir were  passed in as startup parameters. Bypassing \'default.cfg\' settings.')
        backgroundImgFilePath = sys.argv[2]
        imgDir = sys.argv[1]
    elif len(sys.argv) == 2:
        print('imgDir was passed in as startup parameter. Bypassing \'default.cfg\' setting.')
        imgDir = sys.argv[1]

    main()
