import subprocess
import os
import time

from asciimatics_FAST import *
from INFO import TTY_SIZE

HALF_H = int(TTY_SIZE['height']/2)
HALF_W = int(TTY_SIZE['width']/2)

def CK_CMD_ERROR_DISPLAY(obj, e):
    Print_at_Center(obj, '[                                                 ]', HALF_H - 1)
    Print_at_Center(obj, e, HALF_H - 1, color=COLOUR_RED, attr=A_BOLD)
    Print_at_Center(obj, 'PRESS ANY KEY TO BREAK!', HALF_H + 2, color=COLOUR_RED, attr=A_UNDERLINE)
    obj.refresh()
    obj.wait_for_input(10000)
    exit()
    pass

def CK_COMMAND(obj, command):
    Print_at_Center(obj, '[                                                 ]', HALF_H - 1)
    Print_at_Center(obj, 'CHECKING COMMAND "%s"' % command, HALF_H - 1)
    obj.refresh()

    Status = subprocess.getstatusoutput('which %s' % command)[0]

    if int(Status) == 1:
        CK_CMD_ERROR_DISPLAY(obj, 'Command "%s" not found!' % command)
    else:
        time.sleep(0.2)
        pass
    pass

def CK_DEVICE():
    P = subprocess.Popen(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    P.wait()

    Feedback, error = P.communicate()
    Feedback = Feedback.decode()
    Feedback = Feedback.replace('List of devices attached', '')

    # Feedback = ((((os.popen("adb  devices")).read()).replace('List of devices attached', '')).strip()).replace('\n', '')
    
    if 'device' in Feedback:
        return True
    else:
        return False

    pass