from asciimatics_FAST import *

KEY_MAPPING = {'KEY_UP': -204, 'KEY_DOWN': -206, 'KEY_TAB': -301, 'KEY_ENTER': 10} # , 'KEY_LEFT': -203, 'KEY_RIGHT': -205}
NOW_AT = 1

SETTINGS = []
SETTINGS_CALL = []
SETTINGS_CALL_PARMS = []

def REDRAW(obj, at, Datum, F = None):
    Del_line_down(obj, Datum)

    try:
        F(obj)
    except:
        pass

    for i in range(len(SETTINGS)):
        if i == (at - 1):
            Print_at_Center(obj, '> ' + SETTINGS[i] + ' <', Datum + i*2)
            pass
        else:
            Print_at_Center(obj, SETTINGS[i], Datum + i*2)
            pass
        pass
    pass

def KEY_EV_INIT(A, B, C):
    global SETTINGS
    global SETTINGS_CALL
    global SETTINGS_CALL_PARMS

    SETTINGS = A
    SETTINGS_CALL = B
    SETTINGS_CALL_PARMS = C
    pass

def Init(obj, Datum):
    REDRAW(obj, NOW_AT, Datum)
    obj.refresh()
    pass

# Fresh
def BackCall(obj, K, Datum, HookParm):
    global NOW_AT

    if K == 'KEY_UP':
        NOW_AT -= 1
    elif K == 'KEY_DOWN' or K == 'KEY_TAB':
        NOW_AT += 1
    elif K == 'KEY_ENTER':
        obj.close()
        SETTINGS_CALL[NOW_AT - 1](SETTINGS_CALL_PARMS[NOW_AT - 1])
        obj.open()
        pass
    
    if NOW_AT > len(SETTINGS):
        NOW_AT = 1
    elif NOW_AT < 1:
        NOW_AT = len(SETTINGS)
        pass

    REDRAW(obj, NOW_AT, Datum, HookParm)
    obj.refresh()

    pass

def KEY_EV(obj, obj2, PARM, PARM2 = None, to = 5):
    obj.wait_for_input(to)

    try:
        KEY = str(None)
        event = obj.get_event()
        for K,V in KEY_MAPPING.items():
            if V == event.key_code:
                KEY = K
                break
            pass
        if KEY != str(None):
            obj2(obj, KEY, PARM, PARM2)
            pass
        pass
    except AttributeError:
        pass
    pass