
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from conexion_maquinas import conexion_maquinas
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Pedro\Desktop\prueba\seleccionar_pa_co\build\assets\frame0")
from paramatros import parametros

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def parametros_co(window):
    canvas = Canvas(
        window,
        bg = "#EAEAEA",
        height = 1024,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        60.0,
        fill="#A5CAEA",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        72.0,
        33.0,
        image=image_image_1
    )

    canvas.create_rectangle(
        586.0,
        67.0,
        1440.0,
        1024.0,
        fill="#BDBFBF",
        outline="")

    canvas.create_rectangle(
        0.0,
        60.0,
        1454.0,
        127.0,
        fill="#A7A7A7",
        outline="")

    canvas.create_rectangle(
        0.0,
        189.0,
        602.0,
        1024.0,
        fill="#BDBFBF",
        outline="")

    canvas.create_text(
        500.0,
        76.0,
        anchor="nw",
        text="ENSAYO",
        fill="#FFFFFF",
        font=("Inika Bold", 30 * -1)
    )

    canvas.create_rectangle(
        0.0,
        117.0,
        1468.0,
        189.0,
        fill="#A5CAEA",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        1307.0,
        153.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        1382.0,
        34.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Toplevel(conexion_maquinas(window)),
        relief="flat"
    )
    button_1.place(
        x=205.0,
        y=355.0,
        width=464.0,
        height=230.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Toplevel(parametros(window)),
        relief="flat"
    )
    button_2.place(
        x=818.0,
        y=350.0,
        width=463.0,
        height=235.0
    )

    canvas.create_text(
        903.0,
        148.0,
        anchor="nw",
        text="INFORMACION",
        fill="#FFFFFF",
        font=("Inika Bold", 30 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
