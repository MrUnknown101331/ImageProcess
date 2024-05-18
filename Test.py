from screeninfo import get_monitors

monitors = get_monitors()
wScreen, hScreen = monitors[0].width, monitors[0].height

print(wScreen, hScreen)
