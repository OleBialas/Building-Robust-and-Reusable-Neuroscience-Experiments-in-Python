from argparse import ArgumentParser
from psychopy import prefs

prefs.hardware["audioLatencyMode"] = 0
from psychopy.event import waitKeys
from psychopy.sound import Sound
from psychopy.visual import Window

parser = ArgumentParser()
parser.add_argument("freq", type=int)
parser.add_argument("key", type=str)
parser.add_argument("--timed", action="store_true")
args = parser.parse_args()

with Window() as win:
    tone = Sound(value=args.freq, stereo=False)
    tone.play()
    keys = waitKeys(keyList=[args.key], timeStamped=args.timed)
    if args.timed:
        print(keys[0][1])
