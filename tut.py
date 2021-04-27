import pyautogui as pgui#pyautogui
# import time
# for i in range(5):
#     time.sleep(1)
#     print(pgui.position())#gives the current location of cursor
    
# pgui.moveTo(1100,200)#This w\ill move the cursor to the given position
# pgui.moveRel(100,100)#move the cursor reletive to the current position

# pgui.click(x=1100 ,y=200)#will click on the given position
# pgui.click(x=1100 ,y=200,button="right")
# pgui.click(x=1100 ,y=200,button="right",clicks=2,interval=0.5)
pgui.typewrite("this is a sentence")
pgui.press("enter",presses=2)
pgui.hotkey("ctrl","a")