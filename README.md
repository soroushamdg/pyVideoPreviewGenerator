# pyPreviewGenerator
**pyPreviewGenerator** is a python module you can use to generate short previews of your videos. Like you have made a short documentry for your school and you want to create a short preview to post on instagram, so you can quickly generate the preview using this script, it's super easy to use, and so much faster than doing it by video editors.


# Installation

you can both clone this repository or install it using pip, both instructions are below;
- installing using **pip**

    `pip install pyPreviewGenerator`

you can checkout modules pip page here.

- Clone & Install
1. clone repo
2. run below command to install requirements:
3. change terminal directory to cloned directory
4. run: `pip install .`
5. you're ready to go!

## Usage

first you need to import the module

    from pyPreviewGenerator import pyPreviewGenerator
then to generate run below function

'''python
pyPreviewGenerator.generate_preview(filePath,   
                                    startRange = 50, #as second   
 endRange = 350, #as second   
 introRange=(0,50), # pick intro from 0 to 60 seconds of input video as intro - default = None   
 outroRange= (351,400), # pick outro from 351 to 400 seconds of input video as outro - default = None  
  miniClipsCount=3, # define how many parts your video split into - default = 3   
 fadeEffectBetweenClips= 1 , # define fade effect duration for between scenes as seconds - default = 1  
  fadeEffectPadding = -0.5,  # define padding between scenes - default = -0.5   
 exportPath = None # define export path - default = 'preview.mp4' next to input video  
  )
  '''

## License
**@soroushamdg made it.**

License attached to here

## Issues
if you found a bug, catch it then throw it in issues section