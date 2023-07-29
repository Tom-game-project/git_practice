import tkinter as tk

root = tk.Tk()
root.title("hello world")

label0 = tk.Label(
    root,
    text="""
hello world
""")
label0.pack()

label1 = tk.Label(
    root,
    text="蛇足"
)
label1.pack()

label2 = tk.Label(
    root,
    text="""
hello world2
"""
)
root.mainloop()
