import pyautogui
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.sleep(3)
pyautogui.write('jw.org')
pyautogui.press('enter')
pyautogui.PAUSE = 2
pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://wol.jw.org/pt/wol/h/r5/lp-t')
pyautogui.press('enter')