import click
from pyPreviewGenerator.pyPreviewGenerator import generate_preview

@click.command()
@click.option('-f','--filepath',
              help='Full path to your input video file',type = str)
@click.option('-s','--startrange',
              help='Starting range to extract clips of as seconds, exp : 30',type = int)
@click.option('-e','--endrange',
              help='Ending range to extract clips of as seconds, exp : 680',type = int)
@click.option('-i','--introrange',default = None,
              help='Range of intro to clip to first of video as seconds in tuple, exp : (0,30)',type = tuple)
@click.option('-o','--outrorange',default = None,
              help='Range of outro to clip to end of video as seconds in tuple, exp : (0,30)',type = tuple)
@click.option('-m','--miniclipscount',default = 3,
              help='How many scenes you want to split clip into',type = int)
@click.option('-d','--fadeeffectduration',default = 1,
              help='Fade effect between clips duration as second',type = int)
@click.option('-p','--fadeeffectpadding',default = -0.5,
              help='Fade effect between clips padding as second',type = float)
@click.option('-x','--exportpath',default = None,
              help='Full path to your output video file, including format suffix, if None, it will save next to input file',type = str)
def pg_cli(filePath,
           startrange,
           endrange,
           introrange,
           outrorange,
           miniclipscount,
           fadeeffectbetweenclips,
           fadeeffectpadding,
           exportpath):
    generate_preview(filePath=filePath,
                     startRange=startrange,
                     endRange=endrange,
                     introRange=introrange,
                     outroRange=outrorange,
                     miniClipsCount=miniclipscount,
                     fadeEffectBetweenClips=fadeeffectbetweenclips,
                     fadeEffectPadding=fadeeffectpadding,
                     exportPath=exportpath
                     )

if __name__ == "__main__":
    pg_cli()
