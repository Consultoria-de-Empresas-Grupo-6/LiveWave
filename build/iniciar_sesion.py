
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sys

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from seleccionar_pa_co import parametros_co
from tkinter import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Pedro\Desktop\prueba\Inicio_sesion_Definitivo\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def iniciar_sesion(window):

    canvas = Canvas(
        bg = "#FFFFFF",
        height = 855,
        width = 1425,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        2.0,
        1440.0,
        62.0,
        fill="#4A90E2",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        72.0,
        31.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1382.0,
        32.0,
        image=image_image_2
    )

    canvas.create_rectangle(
        593.0,
        68.0,
        1440.0,
        1025.0,
        fill="#BDBFBF",
        outline="")

    canvas.create_rectangle(
        621.0,
        61.0,
        1468.0,
        1018.0,
        fill="#BDBFBF",
        outline="")

    canvas.create_rectangle(
        0.0,
        58.0,
        580.0,
        126.0,
        fill="#A7A7A7",
        outline="")

    canvas.create_rectangle(
        14.0,
        57.0,
        1454.0,
        125.0,
        fill="#A7A7A7",
        outline="")

    canvas.create_rectangle(
        0.0,
        124.0,
        602.0,
        1051.0,
        fill="#BDBFBF",
        outline="")

    canvas.create_text(
        595.0,
        75.0,
        anchor="nw",
        text="ENSAYO",
        fill="#FFFFFF",
        font=("Inika Bold", 30 * -1)
    )

    canvas.create_rectangle(
        2.0,
        115.0,
        1472.0,
        187.0,
        fill="#A5CAEA",
        outline="")

    canvas.create_rectangle(
        407.0,
        282.0,
        959.0,
        788.0,
        fill="#D9D9D9",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=654.0,
        y=588.0,
        width=301.0,
        height=49.0
    )

    canvas.create_text(
        554.0,
        291.0,
        anchor="nw",
        text="Iniciar sesion",
        fill="#000000",
        font=("Inika Bold", 33 * -1)
    )

    canvas.create_text(
        426.0,
        353.0,
        anchor="nw",
        text="Correo",
        fill="#000000",
        font=("Inika Bold", 32 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        685.5,
        432.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=446.0,
        y=414.0,
        width=479.0,
        height=34.0
    )

    canvas.create_text(
        427.0,
        483.0,
        anchor="nw",
        text="Contraseña",
        fill="#000000",
        font=("Inika Bold", 32 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        685.5,
        548.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        show="*"
    )
    entry_2.place(
        x=446.0,
        y=530.0,
        width=479.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Toplevel(parametros_co(window)),
        relief="flat"
    )
    button_2.place(
        x=538.0,
        y=655.0,
        width=364.0,
        height=94.0
    )

    window.resizable(False, False)
    window.mainloop()
