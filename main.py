import pyautogui
from PIL import Image,ImageGrab ## pip install pillow
import time
# from numpy import asarray

## creating a function which will use in jumping

def hit(key):
    pyautogui.keyDown(key)
    return

## creating an rectangle which jumps over cactus for that we needed to
## create an black rectangle
def iscollide(data):
    for i in range(300,415):
        for j in range(410,563):
            if data[i,j]<100:
                hit("down")
                return
    
    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return       


if __name__ == "__main__":
    print("hey dino start in 3 sec")
    time.sleep(2)
    # hit('up')
    while True:
        # image= takescreenshot()
        image= ImageGrab.grab().convert('L')
        data= image.load()
        iscollide(data)
    # print(asarray(image))
    # for i in range(400,470):
    #     for j in range(500,500):
    #         data[i,j]=0


    # for i in range(30,190):
    #     for j in range(50, 90):
    #         data[i, j] = 100

    # image.show()        