__author__ = 'Kingpin'
import Tkinter as tk


class KeyboardDetector:

    text = None
    delegate = None
    root = None

    def __init__(self, delegate=None):
        self.root = tk.Tk()
        self.delegate = delegate
        self.root.geometry('300x200')
        self.text = tk.Text(self.root, background='black', foreground='white', font=('Comic Sans MS', 12))
        self.text.pack()
        self.root.bind('<KeyPress>', self.onKeyPress)
        self.root.mainloop()

    def onKeyPress(self, event):
        self.text.insert('end', 'You pressed %s\n' % (event.char, ))
        self.text.see(tk.END)
        if self.delegate:
            self.delegate.key_pressed(event)

