import random
import pathlib
from moviepy.video.io import VideoFileClip
import moviepy.editor as mp


def mini_clips_times(count, start_range, end_range):
    """
    This function will return {count} number of mini clips start and end times as tuples in a list
    :param count: number of mini clips
    :param start_range: start range
    :param end_range: end range
    :return: [(start,end),...]
    """
    ranges = []
    miniRangesDurations = (end_range - start_range)/count
    for i in range(count):
        k = random.randrange(int(start_range + (i*miniRangesDurations)),int(start_range + (i*miniRangesDurations) +miniRangesDurations ))
        ranges.append(
            (k,k+5)
        )
    return ranges

def check_file_exists(path):
    return pathlib.Path(path).exists()

def generate_full_vieo_object(filepath):
    return VideoFileClip.VideoFileClip(filepath)

def generate_mini_clips_objects_array(VideoFile, clipsTimeRanges):
    return [VideoFile.subclip(startTime, endTime) for startTime, endTime in clipsTimeRanges]

def generate_fade_effect_between_clips(clipsObjects, fadeTime):
    return [clip.crossfadein(fadeTime) for clip in clipsObjects]

def generate_concatenate_videoclips(clips,method="compose",padding = 0):
    return mp.concatenate_videoclips(clips,
                                                method=method,
                                                padding = padding)