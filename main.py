import qrcode
from PIL import Image
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *

from pathlib import Path
PATH = Path(__file__).parent / 'res'
PATHD = Path (__file__).parent / 'download'


class QrCodeGenerator (ttk.Frame):
    def __init__ (self, master):
        super().__init__(master, padding=(20,10))
        self.pack(fill=BOTH, expand=YES)

        #form inputs
        self.link = ttk.StringVar(value="")

        #form_header
        headerText = "QR CODE GENERATOR"
        headerLabel = ttk.Label(master=self, text=headerText, font=('TkDefaultFixed', 20), width=50)
        headerLabel.pack()

        #form entries
        self.create_form_entry("Link", self.link)
        self.create_button()


    def create_form_entry(self, label, variable):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)
    
        lbl = ttk.Label(master=container, text=label.title())
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(master=container, textvariable=variable)
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_button(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15,10))

        sub_btn = ttk.Button(master=container, text="Generate", command=self.qr_gen, bootstyle=SUCCESS, width=6)
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()
        
        cnl_btn = ttk.Button(master=container, text="Cancel", command=self.on_cancel, bootstyle=DANGER, width=6)
        cnl_btn.pack(side=RIGHT, padx=5)

    def qr_gen(self):
        str_to_qr = self.link.get()
        qr = qrcode.QRCode(version=2, box_size=10, border=4)
        qr.add_data(str_to_qr)
        qr.make(fit=True)
        qr_image = qr.make_image(fill="black", back_color="orange")
        
        qr_image.save(PATH / "qr_code.png")
        qr_image.save(PATHD / "qr_code.png")

        self.media = ttk.PhotoImage(file=PATH / 'qr_code.png')
        lbl_qrCode = ttk.Label(master=self, image=self.media)
        lbl_qrCode.pack(side=LEFT)


    def on_cancel(self):
        self.quit()

if __name__ == "__main__":

    app = ttk.Window("Data Entry", "superhero", resizable=(False, False))
    QrCodeGenerator(app)
    app.mainloop()