from Tkinter import *

import os
import threading
import winsound
import webbrowser

from scripts.tkinter_helpers import TkRepeatingTask


class GUI(Tk):
    def __init__(self, title, asset_path):
        Tk.__init__(self)

        self.asset_path = asset_path

        self.resizable(width=False, height=False)
        self.wm_title(title)
        self.iconbitmap(os.path.join(self.asset_path, 'favicon.ico'))

        self.vcmd = (self.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.top_frame = Frame(self)
        self.upper_mid_frame = Frame(self)
        self.lower_mid_frame = Frame(self)
        self.bottom_frame = Frame(self)

        self.white_label_1_string = StringVar()
        self.white_label_2_string = StringVar()
        self.white_label_3_string = StringVar()
        self.white_label_4_string = StringVar()
        self.white_label_5_string = StringVar()
        self.white_label_6_string = StringVar()
        self.white_label_7_string = StringVar()
        self.blue_label_1_string = StringVar()
        self.blue_label_2_string = StringVar()
        self.blue_label_3_string = StringVar()
        self.blue_label_4_string = StringVar()
        self.blue_label_5_string = StringVar()
        self.blue_label_6_string = StringVar()
        self.blue_label_7_string = StringVar()


        # frame setup
        self.setup_top_frame()
        self.setup_upper_midframe()
        self.setup_lower_midframe()
        self.setup_bottom_frame()

        self.state = "white_label_1"

        self.white_label_1_timer   = 5 * 60
        self.blue_label_1_timer    = 5 * 60
        self.white_label_2_timer   = 3 * 60 + 20
        self.blue_label_2_timer    = 2 * 60 + 20
        self.white_label_3_timer   = 2 * 60 + 30
        self.blue_label_3_timer    = 1 * 60 + 30
        self.white_label_4_timer   = 2 * 60
        self.blue_label_4_timer    = 1 * 60
        self.white_label_5_timer   = 2 * 60
        self.blue_label_5_timer    = 0 * 60 + 40
        self.white_label_6_timer   = 1 * 60 + 30
        self.blue_label_6_timer    = 0 * 60 + 30
        self.white_label_7_timer   = 1 * 60 + 30
        self.blue_label_7_timer    = 0 * 60 + 20

        self.white_stage1_alarm_offset = None
        self.white_stage2_alarm_offset = None
        self.white_stage3_alarm_offset = None
        self.white_stage4_alarm_offset = None
        self.white_stage5_alarm_offset = None
        self.white_stage6_alarm_offset = None
        self.white_stage7_alarm_offset = None
        self.blue_stage1_alarm_offset = None
        self.blue_stage2_alarm_offset = None
        self.blue_stage3_alarm_offset = None
        self.blue_stage4_alarm_offset = None
        self.blue_stage5_alarm_offset = None
        self.blue_stage6_alarm_offset = None
        self.blue_stage7_alarm_offset = None

        self.timer = TkRepeatingTask(self, self.every_second, 1000)

        self.running = False
        self.draw_timers()

    def hyperlink_1(self, event):
        webbrowser.open_new(r"http://www.twitch.tv/thepatchelist")

    def hyperlink_2(self, event):
        webbrowser.open_new(r"http://www.twitter.com/thepatchelist")

    def hotkey_received(self):
        if not self.running:
            self.running = True
            #print "hotkey received"
            self.timer.start()
            #print "timer started"

    def apply_timers(self):
        self.button_1.configure(text="Applied!")
        if not self.white_entry_1.get() == "":
            self.white_stage1_alarm_offset = int(self.white_entry_1.get())
            self.white_entry_1.configure(fg="green", bg="black")

        if not self.white_entry_2.get() == "":
            self.white_stage2_alarm_offset = int(self.white_entry_2.get())
            self.white_entry_2.configure(fg="green", bg="black")

        if not self.white_entry_3.get() == "":
            self.white_stage3_alarm_offset = int(self.white_entry_3.get())
            self.white_entry_3.configure(fg="green", bg="black")

        if not self.white_entry_4.get() == "":
            self.white_stage4_alarm_offset = int(self.white_entry_4.get())
            self.white_entry_4.configure(fg="green", bg="black")

        if not self.white_entry_5.get() == "":
            self.white_stage5_alarm_offset = int(self.white_entry_5.get())
            self.white_entry_5.configure(fg="green", bg="black")
            
        if not self.white_entry_6.get() == "":
            self.white_stage6_alarm_offset = int(self.white_entry_6.get())
            self.white_entry_6.configure(fg="green", bg="black")
            
        if not self.white_entry_7.get() == "":
            self.white_stage7_alarm_offset = int(self.white_entry_7.get())
            self.white_entry_7.configure(fg="green", bg="black")
            
        if not self.blue_entry_1.get() == "":
            self.blue_stage1_alarm_offset = int(self.blue_entry_1.get())
            self.blue_entry_1.configure(fg="green", bg="black")
            
        if not self.blue_entry_2.get() == "":
            self.blue_stage2_alarm_offset = int(self.blue_entry_2.get())
            self.blue_entry_2.configure(fg="green", bg="black")
            
        if not self.blue_entry_3.get() == "":
            self.blue_stage3_alarm_offset = int(self.blue_entry_3.get())
            self.blue_entry_3.configure(fg="green", bg="black")
            
        if not self.blue_entry_4.get() == "":
            self.blue_stage4_alarm_offset = int(self.blue_entry_4.get())
            self.blue_entry_4.configure(fg="green", bg="black")
            
        if not self.blue_entry_5.get() == "":
            self.blue_stage5_alarm_offset = int(self.blue_entry_5.get())
            self.blue_entry_5.configure(fg="green", bg="black")
            
        if not self.blue_entry_6.get() == "":
            self.blue_stage6_alarm_offset = int(self.blue_entry_6.get())
            self.blue_entry_6.configure(fg="green", bg="black")
            
        if not self.blue_entry_7.get() == "":
            self.blue_stage7_alarm_offset = int(self.blue_entry_7.get())
            self.blue_entry_7.configure(fg="green", bg="black")

    def play_alarm_sound(self):
        soundthread = threading.Thread(target=winsound.PlaySound, args=(os.path.join(self.asset_path, 'alarm.wav'), winsound.SND_FILENAME))
        soundthread.start()

    def every_second(self):
        if self.state == "white_label_1":
            self.white_label_1_timer -= 1
            self.white_label_1.configure(fg="green", bg="black")
            if self.white_label_1_timer == self.white_stage1_alarm_offset:
                self.play_alarm_sound()
            if self.white_label_1_timer <= 0:
                self.white_label_1.configure(fg="red")
                self.state = "blue_label_1"

        elif self.state == "blue_label_1":
            self.blue_label_1_timer -= 1
            self.blue_label_1.configure(fg="green", bg="black")
            if self.blue_label_1_timer == self.blue_stage1_alarm_offset:
                self.play_alarm_sound()
            if self.blue_label_1_timer <= 0:
                self.blue_label_1.configure(fg="red")
                self.state = "white_label_2"

        elif self.state == "white_label_2":
            self.white_label_2_timer -= 1
            self.white_label_2.configure(fg="green", bg="black")
            if self.white_label_2_timer == self.white_stage2_alarm_offset:
                self.play_alarm_sound()
            if self.white_label_2_timer <= 0:
                self.white_label_2.configure(fg="red")
                self.state = "blue_label_2"

        elif self.state == "blue_label_2":
            self.blue_label_2_timer -= 1
            self.blue_label_2.configure(fg="green", bg="black")
            if self.blue_label_2_timer == self.blue_stage2_alarm_offset:
                self.play_alarm_sound()
            if self.blue_label_2_timer <= 0:
                self.blue_label_2.configure(fg="red")
                self.state = "white_label_3"

        elif self.state == "white_label_3":
            self.white_label_3_timer -= 1
            self.white_label_3.configure(fg="green", bg="black")
            if self.white_label_3_timer == self.white_stage3_alarm_offset:
                self.play_alarm_sound()
            if self.white_label_3_timer <= 0:
                self.white_label_3.configure(fg="red")
                self.state = "blue_label_3"

        elif self.state == "blue_label_3":
            self.blue_label_3_timer -= 1
            self.blue_label_3.configure(fg="green", bg="black")
            if self.blue_label_3_timer == self.blue_stage3_alarm_offset:
                self.play_alarm_sound()
            if self.blue_label_3_timer <= 0:
                self.blue_label_3.configure(fg="red")
                self.state = "white_label_4"

        elif self.state == "white_label_4":
            self.white_label_4_timer -= 1
            self.white_label_4.configure(fg="green", bg="black")
            if self.white_label_4_timer == self.white_stage4_alarm_offset:
                self.play_alarm_sound()
            if self.white_label_4_timer <= 0:
                self.white_label_4.configure(fg="red")
                self.state = "blue_label_4"

        elif self.state == "blue_label_4":
            self.blue_label_4_timer -= 1
            self.blue_label_4.configure(fg="green", bg="black")
            if self.blue_label_4_timer == self.blue_stage4_alarm_offset:
                self.play_alarm_sound()
            if self.blue_label_4_timer <= 0:
                self.blue_label_4.configure(fg="red")
                self.state = "white_label_5"

        elif self.state == "white_label_5":
            self.white_label_5_timer -= 1
            self.white_label_5.configure(fg="green", bg="black")
            if self.white_label_5_timer == self.white_stage5_alarm_offset:
                self.play_alarm_sound()
            if self.white_label_5_timer <= 0:
                self.white_label_5.configure(fg="red")
                self.state = "blue_label_5"

        elif self.state == "blue_label_5":
            self.blue_label_5_timer -= 1
            self.blue_label_5.configure(fg="green", bg="black")
            if self.blue_label_5_timer == self.blue_stage5_alarm_offset:
                self.play_alarm_sound()
            if self.blue_label_5_timer <= 0:
                self.blue_label_5.configure(fg="red")
                self.state = "white_label_6"

        elif self.state == "white_label_6":
            self.white_label_6_timer -= 1
            self.white_label_6.configure(fg="green", bg="black")
            if self.white_label_6_timer == self.white_stage6_alarm_offset:
                self.play_alarm_sound()
            if self.white_label_6_timer <= 0:
                self.white_label_6.configure(fg="red")
                self.state = "blue_label_6"

        elif self.state == "blue_label_6":
            self.blue_label_6_timer -= 1
            self.blue_label_6.configure(fg="green", bg="black")
            if self.blue_label_6_timer == self.blue_stage6_alarm_offset:
                self.play_alarm_sound()
            if self.blue_label_6_timer <= 0:
                self.blue_label_6.configure(fg="red")
                self.state = "white_label_7"

        elif self.state == "white_label_7":
            self.white_label_7_timer -= 1
            self.white_label_7.configure(fg="green", bg="black")
            if self.white_label_7_timer == self.white_stage7_alarm_offset:
                self.play_alarm_sound()
            if self.white_label_7_timer <= 0:
                self.white_label_7.configure(fg="red")
                self.state = "blue_label_7"

        elif self.state == "blue_label_7":
            self.blue_label_7_timer -= 1
            self.blue_label_7.configure(fg="green", bg="black")
            if self.blue_label_7_timer == self.blue_stage4_alarm_offset:
                self.play_alarm_sound()
            if self.blue_label_7_timer <= 0:
                self.blue_label_7.configure(fg="red")
                self.state = "FINISHED"

        self.draw_timers()


    def draw_timers(self):
        self.white_label_1_string.set(self.white_label_1_timer)
        self.white_label_2_string.set(self.white_label_2_timer)
        self.white_label_3_string.set(self.white_label_3_timer)
        self.white_label_4_string.set(self.white_label_4_timer)
        self.white_label_5_string.set(self.white_label_5_timer)
        self.white_label_6_string.set(self.white_label_6_timer)
        self.white_label_7_string.set(self.white_label_7_timer)

        self.blue_label_1_string.set(self.blue_label_1_timer)
        self.blue_label_2_string.set(self.blue_label_2_timer)
        self.blue_label_3_string.set(self.blue_label_3_timer)
        self.blue_label_4_string.set(self.blue_label_4_timer)
        self.blue_label_5_string.set(self.blue_label_5_timer)
        self.blue_label_6_string.set(self.blue_label_6_timer)
        self.blue_label_7_string.set(self.blue_label_7_timer)

    def run(self):

        self.mainloop()

    def setup_top_frame(self):
        # frames dividing the window
        self.top_frame.pack()

        title_label = Label(self.top_frame,
                            text="This tool helps you keep track of each stage of circles in PUBG. \nSee how long "
                                 "the circles run and add a time when you want to be notified.\n\n"
                                 "Insert a time in full seconds (120 = 2 minutes) and hit the Apply button.\n"
                                 "A sound will notify you when the remaining time has been reached.")

        title_label.grid(row=0, column=5, padx=(10, 10), pady=(10, 10))

    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if(action=="1"):
            if text in '0123456789':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True

    def setup_upper_midframe(self):
        self.upper_mid_frame.pack()

        # define labels
        notify_white_label = Label(self.upper_mid_frame, text="White Circle Timings")
        notify_blue_label = Label(self.upper_mid_frame, text="Blue Circle Timings")
        time_label = Label(self.upper_mid_frame, text="Time")
        #active_label = Label(self.upper_mid_frame, text=">")

        self.white_label_1 = Label(self.upper_mid_frame, textvariable=self.white_label_1_string, font=("Helvetica", 12))
        self.white_label_2 = Label(self.upper_mid_frame, textvariable=self.white_label_2_string, font=("Helvetica", 12))
        self.white_label_3 = Label(self.upper_mid_frame, textvariable=self.white_label_3_string, font=("Helvetica", 12))
        self.white_label_4 = Label(self.upper_mid_frame, textvariable=self.white_label_4_string, font=("Helvetica", 12))
        self.white_label_5 = Label(self.upper_mid_frame, textvariable=self.white_label_5_string, font=("Helvetica", 12))
        self.white_label_6 = Label(self.upper_mid_frame, textvariable=self.white_label_6_string, font=("Helvetica", 12))
        self.white_label_7 = Label(self.upper_mid_frame, textvariable=self.white_label_7_string, font=("Helvetica", 12))

        self.blue_label_1 = Label(self.upper_mid_frame, textvariable=self.blue_label_1_string, font=("Helvetica", 12))
        self.blue_label_2 = Label(self.upper_mid_frame, textvariable=self.blue_label_2_string, font=("Helvetica", 12))
        self.blue_label_3 = Label(self.upper_mid_frame, textvariable=self.blue_label_3_string, font=("Helvetica", 12))
        self.blue_label_4 = Label(self.upper_mid_frame, textvariable=self.blue_label_4_string, font=("Helvetica", 12))
        self.blue_label_5 = Label(self.upper_mid_frame, textvariable=self.blue_label_5_string, font=("Helvetica", 12))
        self.blue_label_6 = Label(self.upper_mid_frame, textvariable=self.blue_label_6_string, font=("Helvetica", 12))
        self.blue_label_7 = Label(self.upper_mid_frame, textvariable=self.blue_label_7_string, font=("Helvetica", 12))

        self.stage_label_1 = Label(self.upper_mid_frame, text="Stage 1", font=("Helvetica", 12))
        self.stage_label_2 = Label(self.upper_mid_frame, text="Stage 2", font=("Helvetica", 12))
        self.stage_label_3 = Label(self.upper_mid_frame, text="Stage 3", font=("Helvetica", 12))
        self.stage_label_4 = Label(self.upper_mid_frame, text="Stage 4", font=("Helvetica", 12))
        self.stage_label_5 = Label(self.upper_mid_frame, text="Stage 5", font=("Helvetica", 12))
        self.stage_label_6 = Label(self.upper_mid_frame, text="Stage 6", font=("Helvetica", 12))
        self.stage_label_7 = Label(self.upper_mid_frame, text="Stage 7", font=("Helvetica", 12))

        # define entry fields
        self.white_entry_1 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.white_entry_2 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.white_entry_3 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.white_entry_4 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.white_entry_5 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.white_entry_6 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.white_entry_7 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)

        self.blue_entry_1 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.blue_entry_2 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.blue_entry_3 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.blue_entry_4 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.blue_entry_5 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.blue_entry_6 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)
        self.blue_entry_7 = Entry(self.upper_mid_frame, validate="key", validatecommand=self.vcmd)

        self.white_entry_1.grid(row=1, column=1)
        self.white_entry_2.grid(row=3, column=1)
        self.white_entry_3.grid(row=5, column=1)
        self.white_entry_4.grid(row=7, column=1)
        self.white_entry_5.grid(row=9, column=1)
        self.white_entry_6.grid(row=11, column=1)
        self.white_entry_7.grid(row=13, column=1)

        notify_white_label.grid(row=0, column=1, padx=(10, 10), pady=(10, 10))

        self.white_label_1.grid(row=1, column=2)
        self.white_label_2.grid(row=3, column=2)
        self.white_label_3.grid(row=5, column=2)
        self.white_label_4.grid(row=7, column=2)
        self.white_label_5.grid(row=9, column=2)
        self.white_label_6.grid(row=11, column=2)
        self.white_label_7.grid(row=13, column=2, padx=(10, 10))

        self.stage_label_1.grid(row=1, column=4)
        self.stage_label_2.grid(row=3, column=4)
        self.stage_label_3.grid(row=5, column=4)
        self.stage_label_4.grid(row=7, column=4)
        self.stage_label_5.grid(row=9, column=4)
        self.stage_label_6.grid(row=11, column=4)
        self.stage_label_7.grid(row=13, column=4)

        time_label.grid(row=0, column=4, padx=(10, 10), pady=(10, 10))
        #active_label.grid(row=3, column=4)
        #self.seperate = self.Seperator(self.upper_mid_frame, orient=VERTICAL).grid(column=5, rowspan=7, sticky="ns")

        self.blue_label_1.grid(row=1, column=6)
        self.blue_label_2.grid(row=3, column=6)
        self.blue_label_3.grid(row=5, column=6)
        self.blue_label_4.grid(row=7, column=6)
        self.blue_label_5.grid(row=9, column=6)
        self.blue_label_6.grid(row=11, column=6)
        self.blue_label_7.grid(row=13, column=6, padx=(10, 10))

        self.blue_entry_1.grid(row=1, column=7)
        self.blue_entry_2.grid(row=3, column=7)
        self.blue_entry_3.grid(row=5, column=7)
        self.blue_entry_4.grid(row=7, column=7)
        self.blue_entry_5.grid(row=9, column=7)
        self.blue_entry_6.grid(row=11, column=7)
        self.blue_entry_7.grid(row=13, column=7)

        notify_blue_label.grid(row=0, column=7, padx=(10, 10), pady=(10, 10))

    def setup_lower_midframe(self):
        self.lower_mid_frame.pack()

        # define buttons
        self.button_1 = Button(self.lower_mid_frame, text="Apply Timers", command=self.apply_timers)
        self.button_2 = Button(self.lower_mid_frame, text="START", command=self.hotkey_received)
        #button_3 = Button(self.lower_mid_frame, text="Set Hotkey")
        self.button_4 = Button(self.lower_mid_frame, text="Exit", command=self.quit)

        # display buttons
        self.button_1.pack(side=LEFT, padx=(10, 10), pady=(10, 10))
        self.button_2.pack(side=LEFT, padx=(10, 10), pady=(10, 10))
        #button_3.pack(side=LEFT, padx=(10, 10), pady=(10, 10))
        self.button_4.pack(padx=(10, 10), pady=(10, 10))

    def setup_bottom_frame(self):
        self.bottom_frame.pack()

        self.support_label = Label(self, text="Support and Feedback")
        self.support_label.pack()
        self.link1 = Label(self, text="http://www.twitch.tv/ThePatchelist", fg="blue",
                          cursor="hand2")
        self.link2 = Label(self, text="http://www.twitter.com/ThePatchelist", fg="blue",
                           cursor="hand2")
        self.link1.pack()
        self.link1.bind("<Button-1>", self.hyperlink_1)
        self.link2.pack()
        self.link2.bind("<Button-1>", self.hyperlink_2)







