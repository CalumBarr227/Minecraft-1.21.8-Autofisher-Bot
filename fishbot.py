import pyautogui
import cv2
import numpy as np
import time

TEXT_TEMPLATE = "fish_splash_text2.png"
MATCH_THRESHOLD = 0.8
DELAY_AFTER_CLICK = 0.5

template = cv2.imread(TEXT_TEMPLATE, cv2.IMREAD_UNCHANGED)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w, h = template_gray.shape[::-1]

print("starting bot, switch to minecraft")
time.sleep(3)

while True:
    screenshot = pyautogui.screenshot()
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    gray_screenshot = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(gray_screenshot, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val >= MATCH_THRESHOLD:
        screen_width, screen_height = pyautogui.size()
        pyautogui.click(screen_width // 2, screen_height // 2, button='right')
        print("fish caught")
        time.sleep(DELAY_AFTER_CLICK)

        pyautogui.click(screen_width // 2, screen_height // 2, button='right')
        print("rod recast")
        time.sleep(DELAY_AFTER_CLICK)

    cv2.rectangle(screenshot_cv, max_loc, (max_loc[0]+w, max_loc[1]+h), (0,255,0), 2)
    cv2.imshow("fish splash text appeared", screenshot_cv)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
