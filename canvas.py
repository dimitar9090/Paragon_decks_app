from tkinter import *


def create_root():
    root = Tk()

    root.geometry("500x400")
    label = Label(root, text="PARAGON BUILDS")
    root.title("Paragon Builds")
    root.resizable(False, False)

    return root


def create_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = create_root()
frame = create_frame()