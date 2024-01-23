import threading
import time
import random
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import keyboard

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Dimitar Petkov\PycharmProjects\pythonProject\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def afk_hotkey_event():
    afk_protection_toggle()


def tag_hotkey_event():
    tag_buddy_toggle()


def afk_protection_toggle():
    global afk_protection_active
    afk_protection_active = not afk_protection_active
    if afk_protection_active:
        afk_protection_thread.start()
        print("AFK STARTED")
    else:
        afk_protection_active = False  # Set the flag to stop the thread
        print("AFK STOPPED")


def afk_protection_start():
    while afk_protection_active:
        keyboard.press_and_release("space")
        time.sleep(random.randint(1, 3))
        print("AFK STARTED")


def afk_protection_stop():
    global afk_protection_active
    afk_protection_active = False
    keyboard.unhook_all()
    print("AFK STOPPED")


def tag_buddy_toggle():
    global tag_buddy_active
    tag_buddy_active = not tag_buddy_active
    if tag_buddy_active:
        tag_buddy_thread.start()
    else:
        keyboard.unhook_all()


def tag_buddy_start():
    while tag_buddy_active:
        keyboard.press_and_release("=")
        time.sleep(random.randint(1, 3))  # for testing delete for mega spam
        print("SPAMMING STARTED")


def tag_buddy_stop():
    global tag_buddy_active
    tag_buddy_active = False
    keyboard.unhook_all()
    print("SPAMMING STOPPED")


window = Tk()
window.geometry("800x600")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    300.0,
    image=image_image_1
)

canvas.create_text(
    186.0,
    29.0,
    anchor="nw",
    text="WoW Classic Helper ",
    fill="#FFFFFF",
    font=("BowlbyOneSC Regular", 36 * -1)
)

canvas.create_rectangle(
    399.0,
    94.0,
    400.0,
    600.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    81.0,
    148.0,
    anchor="nw",
    text="Afk Protection",
    fill="#FFFFFF",
    font=("BowlbyOneSC Regular", 24 * -1)
)

canvas.create_text(
    544.0,
    148.0,
    anchor="nw",
    text="Tag Buddy",
    fill="#FFFFFF",
    font=("BowlbyOneSC Regular", 24 * -1)
)

# canvas.create_text(
#     38.0,
#     227.0,
#     anchor="nw",
#     text="Spam Key",
#     fill="#FFFFFF",
#     font=("BowlbyOneSC Regular", 16 * -1)
# )

canvas.create_text(
    38.0,
    263.0,
    anchor="nw",
    text="Toggle On/Off",
    fill="#FFFFFF",
    font=("BowlbyOneSC Regular", 16 * -1)
)

# canvas.create_text(
#     38.0,
#     299.0,
#     anchor="nw",
#     text="Stop Key",
#     fill="#FFFFFF",
#     font=("BowlbyOneSC Regular", 16 * -1)
# )
#
# canvas.create_text(
#     499.0,
#     227.0,
#     anchor="nw",
#     text="Spam Key",
#     fill="#FFFFFF",
#     font=("BowlbyOneSC Regular", 16 * -1)
# )

canvas.create_text(
    499.0,
    263.0,
    anchor="nw",
    text="Toggle On/Off",
    fill="#FFFFFF",
    font=("BowlbyOneSC Regular", 16 * -1)
)

# canvas.create_text(
#     499.0,
#     299.0,
#     anchor="nw",
#     text="Stop Key",
#     fill="#FFFFFF",
#     font=("BowlbyOneSC Regular", 16 * -1)
# )

# button_image_1 = PhotoImage(
#     file=relative_to_assets("button_1.png"))
# button_1 = Button(
#     image=button_image_1,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_1 clicked"),
#     relief="flat"
# )
# button_1.place(
#     x=159.0,
#     y=224.0,
#     width=110.0,
#     height=31.0
# )

# button_image_2 = PhotoImage(
#     file=relative_to_assets("button_2.png"))
# button_2 = Button(
#     image=button_image_2,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_2 clicked"),
#     relief="flat"
# )
# button_2.place(
#     x=159.0,
#     y=296.0,
#     width=110.0,
#     height=31.0
# )

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=159.0,
    y=260.0,
    width=110.0,
    height=31.0
)

# button_image_4 = PhotoImage(
#     file=relative_to_assets("button_4.png"))
# button_4 = Button(
#     image=button_image_4,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_4 clicked"),
#     relief="flat"
# )
# button_4.place(
#     x=615.0,
#     y=224.0,
#     width=110.0,
#     height=31.0
# )
#
# button_image_5 = PhotoImage(
#     file=relative_to_assets("button_5.png"))
# button_5 = Button(
#     image=button_image_5,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_5 clicked"),
#     relief="flat"
# )
# button_5.place(
#     x=615.0,
#     y=296.0,
#     width=110.0,
#     height=31.0
# )

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=615.0,
    y=260.0,
    width=110.0,
    height=31.0
)

# New button functionalities
# button_1.config(command=afk_protection_start)
# button_2.config(command=afk_protection_stop)
button_3.config(command=afk_protection_toggle)

# button_4.config(command=tag_buddy_start)
# button_5.config(command=tag_buddy_stop)
button_6.config(command=tag_buddy_toggle)

# Hotkeys
keyboard.add_hotkey('shift+f2', afk_hotkey_event)
keyboard.add_hotkey('shift+f3', tag_hotkey_event)

# New thread objects
afk_protection_thread = threading.Thread(target=afk_protection_start, name="AfkProtectionThread")
tag_buddy_thread = threading.Thread(target=tag_buddy_start, name="TagBuddyThread")

afk_protection_active = False
tag_buddy_active = False

window.resizable(False, False)
window.mainloop()
