import pyautogui
import time


def getWindowsList():
    windowsList = []
    allWindows = pyautogui.getAllTitles()

    for window in allWindows:
        if window == "":
            continue

        windowsList.append(window)

    return windowsList


def switchTo(window):
    window.activate()
    window.restore()
    if window.isMaximized is False:
        window.maximize()


def altTab():
    pyautogui.keyDown('alt')
    time.sleep(.1)
    pyautogui.press('tab')
    time.sleep(.1)
    pyautogui.keyUp('alt')


# def main():
#     # Main function
#     print("Starting setup...")
#     print("Updating list of windows...\n")
#     updateCurrentWindows()
#     print(getAllWindows())


# def updateCurrentWindows():
#     # Function to update the list of current windows, and write into windows.txt

#     # Opens an emptied file to be appended to
#     open("windows.txt", "w").close()
#     file = open("windows.txt", "a")

#     allWindows = pag.getAllTitles()

#     for window in allWindows:
#         if window == "":
#             continue

#         try:
#             file.write(window + "\n")
#         except UnicodeEncodeError:
#             encodedWindow = window.encode('utf8')
#             decodedWindow = encodedWindow.decode('ascii', 'ignore')
#             file.write(decodedWindow + "\n")

#     file.close()
#     print("File (windows.txt) updated!\n")


# def getAllWindows():
#     # Function that reads from windows.txt, and returns a list of all windows
#     file = open("windows.txt", "r")
#     content = file.readlines()
#     windowsList = []
#     for line in content:
#         window = line.strip("\n")
#         windowsList.append(window)

#     return(windowsList)


# main()
