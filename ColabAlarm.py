# перемещает курсор по экрану, чтобы Google Colab не засыпал
# moves the cursor around the screen so that Google Colab does not fall asleep

import time
import pyautogui
from random import *

while True:
    pyautogui.moveTo(randint(100,200),randint(100,200) , 2)
    time.sleep(10)