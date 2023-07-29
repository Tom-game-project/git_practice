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
    text="""
hello world1
"""
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

label4 = tk.Label(
    root,
    text="""
hello worrld4
"""
)
label4.pack()

root.mainloop()
