Grub Background Image Swapper

Purpose:
  - I just wanted a simple way to change the desktop image shown on the Grub menu screen. This script allows me to either run it manually to set a new background, run as a CRON job or similar, or run from a shell script at login or other time.

Usage: 
  - Either run using python command: python grub_background_image_swapper.py
  - Or set the script to executable, chmod +x grub_background_image_swapper.py, and run it directly.

Configuration:
  - You can configure the image directory and the Grub desktop image location via the default.cfg file.
  - You can also pass in the settings via the command line: grub_background_image_swapper.py imgDir backgroundImgFilePath
  - Values passed on the command prompt will override settings from the default.cfg file.

By default we look for and store images in the '/home/shared/images' folder. The default filename is 'grub-bg.jpg'. This path+filename combination needs to match what is set in the Grub config file for the destkop image. This is not a standard 
*nix folder and will need to be created and updated with the proper access rights. Of course, if you set the configuration file or command line parameters to a different folder you will need to ensure they have proper access.
