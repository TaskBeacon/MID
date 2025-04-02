from .expsetup import Initialize
from .trialcontrol import GenTrialSeq
from .expcontrol import RunTask
import os
# Get the directory where __init__.py is located (which is TaskFunc)
taskfunc_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the img folder
img_path = os.path.join(taskfunc_dir, 'img')

