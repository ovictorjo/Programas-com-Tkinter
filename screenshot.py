import pyautogui
from tkinter import*

root = Tk()
root.geometry("400x200")

def take():
    image = pyautogui.screenshot("screenshot.png")

l1 = Label(text="Screenshot gui APP",font=('arial',18,'bold'))
l1.pack(pady=10)

l1 = Label(text="Click Here", font=('arial',10,'bold'))
l1.pack(pady=10)

btn = Button(root,text="Click Me",command=take,font=('arial',12,'bold'),fg='green')
btn.pack(pady=10)

root.mainloop()
