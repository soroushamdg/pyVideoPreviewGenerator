import pathlib
from pyPreviewGenerator import helpers


def generate_preview(filePath, startRange, endRange, introRange=None, outroRange= None,miniClipsCount=3, fadeEffectBetweenClips= 1, fadeEffectPadding = -0.5, exportPath = None):
    """
    This function will export generated preview as mp4 next to input path.
    :param filePath: input video path
    :param startRange: mini clips start range
    :param endRange: mini clips end range
    :param introRange: if you want to include intro at the first of preview, enter as : [startRange,endRange]
    :param outroRange: if you want to include outro at the end of preview, enter as : [startRange,endRange]
    :param miniClipsCount: How many mini clips it should have
    :return: Boolean
    """
    assert helpers.check_file_exists(filePath), 'pyPreviewBaker => Error, file does not exist'

    clipsTimeRanges = []

    if introRange:
        clipsTimeRanges.append(tuple(introRange))

    miniClips = helpers.mini_clips_times(count= miniClipsCount, start_range= startRange, end_range= endRange)

    assert miniClips, 'pyPreviewBaker => Error in generating random mini clips timings, check your range and try again.'

    clipsTimeRanges.extend(miniClips)

    if outroRange:
        clipsTimeRanges.append(tuple(outroRange))

    try:
        fullVideo = helpers.generate_full_vieo_object(filePath)
    except:
        print('pyPreviewBaker => Can\'t open input video clip, check and try again.')
        return False
    else:
        print('pyPreviewBaker => Opening input video was successful')

    miniClipsVideos = helpers.generate_mini_clips_objects_array(fullVideo, clipsTimeRanges= clipsTimeRanges)

    if fadeEffectBetweenClips:
        clipsFinal = helpers.generate_fade_effect_between_clips(clipsObjects=miniClipsVideos, fadeTime=fadeEffectBetweenClips)
    else:
        clipsFinal = miniClipsVideos

    try:
        print('concatenating clips')
        concat_clip = helpers.generate_concatenate_videoclips(clipsFinal,
                                                              method="compose",
                                                              padding = fadeEffectPadding if fadeEffectBetweenClips else 0)
    except:
        print('pyPreviewBaker => mixing mini clips went wrong, please check your ranges and try again')
        return False
    else:
        print('pyPreviewBaker => mixed mini clips successfully')

    try:
        concat_clip.write_videofile(exportPath if exportPath else str(pathlib.Path(filePath).parent.joinpath('preview_pyPreviewGenerator.mp4')))
    except Exception as msg:
        print('pyPreviewBaker => Writing export .mp4 file went wrong',msg)
        return False
    else:
        print('pyPreviewBaker => Export finished successfully.')
    return True
