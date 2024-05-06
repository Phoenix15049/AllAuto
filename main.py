import re
import webbrowser
import mss
import pyautogui as pg
import pytesseract
from PIL import Image
from plyer import notification
from pyautogui import *
import threading

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def discounter(price):
    """
    Calculates the discount based on the price.

    Args:
    - price (int or float): The price of the item.

    Returns:
    - int: The discount amount based on the price.

    This function calculates the discount amount based on the price of an item. It applies different discount rates
    """
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
    """
    Function to capture a screenshot of the screen.

    Uses the `mss` library to grab a screenshot and converts it to an `Image` object using `Pillow`.

    Returns:
        Image: An `Image` object representing the captured screenshot.
    """
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        return img


def read_text_from_screen(x, y, width, height):
    """
        Reads text from a specific region of the screen.

        Parameters:
        - x: The x-coordinate of the top-left corner of the region.
        - y: The y-coordinate of the top-left corner of the region.
        - width: The width of the region.
        - height: The height of the region.

        Returns:
        - text: The extracted text from the specified region.

        This function captures a screenshot of the entire screen and crops it to the specified region
        defined by the coordinates (x, y) and dimensions (width, height). The cropped image is then
        converted to grayscale and processed using Optical Character Recognition (OCR) to extract
        the text content. Finally, the extracted text is returned.
        """
    screenshot = capture_screenshot()
    roi = (x, y, width, height)
    cropped_img = screenshot.crop(roi)
    cropped_img = cropped_img.convert('L')
    text = pytesseract.image_to_string(cropped_img)
    return text


def openingvars(step, maxloc):
    """
        Opens variables on a page by finding and clicking each one.

        Args:
            step (int): The distance to move vertically between variable clicks.
            maxloc (int): The maximum vertical position to search for variables.

        Note:
            This function iteratively moves the mouse cursor upward on the screen
            by `step` pixels, clicking on each variable found until reaching
            a maximum vertical position of `maxloc`. The step size decreases
            alternately with each iteration to enhance precision.

        Requires:
            - pyautogui (imported as pg): A Python module for GUI automation.
              Install it via pip: `pip install pyautogui`.

        Example:
            # Set step size to 10 pixels and maximum position to 500 pixels
            openingvars(10, 500)
    """
    print("OPENINGVARS...")
    counter = pg.position().y
    stepdec = True
    while counter >= maxloc:
        pg.move(0, -step, 0.6)
        pg.leftClick()
        counter -= step
        if stepdec:
            step -= 1
            stepdec = False
        else:
            stepdec = True


def screenvarlocating():
    """
        Locates the position of product variables on the screen and opens them recursively until reaching the uppermost product.

        This function first identifies the location of the lower part of the product variables. If the 'BAction.png' image is found,
        indicating the presence of a product, it proceeds to determine the maximum location and opens the variables by calling
        'openingvars()' function. It repeats this process recursively until it reaches the upper part of the product, identified
        by the absence of the 'BAction.png' image. To confirm reaching the uppermost product, it checks for the presence of the
        'NMGH.png' image. Upon reaching the upper part, it scrolls, moves, and recalls itself to continue the process until
        all product variables are opened.
    """
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
    """
        Check if an image is present on the screen.

        Args:
            img (str): The filename of the image to search for.

        Returns:
            bool: True if the image is found, False otherwise.

        Raises:
            None

        This function takes the filename of an image and checks the screen for its presence.
        It constructs the full path to the image using the provided filename and attempts to locate the image on the screen using PyAutoGUI's locateCenterOnScreen function.
        The function sleeps for a short duration to allow the screen to stabilize before attempting the search. If the image is found, its location is returned, and True is returned.
        If the image is not found, a pg.ImageNotFoundException is caught, and False is returned.
    """
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
    """
        Function to modify the characteristics of a product variable to remove the discount
        and apply a new profit on it.

        Steps:
        1. Moves to the 'Laghvzaman.png' picture and clicks on it.
        2. Performs a series of key presses to navigate to the desired field.
        3. Clears the current discount value.
        4. Retrieves the main price of the product.
        5. Calculates the new price after removing the discount using the 'discounter' function.
        6. Applies a new profit on the product using the 'EmaalSood' function.
        7. Checks for the end condition.

        Note: This function assumes the existence of the following helper functions:
        - MoveToPic(filename, bool, float): Moves to the specified image and clicks on it.
        - press(key): Simulates a key press.
        - returnGN(): Retrieves the main price of the product.
        - discounter(price): Calculates the new price after removing the discount.
        - EmaalSood(price): Applies a new profit on the product.
        - isendingcheck(): Checks for the end condition.
        """
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
    """
        Function to adjust the price of a product according to the desired profit and update its features.

        Args:
        - MainPrice (int): The raw price of the product.

        Steps:
        1. Checks if the MainPrice is 10.
        2. If MainPrice is 10:
           - Searches for the 'sabett.png' image.
           - Enters the new price (10) into the appropriate field.
           - Confirms the changes by navigating through the UI.
        3. If MainPrice is not 10:
           - Searches for the 'darsad.png' image.
           - Enters the calculated price into the appropriate field.
           - Confirms the changes by navigating through the UI.

        Note: This function assumes the existence of the following helper functions:
        - press(key): Simulates a key press.
        - typewrite(text): Simulates typing the specified text.
        - pg.locateOnScreen(image, grayscale, confidence): Locates the specified image on the screen.
        - sleep(seconds): Pauses the execution for the specified duration.

        Note: This function utilizes PyAutoGUI library for GUI automation.
        """
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
    """
        Function to find and position the ZL image, performing discount removal for all products.



        Steps:
        1. Waits for a short duration to allow for screen stability.
        2. Checks if the 'ISLOADING.png' image is present, if so, executes 'isloadingcheck'.
        3. If not loading, waits for 7 seconds for screen stability.
        4. Scrolls the screen to facilitate image searching.
        5. Searches for the 'ZL.png' image within a defined region using 'ScrollPointFind'.
        6. Moves to the found 'ZL.png' image and adjusts its position.
        7. Locates screen variables using 'screenvarlocating'.
        8. Checks if all variables are fully opened with 'VarsFullOpenCheck'.
        9. Enters a loop until the 'ZT.png' image is found.
        10. If the 'PIC.png' image is found, scrolls to find the 'Laghvzaman.png' image and executes 'RemoveInsideDiscount'.
        11. Scrolls the screen in the opposite direction if 'ZT.png' is not found.
        12. Moves to the 'ZT.png' image once found.



        Note: This function assumes the existence of the following helper functions:
        - sleep(seconds): Pauses execution for the specified duration.
        - imagecheck(filename): Checks if the specified image is present on the screen.
        - isloadingcheck(): Executes loading check functionality.
        - scroll(distance): Scrolls the screen by the specified distance.
        - ScrollPointFind(filename, x_start, y_start, width, height, confidence, step): Searches for an image within a defined region.
        - MoveToPic(filename, bool, float): Moves to the specified image and clicks on it.
        - move(x, y): Moves the cursor by the specified distance.
        - screenvarlocating(): Locates screen variables.
        - VarsFullOpenCheck(): Checks if all variables are fully opened.
        - RemoveInsideDiscount(): Executes discount removal functionality.


        """
    sleep(0.5)
    if imagecheck('ISLOADING.png'):
        isloadingcheck()
    else:
        sleep(7)
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
    """
        Opens a web browser and searches for the specified game on the SteamDB website.

        Args:
        - GameName (str): The name of the game to search for on SteamDB.

        Steps:
        1. Constructs the URL for the SteamDB search page using the provided game name.
        2. Opens a new web browser window/tab with the constructed URL.
        3. Waits for a short duration (0.3 seconds) to allow the web page to load.

        Note: This function requires the 'webbrowser' module to be imported.

        Example:
        >>> SteamdbOpenSingle("Cyberpunk 2077")
        Opens the default web browser and searches for "Cyberpunk 2077" on SteamDB.
        """
    temp = "https://steamdb.info/search/?a=all&q=" + GameName
    webbrowser.open_new(temp)
    sleep(0.3)


def ScrollPointFind(img, top, left, width, height, confidence, scr):
    """
        Function to scroll on a page to find an image in the specified coordinates
        and scrolls until the image is found.

        Args:
        - img (str): The filename of the image to be found.
        - top (int): The top coordinate of the region to search for the image.
        - left (int): The left coordinate of the region to search for the image.
        - width (int): The width of the region to search for the image.
        - height (int): The height of the region to search for the image.
        - confidence (float): The confidence threshold for image matching.
        - scr (int): The number of scrolls to perform if the image is not found initially.

        Returns:
        - Loc (list): A list containing the coordinates of the found image [left, top].

        Note:
        - This function assumes the existence of the PyAutoGUI library (imported as 'pg').
        - The 'Assets\\Images' directory is expected to contain the images to be searched for.
        - If the image is not found initially, the function scrolls up by the specified amount ('scr') and continues the search.
        """
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


def ImgFind(img, center=False):
    """
        Function to locate an image on the screen.

        Args:
        - img (str): The name of the image file to search for.
        - center (bool, optional): If True, returns the center location of the image.
          If False, returns the location of the upper left corner of the image. Default is False.

        Returns:
        - list: A list containing the coordinates [x, y] of the found image.

        Notes:
        - This function continuously searches for the specified image on the screen until it is found.
        - The function uses the PyAutoGUI library for image recognition.
        - The 'grayscale' parameter is set to False to search for the image in color.
        - The 'confidence' parameter specifies the confidence threshold for image recognition.

        Raises:
        - ImageNotFoundException: If the specified image is not found on the screen.

        Example usage:
        >>> ImgFind('example.png', center=True)

        This example searches for the image named 'example.png' on the screen and returns its center location.
        """
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
    """
        Reads the content of a file specified by the given filepath.

        Args:
        - filepath (str): The path to the file to be read.

        Returns:
        - list: A list containing all the lines of the file, with newline characters removed.

        Note:
        - This function opens the specified file in read mode.
        - It reads each line of the file, removes the newline character at the end, and adds it to a list.
        - The list of lines is returned once all lines are processed.
        - If the file is not found or cannot be opened, this function will raise an exception.
        """
    f = open(filepath, "r")
    lines = f.readlines()
    AllLines = []
    for line in lines:
        AllLines.append(line.replace("\n", ""))
    return AllLines

def OpenLinks(links, DBNames=None, steamdbOpen=False, variablesOpen=False):  ## Main Opener
    """
        Function to open links based on given conditions.

        Args:
        - indexes (list): List of indexes indicating which links to open.
        - links (list): List of URLs to open.
        - DBNames (list, optional): List of database names corresponding to each link.
        - steamdbOpen (bool, optional): Flag indicating whether to open links in SteamDB.
        - variablesOpen (bool, optional): Flag indicating whether to open links using variables.

        Steps:
        1. Iterate through the indexes and open the corresponding links.
        2. If 'variablesOpen' is True:
           - If 'steamdbOpen' is True, open the game using 'OpenSingleGame' function and open SteamDB using 'SteamdbOpenSingle'.
           - If 'steamdbOpen' is False, only open the game using 'OpenSingleGame' function.
        3. If 'variablesOpen' is False:
           - If 'steamdbOpen' is True, open the game in the default web browser and open SteamDB using 'SteamdbOpenSingle'.
           - If 'steamdbOpen' is False, only open the game in the default web browser.

        Note:
        - 'OpenSingleGame' function opens a single game URL.
        - 'SteamdbOpenSingle' function opens a single SteamDB URL.
        - If 'DBNames' is provided, it should have the same length as 'indexes'.
        """
    if DBNames is None:
        DBNames = []
    for i in range(len(links)):
        if variablesOpen:
            if steamdbOpen:
                OpenSingleGame(links[i])
                sleep(0.5)
                SteamdbOpenSingle(DBNames[i])
            else:
                OpenSingleGame(links[i])
                sleep(0.5)
        else:
            if steamdbOpen:
                webbrowser.open_new(links[i])
                sleep(0.5)
                SteamdbOpenSingle(DBNames[i])
            else:
                webbrowser.open_new(links[i])
                sleep(0.5)


def ListLinks(SampleGn, allgamenames, allgamelinks):
    """
        Function to generate a list of links related to a given list of game names.

        Args:
        - SampleGn (list): List of game names.
        - allgamenames (list): List of all available game names.
        - allgamelinks (list): List of corresponding links for each game.

        Returns:
        - listlinks (list): List of links related to the provided game names.
        - notfound (list): List of game names for which links were not found.

        Steps:
        1. Initialize empty lists to store found links and game names not found.
        2. Iterate through each game name in the provided list.
        3. Attempt to find the index of the game name in the list of all game names.
        4. If found, append the corresponding link to the list of links.
        5. If not found, print a message indicating the game was not found and append the game name to the not found list.
        6. Return the list of links and the list of game names not found.

        Note: This function assumes that SampleGn, allgamenames, and allgamelinks are lists of the same length,
        with corresponding elements representing the same game.
        """
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
    """
        Function to move the mouse cursor to the position of a specified image on the screen.

        Parameters:
        - img (str): The filename of the image to locate on the screen.
        - center (bool): If True, moves the cursor to the center of the found image. Defaults to False.
        - dur (float): The duration (in seconds) of the mouse movement animation. Defaults to 0.0.

        Returns:
        - None

        Dependencies:
        - ImgFind(img, center): Helper function to locate the specified image on the screen.
        - moveTo(x, y, dur): PyAutoGUI function to move the mouse cursor to the specified coordinates.

        Notes:
        - This function utilizes PyAutoGUI library to interact with the mouse cursor.
        - It locates the specified image on the screen using the helper function ImgFind.
        - If center is set to True, the mouse cursor moves to the center of the found image.
        - The duration parameter controls the speed of the mouse movement animation.
        """
    pos = ImgFind(img, center)
    moveTo(pos[0], pos[1], dur)


def RemoveSingleDiscount(link):
    OpenSingleGame(link)
    find_ZL_and_position()


def OpenSingleGame(link):
    """
        Opens a game link on a web page and scrolls to the game variables section.

        Parameters:
        - link (str): The URL of the game to be opened.

        Steps:
        1. Opens the provided game link in a new web browser tab.
        2. Scrolls the webpage to find the '1st.png' image.
        3. Scrolls vertically to the designated coordinates to locate the '2nd.png' image.
        4. Scrolls further to ensure visibility of the game variables.
        5. Moves the mouse cursor to the '3rd.png' image and left-clicks.

        Note: This function assumes the existence of the following helper functions:
        - webbrowser.open_new(link): Opens the provided URL in a new web browser tab.
        - ImgFind(filename): Searches for the specified image on the webpage and scrolls if necessary.
        - pg.scroll(distance): Scrolls the webpage vertically by the given distance.
        - ScrollPointFind(filename, x, y, width, height, confidence, scroll_distance):
          Searches for the specified image within a scrollable area defined by coordinates and dimensions.
        - MoveToPic(filename, bool): Moves the mouse cursor to the specified image.
        - leftClick(): Performs a left-click action at the current mouse cursor position.
        """
    webbrowser.open_new(link)

    ImgFind('1st.png')
    pg.scroll(-3000)
    ScrollPointFind('2nd.png', 1390, 150, 330, 880, 0.8, 400)
    ScrollPointFind('2nd.png', 1483, 214, 237, 162, 0.8, 50)

    MoveToPic("3rd.png", True)
    leftClick()


def definelinks(isSingle=False, GameName=""):
    """
        Function to initialize the list of games and links.

        Steps:
        1. Reads the list of all game names from the 'GameNames.txt' file.
        2. Reads the list of all game links from the 'GameLinks.txt' file.
        3. Reads a sample game name from the 'GameName.txt' file.
        4. Returns the list of links corresponding to the sample game name.

        Note: This function assumes the existence of the following helper functions:
        - FileInside(filepath): Reads the contents of the specified file.
        - ListLinks(sample_game_name, all_game_names, all_game_links):
          Generates a list of links corresponding to the sample game name from
          the lists of all game names and links.

        Parameters:
        - None

        Returns:
        - list: A list of links corresponding to the sample game name.

        File Paths:
        - '.\\Assets\\Docs\\GameNames.txt': Contains a list of all game names.
        - '.\\Assets\\Docs\\GameLinks.txt': Contains a list of all game links.
        - '.\\GameName.txt': Contains a sample game name.

        Example Usage:
        >>> definelinks()
        ['https://example.com/game1', 'https://example.com/game2', ...]
        """
    AllGameNames = FileInside(".\\Assets\\Docs\\GameNames.txt")
    AllGameLinks = FileInside(".\\Assets\\Docs\\GameLinks.txt")
    SampleGN = FileInside(".\\GameName.txt")
    if isSingle:
        return ListLinks([GameName], AllGameNames, AllGameLinks)
    return ListLinks(SampleGN, AllGameNames, AllGameLinks)


def RemoveAllDiscount():
    """
        Function to remove discounts from all products.

        Steps:
        1. Retrieves the list of product links using the 'definelinks' function.
        2. Checks if any product links are found. If not, prints "GAMENOTFOUND" and exits.
        3. Iterates over each product link.
        4. Calls the 'RemoveSingleDiscount' function to remove the discount for each product.

        Note: This function assumes the existence of the following helper functions:
        - definelinks(): Retrieves the list of product links.
        - RemoveSingleDiscount(link): Removes the discount for a single product identified by the given link.
        """
    links = definelinks()
    if len(links[1]) != 0:
        print("GAMENOTFOUND")
    else:
        for i in range(len(links[0])):
            RemoveSingleDiscount(links[0][i])


def show_place(top, left, width, height):
    """
        Function to determine the range by taking a screenshot of the desired area using the
        built-in screenshot method in Windows.

        Parameters:
        - top: The top coordinate of the desired area.
        - left: The left coordinate of the desired area.
        - width: The width of the desired area.
        - height: The height of the desired area.

        Steps:
        1. Triggers the Windows built-in screenshot method by pressing the 'Win + Shift + S' hotkey combination.
        2. Searches for the 'tester.png' image on the screen.
        3. Moves the mouse cursor to the specified coordinates (top, left) with a 0.5-second delay.
        4. Drags the mouse cursor to define the area with the specified width and height, dragging for 2 seconds.

        Note: This function assumes the existence of the following helper functions:
        - hotkey(keys): Simulates a hotkey press combination.
        - ImgFind(image): Searches for the specified image on the screen.
        - moveTo(x, y, duration): Moves the mouse cursor to the specified coordinates with a specified duration.
        - drag(x, y, duration): Drags the mouse cursor from its current position by the specified offset (x, y) with a specified duration.
        """
    hotkey('win', 'shift', 's')
    ImgFind('tester.png')
    moveTo(top, left, 0.5)
    drag(width, height, 2)


def returnGN():
    """
        Function to retrieve the numerical value of the final price of a product from the screen.

        Steps:
        1. Waits for a brief period to ensure stability in screen updates.
        2. Locates the position of the 'GN.png' image on the screen.
        3. Calculates the coordinates and dimensions of the region around the located image.
        4. Utilizes a screenshot method to capture the area around the identified image.
        5. Extracts text from the captured region using optical character recognition (OCR).
        6. Converts the extracted text into a numerical value.
        7. Returns the numerical value of the final price.

        Note: This function relies on the existence of the following helper functions:
        - ImgFind(filename): Locates the position of the specified image on the screen.
        - read_text_from_screen(x, y, width, height): Reads text from the specified region of the screen.
        - StrtoNum(text): Converts the extracted text into a numerical value.
        - sleep(seconds): Pauses the execution for the specified duration.
        """
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
    """
        Converts a string containing numeric and non-numeric characters into an integer.

        Args:
        - string (str): The input string containing numeric and non-numeric characters.

        Returns:
        - int: The integer representation of the input string after removing non-numeric characters.

        Example:
        >>> StrtoNum("abc123def456")
        123456

        Notes:
        - This function uses regular expressions to remove non-numeric characters from the input string.
        - The resulting string is converted into an integer before being returned.
        - If the input string contains no numeric characters, the function returns 0.
        """
    result = re.sub(r'\D', '', str)
    return int(result)


def FullOpenAllGames(steamdbcheck=False, variablecheck=False):
    #    AllGameNames = FileInside(".\\Assets\\Docs\\GameNames.txt")
    #     AllGameLinks = FileInside(".\\Assets\\Docs\\GameLinks.txt")
    SampleGN = FileInside(".\\GameName.txt")
    links = definelinks()
    OpenLinks(links[0], SampleGN, steamdbcheck, variablecheck)


def FullOpenSingleGames(steamdbcheck=False, variablecheck=False, GameName=""):
    # AllGameNames = FileInside(".\\Assets\\Docs\\GameNames.txt")
    # AllGameLinks = FileInside(".\\Assets\\Docs\\GameLinks.txt")
    links = definelinks(True, GameName)
    OpenLinks(links[0], [GameName], steamdbcheck, variablecheck)


if __name__ == '__main__':
    AllGameNames = FileInside(".\\Assets\\Docs\\GameNames.txt")
    AllGameLinks = FileInside(".\\Assets\\Docs\\GameLinks.txt")
    SampleGN = FileInside(".\\GameName.txt")