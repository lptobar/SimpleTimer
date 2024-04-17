import tkinter as tk
from pynput import keyboard

class Timer:
    def __init__(self):
        self.timer_id = None
        self.remaining_time = 0
        self.started = False

        self.root = tk.Tk()
        self.root.geometry('-0+0')
        self.root.wm_overrideredirect(True)
        self.root.wm_attributes('-topmost', True)
        self.root.wm_attributes('-transparentcolor', self.root['bg'])

        self.label = tk.Label(self.root, text=self.format_time(), font=('Helvetiva', 36), fg='white')
        self.label.pack(pady=20)

        self.listener = keyboard.Listener(on_press=self.start_timer)
        self.listener.start()
            
    def update_time(self):
        self.remaining_time += 1
        self.label.config(text=self.format_time())
        self.timer_id = self.root.after(1000, self.update_time)

    def format_time(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        return '{:02d}:{:02d}'.format(minutes, seconds)
    
    def start_timer(self, key):
        if key == keyboard.Key.f1:
            if self.started:
                self.root.after_cancel(self.timer_id)
                self.remaining_time = 0
                self.label.config(text=self.format_time())
            else:
                self.update_time()
            
            self.started = not self.started