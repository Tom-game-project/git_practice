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
label2.pack()

label3 = tk.Label(
    root,
    text="""
hello world3
"""
)
label3.pack()
root.mainloop()
