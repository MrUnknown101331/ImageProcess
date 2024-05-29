from screeninfo import get_monitors

for monitor in get_monitors():
    wScreen, hScreen = monitor.width, monitor.height
    print(wScreen, hScreen)
