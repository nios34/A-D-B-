import os
import INFO

def RUN_CMD_WITH_GRAPICA(command):
    EM = 'xterm'
    os.system('%s +ls -e \'%s\' 2>/dev/null &' % (EM, command))
    pass

def RUN_CMD_WITH_NO_GRAPICA(command):
    os.system('screen %s' % command)
    pass

def Is_grapica_on():
    if '' == os.popen("echo $DESKTOP_SESSION").read().strip():
        Result = False
    else:
        Result = True
        pass
    return Result

def OPEN_ADB_SHELL_AUTO(ZW):
    # if Is_grapica_on():
    #     RUN_CMD_SHELL_WITH_GRAPICA('adb shell')
    #     pass
    # else:
    RUN_CMD_WITH_NO_GRAPICA('adb shell')
        # pass
    pass