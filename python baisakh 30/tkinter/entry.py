import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

left_sidebar = tk.Frame(
    root,
    bg="red",
    width=200,
).grid(row=0, column=0)


# # Make row 0 and 1 expandable vertically
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)

# # Make column 0 and 1 expandable horizontally
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# Make row 0 and column 0 expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.mainloop()
