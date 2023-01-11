import pyautogui

print('Press Ctrl-C to quit.')

try:
    while True:
        x, y = pyautogui.position()
        x = x * 2
        y = y * 2
        positionStr = str(x).rjust(4) + ', ' +  str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')
# Small program shamelessly stolen from pyautogui's documentation page at: https://pyautogui.readthedocs.io/en/latest/mouse.html
