from pytube import YouTube

class Downloader:
    def __init__(self, link):
        if len(link) == 11:
            link = "https://www.youtube.com/watch?v="+link
        self.obj = YouTube(link)
    
    def getName(self):
        return self.obj.title
    
    def getLength(self):
        seconds = self.obj.length
        minutes = int(seconds / 60)
        seconds -= minutes * 60
        hours = int(minutes / 60)
        minutes -= hours * 60
        if seconds < 10:
            seconds = "0"+str(seconds)
        if minutes < 10:
            minutes = "0"+str(minutes)
        if hours < 10:
            hours = "0"+str(hours)
        string = str(hours)+":"+str(minutes)+":"+str(seconds)
        return string
    

    def download(self):
            try:
                download = self.obj.streams.get_highest_resolution()
                download.download()
                print("The video was downloaded.\n")
            except:
                print("An error occurred.")

    