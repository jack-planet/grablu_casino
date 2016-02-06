# -*- coding: utf-8 -*-
import pyws as pyws
import winxpgui

def clickcard(changeflag):
    windowinfo = getwindowinfo()
    if windowinfo == False:
        return(False)
    x = windowinfo[0]
    y = windowinfo[1]
    sgain = windowinfo[2]
    for i in range(0,5):
        if changeflag[i] == 1:
            pyws.click(int(x+(i-2)*55*sgain),int(y+260*sgain),0)
    return(True)

def clickleft():
    windowinfo = getwindowinfo()
    if windowinfo == False:
        return(False)
    x = windowinfo[0]
    y = windowinfo[1]
    sgain = windowinfo[2]
    pyws.mmv(int(x-50*sgain),int(y+400*sgain))#for test
    #pyws.click(int(x-50*sgain),int(y+400*sgain),0)#use

def clickright():
    windowinfo = getwindowinfo()
    if windowinfo == False:
        return(False)
    x = windowinfo[0]
    y = windowinfo[1]
    sgain = windowinfo[2]
    pyws.mmv(int(x+50*sgain),int(y+400*sgain))#for test
    #pyws.click(int(x+50*sgain),int(y+400*sgain),0)#use

def clickcenter():
    windowinfo = getwindowinfo()
    if windowinfo == False:
        return(False)
    x = windowinfo[0]
    y = windowinfo[1]
    sgain = windowinfo[2]
    pyws.mmv(int(x),int(y+400*sgain))#for test
    #pyws.click(int(x),int(y+400*sgain),0)#use

def getwindowinfo():
    try:
        hwnd = pyws.getid("グランブルーファンタジー[ChromeApps版]",0)
    except:
        print("no window")
        return(False)
    print(hwnd)
    rect = winxpgui.GetWindowRect(hwnd)
    size = winxpgui.GetClientRect(hwnd)
    place = winxpgui.GetWindowPlacement(hwnd)
    if place[1]!=1:
        return(False)
    print(size)
    #if size[2]
    x = rect[0]+size[2]/2
    y = rect[1]
    if size[2] == 350:
        sgain = 1
    elif size[2] == 510:
        sgain = 1.46
    elif size[2] == 670:
        sgain = 1.9
    windowinfo = (x, y, sgain)
    return(windowinfo)

def main():
    #test 1
    #changeflag=(1,1,1,1,1)
    #clickcard(changeflag)
    
    #test 2
    clickcenter()
    
    #test 3
    #clickleft()
    
    #test 4
    #clickright()
    
if __name__ == "__main__":
    main()