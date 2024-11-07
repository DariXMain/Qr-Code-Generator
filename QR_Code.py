import pyqrcode
from tkinter import * 
from tkinter import filedialog
win = Tk()
win.title("QRCODE Generator")
win.geometry("400x400")
win.resizable(False, False)

def generate_qr_code():
    qr_text = text.get("1.0","end-1c")
    if qr_text != "" and qr_text != " ":
        qr_code = pyqrcode.create(qr_text, error="H")
        location = filedialog.askdirectory()
        qr_code.png(f"{location}/{qr_text.replace("\n", "").replace("?", "").replace("!", "").replace(".", "").replace("@", "").replace(">", "").replace("<", "").replace("%", "").replace("^", "").replace("&", "").replace("*", "").replace("|", "").replace("/", "")}.png", scale_num.get())
        text.delete("1.0","end-1c")

text = Text(win, width=150, height=10)
text.pack(padx=10, pady=10)

scale_num = Scale(win, from_=2, to=50, orient=HORIZONTAL)
scale_num.pack(padx=52, pady=5, ipadx=100, anchor="nw", side="top")

generate = Button(win, text="Generate", width=10, height=1, command=generate_qr_code, bd=5)
generate.pack()

win.mainloop()
