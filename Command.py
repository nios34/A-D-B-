import os
import time
import Check
import INFO
import Func

from Func import Is_grapica_on
from asciimatics_FAST import *
from INFO import TTY_SIZE
from MENU import *

HALF_H = int(TTY_SIZE['height']/2)
HALF_W = int(TTY_SIZE['width']/2)

DI = {}
BTRINFO = {}

def zw(N):
    pass

def DR_BTR(obj):
    Del_line_down(obj, len(BTRINFO.keys()) + 1)
    pass

def Battery_Manager(obj):
    BTRINFO = INFO.BATTERY_INFO()
    BTRINFO.pop('C')
    obj.clear()
    Print_BOX_at(obj, [[0,0], [TTY_SIZE['width'] - 1, len(BTRINFO.keys())]])
    I = -1
    for K, V in BTRINFO.items():
        I += 1
        if I != 0:
            Print_at(obj, " %s: %s" % (K, V), I, 1)
            pass
        pass
    obj.refresh()

    KEY_EV_INIT(['NM$L', 'STZNSLN', 'WTLKH', 'Quit'], [zw, zw, zw, exit], [0, 0, 0, 0])

    while True:
        KEY_EV(obj, BackCall, len(BTRINFO.keys()) + 1, DR_BTR)
        obj.refresh()
        pass

    pass

def Start_PREPAR(obj):
    Print_at_Center(obj, 'Welcome to A!D!B!', 1)
    Print_at_Center(obj, 'This PROGRAM is a tool for the adb debug and the Android flashing,', 3)
    Print_at_Center(obj, 'And it is under GPL3.0.', 4)
    Print_at_Center(obj, 'If you found some bug, you can report in "https://github.com/Geeks-alliance/A!D!B/issus".', 6, attr=A_UNDERLINE)
    Print_at_Center(obj, 'Thanks for your using.', 8)
    Print_at_Center(obj, 'Enjoy!', 9)
    Print_at_Center(obj, 'To continue, Press any key or Wait 5 secons!', 11, COLOUR_RED, attr=A_REVERSE)
    obj.refresh()
    obj.wait_for_input(5)
    obj.get_key()
    pass

def Start_CHECK(obj):
    obj.clear()
    Print_at_Center(obj, 'WE ARE CHECKING SOMETHING NOW, PLEASE WAITING...', HALF_H - 3, bg=COLOUR_CYAN, attr=A_BOLD)
    Check.CK_COMMAND(obj, 'adb')
    Check.CK_COMMAND(obj, 'fastboot')
    Check.CK_COMMAND(obj, 'zip')
    Check.CK_COMMAND(obj, 'unzip')
    Check.CK_COMMAND(obj, 'screen')
    # if Is_grapica_on():
    #     Check.CK_COMMAND(obj, 'xterm')
    Print_at_Center(obj, '[                                                 ]', HALF_H - 1, bg=COLOUR_GREEN)
    Print_at_Center(obj, 'ALL SUCESS', HALF_H - 1, bg=COLOUR_GREEN, attr=A_BOLD)
    obj.refresh()
    time.sleep(2)
    pass

def Wait_for_DEVICE(obj):
    global DI

    if not Check.CK_DEVICE():
        obj.clear()
        Print_at_Center(obj, 'WAITING FOR YOUR DEVICE...', HALF_H - 1, bg=COLOUR_CYAN, attr=A_BOLD)
        Print_at_Center(obj, 'Please connect the device to your computer!', HALF_H + 1)
        obj.refresh()
        while True:
            time.sleep(1)
            if Check.CK_DEVICE():
                obj.clear()
                Print_at_Center(obj, 'WAITING FOR YOUR DEVICE...', HALF_H - 1, bg=COLOUR_CYAN, attr=A_BOLD)
                Print_at_Center(obj, 'DEVICE(%s) FOUND!' % INFO.DEVICE_INFO()['Code'], HALF_H + 1, bg=COLOUR_GREEN, attr=A_BOLD)
                obj.refresh()
                time.sleep(2)
                break
            pass

    DI = INFO.DEVICE_INFO()
    pass

def DR(obj):
    global DI

    # Print_BOX_at(obj, [[0,0], [INFO.LONG_OF_DEVICE_INFO() + 3,9]])
    Print_BOX_at(obj, [[0,0], [TTY_SIZE['width'] - 1,9]])

    I = -1
    for K, V in DI.items():
        I += 1
        if I != 0:
            Print_at(obj, " %s: %s" % (K, V), I, 1)
            pass
        pass
    
    Print_at_Center(obj, "Press Tab to toggle the option", TTY_SIZE['height'] - 1)
    pass

def Main_menu(obj):
    # Print_AT_Center(obj, str(INFO.DEVICE_INFO().values()), HALF_H - 1, bg=COLOUR_CYAN, attr=A_BOLD)
    DR(obj)
    obj.refresh()

    Datum = 11

    KEY_EV_INIT(['Go to the device\'s shell', 'Install APK file', 'Battery manager', 'Quit'], [Func.OPEN_ADB_SHELL_AUTO, Func.RUN_CMD_WITH_NO_GRAPICA, Battery_Manager, exit], [None, 'screen Script/APK_to_device.sh', obj, 0])

    while True:
        KEY_EV(obj, BackCall, Datum, zw)
        obj.refresh()
        pass
    pass