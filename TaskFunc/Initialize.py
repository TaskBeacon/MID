from psychopy import visual
from psychopy.hardware import keyboard
from psychopy.visual import Circle, Rect, Polygon
from types import SimpleNamespace
from datetime import datetime
from TaskFunc.SetupSeed import SetupSeed


def Initialize(subdata):
    """
    Initializes window, stimuli, experiment settings, and keyboard.

    Args:
        subdata (list): Subject info including ID.
    Returns:
        win (visual.Window): The PsychoPy window object.
        kb (keyboard.Keyboard): Keyboard input handler.
        settings (SimpleNamespace): Experimental settings and stimuli.
    """
    win = visual.Window(
        size=[1920, 1080],
        monitor="testMonitor",
        units="deg",
        screen=1,
        color="white",
        fullscr=True,
        gammaErrorPolicy='ignore'  # avoid gamma ramp errors
    )

    # Define settings
    settings = SimpleNamespace()
    settings.TotalBlocks = 2
    settings.TotalTrials = 20
    settings.TrialsPerBlock = settings.TotalTrials // settings.TotalBlocks

    # random seed
    settings = SetupSeed(settings, subdata, mode="indiv") # each sub will have a unique seed

    # Cue stimuli (colored)
    settings.CircleCue = Circle(win, radius=4, fillColor='magenta', lineColor=None) # Reward cue (based on image)
    settings.SquareCue = Rect(win, width=8, height=8, fillColor='yellow', lineColor=None) # Punishment cue (based on image)
    settings.TriangleCue = Polygon(win, edges=3, size=8, fillColor='cyan', lineColor=None) # Neutral cue (based on image)

    # Target stimulus (black)
    settings.CircleTarget = Circle(win, radius=4, fillColor='black', lineColor=None)

    settings.cueTypes = [1, 2, 3]  # 1 = circle, 2 = square, 3 = triangle (representing cue types)

    # Timing
    settings.cueDuration = 1
    settings.targetDuration = 0.5 # Example duration, adjust as needed
    settings.trialDuration = 3

    # Keyboard settings
    settings.responseKey = 'space' # Assuming a single key press to the target
    settings.keyList = [settings.responseKey]

    # File naming
    dt_string = datetime.now().strftime("%H%M%d%m")
    settings.outfile = f"Subject{subdata[0]}_{dt_string}.csv"

    kb = keyboard.Keyboard()

    return win, kb, settings