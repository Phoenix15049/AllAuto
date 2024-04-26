import webbrowser
from pyautogui import *
import pyautogui as pg
import mss
from PIL import Image
from plyer import notification
from win10toast import ToastNotifier
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def discounter(price):
    if price >= 900000:
        return 10
    elif 900000 > price >= 800000:
        return 95000
    elif 800000 > price >= 700000:
        return 90000
    elif 700000 > price >= 600000:
        return 85000
    elif 600000 > price >= 500000:
        return 80000
    elif 500000 > price >= 400000:
        return 75000
    elif 400000 > price >= 300000:
        return 70000
    elif 300000 > price >= 200000:
        return 60000
    elif 200000 > price >= 150000:
        return 50000
    elif 150000 > price >= 100000:
        return 40000
    elif 100000 > price >= 50000:
        return 30000
    elif 50000 > price >= 0:
        return 25000


def capture_screenshot():
    with mss.mss() as sct:
        # Capture the entire screen
        monitor = sct.monitors[0]
        screenshot = sct.grab(monitor)

        # Convert the screenshot to PIL image format
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        return img


def read_text_from_screen(x, y, width, height):
    # Take a screenshot of the screen
    screenshot = capture_screenshot()

    # Define the region of interest
    roi = (x, y, width, height)
    # Crop the screenshot to the defined ROI
    cropped_img = screenshot.crop(roi)
    # cropped_img.show()
    # Convert the cropped image to grayscale
    cropped_img = cropped_img.convert('L')

    # Use Tesseract OCR to extract text from the cropped image
    text = pytesseract.image_to_string(cropped_img)

    return text


def openingvars(step, maxloc):
    print("OPENINGVARS...")
    counter = pg.position().y
    stepdec = True
    while counter >= maxloc:
        pg.move(0, -step, 0.6)
        pg.leftClick()  # BIGGGGGGGGGGGGGGGGGGGGGGG COMEEEEEEEEEEEEENTTTTTTTTTTTTTTTTTTTTTTTT BIG COMMENT
        counter -= step
        if stepdec:
            step -= 1
            stepdec = False
        else:
            stepdec = True


def screenvarlocating():
    mouse = position()
    if imagecheck('BAction.png'):
        print("BACTION FOUND")
        maxloc = ImgFind('BAction.png', True)[1]
        maxloc += 30
        step = 60
        openingvars(step, maxloc)
        print(maxloc)
    else:
        print("BACTION NOTFOUND")
        maxloc = ImgFind('NMGH.png', True)[1]
        print(maxloc)
        step = 60
        openingvars(step, maxloc)
        scroll(300)
        sleep(0.1)
        move(0, 320, 0.6)
        screenvarlocating()


def imagecheck(img):
    imgadr = "Assets\\Images\\" + img
    try:
        sleep(0.1)
        location = pg.locateCenterOnScreen(imgadr, grayscale=False, confidence=0.8)
        print(img + " Found.")
        return True

    except pg.ImageNotFoundException:
        print('ImageNotFoundException: image not found')
        return False


def isloadingcheck():
    while imagecheck('ISLOADING.png'):
        print("is Loading")


def isendingcheck():
    while not imagecheck('ENDTEST.png'):
        print("is Ending")


def VarsFullOpenCheck():
    while imagecheck('FullCheck.png'):
        print("is Loading")


def RemoveInsideDiscount():
    MoveToPic('Laghvzaman.png', True, 0.1)
    pg.leftClick()
    for i in range(8):
        press('tab')
    press('backspace')

    mainprice = returnGN()
    MainPrice = discounter(mainprice)
    EmaalSood(MainPrice)
    isendingcheck()


def EmaalSood(MainPrice):
    if MainPrice == 10:
        img = 'sabett.png'
        imgadr = "Assets\\Images\\" + img
        sleep(0.1)
        press('tab')
        typewrite("10")
        try:
            location = pg.locateOnScreen(imgadr, grayscale=False, confidence=0.8)
            sleep(0.1)
            press('tab')
            press('enter')
            press('up')
            press('enter')
            sleep(0.1)


        except pg.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
            sleep(0.1)



    else:
        print("Not10")
        img = 'darsad.png'
        imgadr = "Assets\\Images\\" + img
        sleep(0.1)
        press('tab')
        pg.write(str(MainPrice))
        try:
            location = pg.locateOnScreen(imgadr, grayscale=False, confidence=0.8)
            sleep(0.1)
            press('tab')
            press('enter')
            press('down')
            press('enter')
            sleep(0.1)

        except pg.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
            sleep(0.1)


def find_ZL_and_position():
    sleep(0.5)
    if imagecheck('ISLOADING.png'):
        isloadingcheck()
    else:
        sleep(7)
    # move(50, 0, 0.1)
    #
    # sleep(1)
    scroll(300)
    ScrollPointFind('ZL.png', 1234, 580, 219, 412, 0.8, 30)
    MoveToPic('ZL.png', True, 0.3)
    move(50, 0)
    screenvarlocating()
    VarsFullOpenCheck()
    sleep(0.5)
    while not imagecheck('ZT.png'):
        if imagecheck('PIC.png'):
            ScrollPointFind('Laghvzaman.png', 620, 223, 106, 120, 0.8, 30)
            sleep(0.4)
            print("X")
            RemoveInsideDiscount()
            sleep(0.8)
        scroll(-450)

    MoveToPic('ZT.png', True, 0.6)


def SteamdbOpenSingle(GameName):
    temp = "https://steamdb.info/search/?a=all&q=" + GameName
    webbrowser.open_new(temp)
    sleep(0.3)


def ScrollPointFind(img, top, left, width, height, confidence, scr):
    Notfound = True
    Loc = [0, 0]
    while Notfound:
        try:
            imgadr = "Assets\\Images\\" + img
            location = pg.locateOnScreen(imgadr, grayscale=False, region=(top, left, width, height),
                                         confidence=confidence)
            print(location)
            print(location.left, location.top)
            Loc[0] = location.left
            Loc[1] = location.top
            print('DoingFound found')
            Notfound = False
            return Loc

        except pg.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
            pg.scroll(-scr)


def Imgcheck(img):
    try:
        imgadr = "Assets\\Images\\" + img
        sleep(0.1)
        location = pg.locateCenterOnScreen(imgadr, grayscale=False, confidence=0.8)
        print(img + " Found.")
        return True

    except pg.ImageNotFoundException:
        print('ImageNotFoundException: image not found')
        return False


def ImgFind(img, center=False):
    Notfound = True
    Loc = [0, 0]
    while Notfound:
        try:
            imgadr = "Assets\\Images\\" + img
            if center:
                location = pg.locateCenterOnScreen(imgadr, grayscale=False, confidence=0.8)
                Loc[0] = location.x
                Loc[1] = location.y
            else:
                location = pg.locateOnScreen(imgadr, grayscale=False, confidence=0.8)
                Loc[0] = location.left
                Loc[1] = location.top

            print(img + ' found')
            Notfound = False
            return Loc

        except pg.ImageNotFoundException:
            print('ImageNotFoundException: image not found')
            sleep(0.5)


def FileInside(filepath):
    f = open(filepath, "r")
    lines = f.readlines()
    AllLines = []
    for line in lines:
        AllLines.append(line.replace("\n", ""))
    return AllLines


def GameLinkIndex(sample, gamelist):  ## Temp
    indexes = []
    for i in range(len(sample)):
        temp = sample[i]
        indexes.append(gamelist.index(temp))
    return indexes


def OpenLinks(indexes, links, DBNames=None, DB=False):  ## Temp
    if DBNames is None:
        DBNames = []
    for i in range(len(indexes)):
        if DB:
            webbrowser.open_new(links[indexes[i]])
            sleep(0.5)
            SteamdbOpenSingle(DBNames[i])
        else:
            webbrowser.open_new(links[indexes[i]])
            sleep(0.5)


def ListLinks(SampleGn, allgamenames, allgamelinks):
    listlinks = []
    notfound = []
    for i in range(len(SampleGn)):

        temp = SampleGn[i]

        try:
            index = allgamenames.index(temp)
            listlinks.append(allgamelinks[index])

        except:
            print(temp)
            notfound.append(temp)
            print("GAME NOT FOUND !")

    return listlinks, notfound


def MoveToPic(img, center=False, dur=0.0):
    pos = ImgFind(img, center)
    moveTo(pos[0], pos[1], dur)


def RemoveSingleDiscount(link):
    OpenSingleGame(link)
    find_ZL_and_position()


def OpenSingleGame(link):
    webbrowser.open_new(link)

    ImgFind('1st.png')
    pg.scroll(-3000)
    ScrollPointFind('2nd.png', 1390, 150, 330, 880, 0.8, 400)
    ScrollPointFind('2nd.png', 1483, 214, 237, 162, 0.8, 50)

    MoveToPic("3rd.png", True)
    leftClick()


def OpenAllGames(steamdb=False):
    AllGameNames = FileInside(".\\Assets\\Docs\\GameNames.txt")
    AllGameLinks = FileInside(".\\Assets\\Docs\\GameLinks.txt")
    SampleGN = FileInside(".\\GameName.txt")

    links = ListLinks(SampleGN, AllGameNames, AllGameLinks)
    if len(links[1]) != 0:
        print("GAMENOTFOUND")
    else:
        for i in range(len(links[0])):
            if steamdb:
                OpenSingleGame(links[0][i])
                sleep(0.5)
                SteamdbOpenSingle(SampleGN[i])
            else:
                OpenSingleGame(links[0][i])


def RemoveAllDiscount():
    AllGameNames = FileInside(".\\Assets\\Docs\\GameNames.txt")
    AllGameLinks = FileInside(".\\Assets\\Docs\\GameLinks.txt")
    SampleGN = FileInside(".\\GameName.txt")

    links = ListLinks(SampleGN, AllGameNames, AllGameLinks)
    if len(links[1]) != 0:
        print("GAMENOTFOUND")
    else:
        for i in range(len(links[0])):
            RemoveSingleDiscount(links[0][i])


def show_notification2():
    title = "Notification Title"
    message = "This is a notification message"
    # You can set any custom icon image path here
    # You need to have the image file on your system
    # If not set, it will default to the platform icon
    # icon = "path/to/icon.png"

    # Display notification
    notification.notify(
        title=title,
        message=message,
        timeout=5,  # Timeout in seconds
        # app_icon=icon,  # Optionally, you can set a custom icon
    )


def show_place(top, left, width, height):
    hotkey('win', 'shift', 's')
    ImgFind('tester.png')
    moveTo(top, left, 0.5)
    drag(width, height, 2)


def returnGN():
    sleep(0.5)
    loc = ImgFind('GN.png')
    print(loc)
    x, y = loc[0] - 130, loc[1]
    width, height = loc[0], loc[1] + 26  # Adjust width and height according to your requirement
    extracted_text = read_text_from_screen(x, y, width, height)
    print("Extracted Text:", extracted_text)
    price = StrtoNum(extracted_text)
    print(price)
    return price


def StrtoNum(str):
    result = re.sub(r'\D', '', str)
    return int(result)


if __name__ == '__main__':
    AllGameNames = FileInside(".\\Assets\\Docs\\GameNames.txt")
    AllGameLinks = FileInside(".\\Assets\\Docs\\GameLinks.txt")
    SampleGN = FileInside(".\\GameName.txt")

#    OpenLinks(GameLinkIndex(SampleGN, AllGameNames), AllGameLinks, SampleGN, True)
    RemoveAllDiscount()
#    sleep(5)
#    RemoveInsideDiscount()

# returnGN()

# â€™
