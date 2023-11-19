class TextUI:
    def __init__(self):
        pass

    def sendInfo(obj):
        return f'\nThe video is titled: "{obj.getName()}".\nThe length is: {obj.getLength()}'
    
    def sendQuestion():
        answer = str(input("\nDo you want to download it? (Y/N).\n>>>"))
        if answer == "Y".lower():
            return True
        elif answer == "N".lower():
            return False
        else:
            print("Invalid answer.")
            return False