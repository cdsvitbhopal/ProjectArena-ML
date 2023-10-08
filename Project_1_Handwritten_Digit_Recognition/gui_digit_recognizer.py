from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np

model = load_model('mnist.h5')

def predict_digit(img):
    img = img.resize((28,28))
    img = img.convert('L')
    img = np.array(img)
    img = img.reshape(1,28,28,1)
    img = img/255.0
    res = model.predict([img])[0]
    return np.argmax(res), max(res), sorted(enumerate(res), key=lambda x: x[1], reverse=True)[:3]

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.x = self.y = 0
        
        self.canvas = tk.Canvas(self, width=300, height=300, bg = "white", cursor="cross")
        self.label = tk.Label(self, text="Draw a digit", font=("Helvetica", 48))
        self.result_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.classify_btn = tk.Button(self, text="Recognise", command=self.classify_handwriting)   
        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)
       
        self.canvas.grid(row=0, column=0, pady=2, sticky=W)
        self.label.grid(row=0, column=1,pady=2, padx=2)
        self.result_label.grid(row=1, column=0, columnspan=2, pady=2)
        self.classify_btn.grid(row=2, column=1, pady=2, padx=2)
        self.button_clear.grid(row=2, column=0, pady=2)
        
        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")
        self.result_label.config(text="")

    def classify_handwriting(self):
        HWND = self.canvas.winfo_id()
        rect = win32gui.GetWindowRect(HWND)
        a, b, c, d = rect
        rect = (a+4, b+4, c-4, d-4)
        im = ImageGrab.grab(rect)

        digit, acc, top3 = predict_digit(im)
        self.label.configure(text=str(digit))
        self.result_label.config(text=f"Top 3 Predictions:\n{top3[0][0]}: {top3[0][1]*100:.2f}%\n{top3[1][0]}: {top3[1][1]*100:.2f}%\n{top3[2][0]}: {top3[2][1]*100:.2f}%")

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 8
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')

app = App()
mainloop()
