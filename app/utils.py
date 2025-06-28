# Utility functions such as video writing, frame processing etc.

import cv2
import numpy as np
import os

def save_frames_as_video(frames, filename, fps=12):
    if not frames or frames[0] is None:
        print("No frames to save.")
        return None

    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    for frame in frames:
        video_writer.write(frame)

    video_writer.release()
    print(f"Video saved to {filename}")
    return filename
