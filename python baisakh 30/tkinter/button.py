import tkinter as tk

# setup
root_window = tk.Tk()
root_window.title("First GUI")  # set title
root_window.geometry("600x400")  # set size (width x height)


# a button


click_count = 0
label1_text = tk.StringVar()


def button_click():
    global click_count
    click_count += 1
    # print(f"You clicked the button! {click_count} times")
    label1_text.set(f"You clicked the button! {click_count} times")


button = tk.Button(
    root_window,
    text="Click me!",
    bg="green",
    fg="white",
    # command=lambda: print("You clicked the button!"),
    command=button_click,
)
button.pack()


label1_text.set("This is a label")
label1 = tk.Label(root_window, textvariable=label1_text)
label1.pack()


# main loop
root_window.mainloop()  # "Start the GUI, show the window, and wait for user interaction like button clicks, key presses, etc."
