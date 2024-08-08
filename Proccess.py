import webbrowser
import pyautogui as pg
import main
import re
import pyperclip
def extract_usernames_and_passwords(input_text):
    credentials = []
    pattern = r'یوزرنیم\s*:\s*:\s*(?P<username>\S+)\s*پسوورد\s*:\s*:\s*(?P<password>\S+)'

    matches = re.findall(pattern, input_text)

    for match in matches:
        username = match[0]
        password = match[1]
        credentials.append([username, password])

    return credentials

def openpar():
    print("X")
    webbrowser.open_new("https://gamekey98.ir/wp-admin/admin.php?page=wc-orders&status=wc-processing");
    main.ImgFind("darhal.png")
    pg.sleep(1)
    main.MoveToPic("darhal.png", True, 0.1)
    pg.leftClick()
    main.ImgFind("jozsef.png")
    pg.sleep(1)
    pg.leftClick()
    pg.hotkey("ctrl", "a")
    pg.sleep(0.5)
    pg.hotkey("ctrl", "c")
    pg.sleep(0.5)
    return extract_usernames_and_passwords(pyperclip.paste())

def steamcheck(data):
    user = data[0]
    password = data[1]
    webbrowser.open_new("https://help.steampowered.com/en/");
    main.ImgFind("helplogin.png")
    pg.sleep(1)
    main.MoveToPic("helplogin.png", True, 0.1)
    pg.leftClick()

    main.ImgFind("Mainsign.png")

    main.MoveToPic("Mainsign.png", True, 0.1)

    pg.write(data[0])
    pg.press('tab')
    pg.write(data[1])

    pg.leftClick()






def Pardazesh():
    print("X")
    datas = openpar()
    for data in datas:
        print(data)
        steamcheck(data)




if __name__ == '__main__':
    print("X")
    Pardazesh()


