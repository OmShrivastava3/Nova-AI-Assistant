from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text


def User_send():
    send = entry1.get()
    Nova = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    if Nova is not None:
        text.insert(END, "Nova <-- " + str(Nova) + "\n")
    if Nova == "ok sir":
        root.destroy()


def ask():
    ask_val = spech_to_text.spech_to_text()
    Nova_val = action.Action(ask_val)
    text.insert(END, "Me --> " + ask_val + "\n")
    if Nova_val is not None:
        text.insert(END, "Nova <-- " + str(Nova_val) + "\n")
    if Nova_val == "ok sir":
        root.destroy()


def delete_text():
    text.delete("1.0", "end")


# Root window setup
root = Tk()
root.geometry("550x675")
root.title("NOVA")
root.resizable(False, False)

# Set background image
bg_image = Image.open("crazy.png")
bg_image = bg_image.resize((550, 675), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Text Label for NOVA (no background color, only text color)
Text_label = Label(root, text="NOVA", font=("Chiller", 32, "bold"), fg="blue")  # Blue text with no background
Text_label.place(x=230, y=50)

# Add a text widget
text = Text(root, font=("Chiller", 14), bg="white", fg="black", wrap=WORD)
text.place(x=100, y=375, width=375, height=100)

# Add an entry widget with increased size
entry1 = Entry(root, font=("Chiller", 14), justify=CENTER, bg="white", fg="black", relief=GROOVE)
entry1.place(x=75, y=500, width=400, height=35)  # Increased width and height

# Add a text button1
button1 = Button(root, text="ASK", bg="#DB7093", fg="white", font=("Chiller", 14, "bold"), pady=16, padx=40,
                 borderwidth=3, relief=SOLID, command=ask)
button1.place(x=70, y=575)

# Add a text button2
button2 = Button(root, text="Send", bg="#DB7093", fg="white", font=("Chiller", 14, "bold"), pady=16, padx=40,
                 borderwidth=3, relief=SOLID, command=User_send)
button2.place(x=400, y=575)

# Add a text button3
button3 = Button(root, text="Delete", bg="#DB7093", fg="white", font=("Chiller", 14, "bold"), pady=16, padx=40,
                 borderwidth=3, relief=SOLID, command=delete_text)
button3.place(x=225, y=575)
root.mainloop()
