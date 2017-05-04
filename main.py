from scripts.gui import GUI
import ctypes
from ctypes import wintypes
import win32con


if __name__ == "__main__":
    user32 = ctypes.windll.user32

    gui1 = GUI("ThePatchelist's PUBG Timer Notifiers")

    '''
    def hotkey_callback():
        msg = wintypes.MSG()
        if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
            if msg.message == win32con.WM_HOTKEY:
                if msg.wParam == 1:
                    gui1.hotkey_received()
        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageA(ctypes.byref(msg))
        gui1.after(1, hotkey_callback)

    gui1.after(1, hotkey_callback)
    '''

    #gui1.hotkey_received()
    gui1.run()
