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

# Move file to it's new location.
def moveImageFile():
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
    while imgDir + files[i] == backgroundImgFilePath:
        if len(files) = 1:
            print('The imgFile and backgroundImgFilePath are the same and are also the only file in the destination folder. Exiting.')
            return
        print('Files are the same. Generating new random.')
        i = random.randrange(len(files))
    
    print('Copying file, ' + files[i] + ', to bg image.')
    shutil.copyfile(imgDir + files[i], backgroundImgFilePath)

# Get a random(0-len(files)) file and cp it over to backgroundImageFile.
# params is sys.argv and contains filename[0], imgDir[1], backgroundImgFilePath[2].
def main(params):
    getConfiguration()

    # Set imgDir to first param, backgroundImgFilePath to second param
    if len(params) == 3:
        print('backgroundImgFilePath and imgDir were passed in as startup parameters. Bypassing \'default.cfg\' settings.')
        backgroundFilePath = params[2]
        imgDir = params[1]
    elif len(params) == 2:
        print('imgDir was passed in as a startup parameter. Bypassing \'default.cfg\' setting.')
        imgDir = params[1]

    moveImageFile()

if __name__ == '__main__':
    main(sys.argv)
