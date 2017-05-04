import os
import inspect
from scripts.gui import GUI


if __name__ == "__main__":
    assets_path = os.path.join(os.path.dirname(os.path.abspath(inspect.stack()[0][1])), "assets")

    gui1 = GUI("ThePatchelist's PUBG Timer Notifiers", assets_path)
    gui1.run()
