from YTManager import Downloader
from TextUI import TextUI

while True: 
    try:
        link = input('Put the YouTube link here ("exit" to exit). URL: \n>>>')
        if link == "exit":
            break
        obj = Downloader(link)
        print(TextUI.sendInfo(obj))
        if TextUI.sendQuestion():
            obj.download()
    except:
        print("An error occurred.")
