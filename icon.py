import pystray
from PIL import Image
import subprocess


def on_activate(icon):
    # This function will be called when the user clicks on the system tray icon
    subprocess.Popen(['start', '/d', '.', 'cmd.exe', '/k', 'mode con cols=80 lines=25 & python main.py'], shell=True)



# Load an image to use as the system tray icon
image = Image.open("icon.ico")

# Create the system tray icon
icon = pystray.Icon("My App", image, "My App")
icon.menu = pystray.Menu(
    pystray.MenuItem("Open Shell", on_activate),
    pystray.MenuItem("Quit", lambda icon: icon.stop())
)

# Start the system tray icon
icon.run()