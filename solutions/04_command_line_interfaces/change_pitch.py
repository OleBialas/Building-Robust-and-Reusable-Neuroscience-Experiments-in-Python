from argparse import ArgumentParser
from psychopy import prefs

prefs.hardware["audioLatencyMode"] = 0
from psychopy.event import waitKeys
from psychopy.sound import Sound
from psychopy.visual import Window

parser = ArgumentParser()
parser.add_argument("freq", type=int)
parser.add_argument("step", type=int)
parser.add_argument("n_trials", type=int)
args = parser.parse_args()

freq = args.freq
with Window() as win:
    for i in range(args.n_trials):
        tone = Sound(value=freq, stereo=False)
        tone.play()
        key = waitKeys(keyList=["up", "down"])[0]
        if key == "up":
            freq += args.step
        else:
            freq -= args.step
