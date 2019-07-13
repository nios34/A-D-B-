# -*- coding=UTF8 -*-
import os

# def __What_Is_My_API_Android_Version(API_Level):
#     Android_Version = \
#         [None, '1.0', '1.1', '1.5', '1.6', '2.0', '2.0.1', '2.1', '2.2-X', '2.3-1&2', '2.3-3+', '3.0', '3.1', '3.2-X', '4.0-1&2', '4.0-3+', '4.1-X', '4.2-X', '4.3-X', '4.4-X', '4.4W-X', '5.0-X', '5.1-X', '6.0-X', '7.0', '7.1-X', '8.0', '8.1', '9.0']

#     return [Android_Version[API_Level]]

def DISK_INFO():
    DK_INFO = {}
    DF = (((os.popen("adb shell df -h")).read()).split('\n')) ; DF.pop(0) ; DF.pop(-1)
    
    for i in range(len(DF)):
        DF[i] = DF[i].split() ; MO = DF[i][-1] ; DF[i].pop(-1)
        DK_INFO[MO] = DF[i]
        pass

    DK_INFO.setdefault('/data', ['?', '?', '?', '?', '?'])
    return DK_INFO

def BATTERY_INFO():
    BTR = (((os.popen("adb shell dumpsys battery")).read()).strip()).split('\n')
    
    # CLEAN ARRAY
    POP_LIST = []

    for i in range(len(BTR)):
        if (i == 0) or not(':' in BTR[i]):
            POP_LIST.append(i)
        else:
            BTR[i] = BTR[i].strip()
        pass

    POP_LIST.sort()
    POP_LIST.reverse()

    for i in POP_LIST: # POPING
        BTR.pop(i)
        pass
    # CLEAN OK

    # Convert
    for i in range(len(BTR)):
        BTR[i] = BTR[i].split(':')
        pass
    # Convert OK

    # CLEAN AGAIN
    for i in range(len(BTR)):
        BTR[i][1] = BTR[i][1].strip()
        pass
    # CLEAN OK

    # Convert AGAIN
    BTR_INFO = {}
    for i in range(len(BTR)):
        BTR_INFO[BTR[i][0]] = BTR[i][1]
        pass
    # Convert OK

    # BEAUTIFUL
    if BTR_INFO['status'] == str(2):
        BTR_INFO['C'] = 'CHARGING'
    else:
        BTR_INFO['C'] = 'NOT CHARGING'
        pass

    return BTR_INFO

def DEVICE_INFO():
    DEVICE = {}
    DEVICE.setdefault('d',0)
    DEVICE['Code'] = (((os.popen("adb shell getprop ro.product.name")).read()).strip()).capitalize()
    DEVICE['Brand'] = (((os.popen("adb shell getprop ro.product.brand")).read()).strip()).capitalize()
    DEVICE['Model'] = ((os.popen("adb shell getprop ro.product.model")).read()).strip()
    DEVICE['Serialno'] = ((os.popen("adb shell getprop ro.serialno")).read()).strip()
    DEVICE['DATA INFO'] = "%s available (%s USED)" % ((DISK_INFO()['/data'][3], DISK_INFO()['/data'][4]))
    DEVICE['API LEVEL'] = ((os.popen("adb shell getprop ro.build.version.sdk")).read()).strip()
    DEVICE['Android LEVEL'] = ((os.popen("adb shell getprop ro.build.version.release")).read()).strip()
    DEVICE['BATTERY LEVEL'] = '%s (%s)' % (BATTERY_INFO()['level'] + '%', BATTERY_INFO()['C'])
    return DEVICE

def LONG_OF_DEVICE_INFO():
    L = []
    for k,v in (DEVICE_INFO()).items():
        L.append(len(str(v))+len(str(k))+2)
        pass

    L.sort() ; L = L[-1]
    return L

__REQ = tuple((((os.popen("stty size")).read()).strip()).split())
TTY_SIZE = {'height': int(__REQ[0]), 'width': int(__REQ[1])}