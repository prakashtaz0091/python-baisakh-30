import tkinter as tk
import tkinter.ttk as ttk

root_window = tk.Tk()
root_window.title("Basic Calculator")  # set title
root_window.geometry("500x700")  # set size (width x height)
root_window.maxsize(500, 700)
root_window.minsize(500, 700)


# display box
style = ttk.Style()
style.configure(
    "Dark.TEntry",
    foreground="white",
    fieldbackground="grey",
    borderwidth=2,
    relief="sunken",
    padding=10,
)
style.configure(
    "LargeFont.TButton",
    font=("Monospace", 30),
)


def validate_input(action, current, proposed_value, actual_value):
    # print(
    #     f"ACTION: {action}, CURRENT: {current}, PROPOSED: {proposed_value}, ACTUAL: {actual_value}"
    # )
    if actual_value == "Error":
        return True
    else:
        if current == "Error":
            display_box.delete(0, tk.END)
            display_box.insert(0, actual_value)
        return not actual_value.isalpha()


display_box = ttk.Entry(
    root_window,
    font=("Monospace", 30),
    style="Dark.TEntry",
    validate="key",
    validatecommand=(root_window.register(validate_input), "%d", "%s", "%P", "%S"),
)
display_box.grid(row=0, column=0, sticky="nsew", columnspan=4)


# buttons
exclude_buttons = ("C", "DEL", "x²", "=", "%")


def button_click(value):
    if value not in exclude_buttons:
        display_box.insert(tk.END, value)

    if value == "=":
        error_occured = False
        try:
            result = eval(display_box.get())
        except Exception:
            error_occured = True

        if not error_occured:
            display_box.delete(0, tk.END)
            display_box.insert(0, str(result))
        else:
            display_box.delete(0, tk.END)
            display_box.insert(0, "Error")
    elif value == "C":
        display_box.delete(0, tk.END)
    elif value == "DEL":
        display_box.delete(len(display_box.get()) - 1, tk.END)
    elif value == "x²":
        display_box.insert(tk.END, "**2")
    elif value == "%":
        display_box.insert(tk.END, "/100")


keys = (
    ("C", "DEL", "x²", "%"),
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
)

for row in range(0, 5):
    for column in range(0, 4):
        new_button = ttk.Button(
            root_window,
            text=f"{keys[row][column]}",
            style="LargeFont.TButton",
            command=lambda x=keys[row][column]: button_click(x),
        )
        new_button.grid(row=row + 1, column=column, sticky="nsew")

for i in range(0, 5):
    root_window.grid_rowconfigure(i + 1, weight=1)
    root_window.grid_columnconfigure(i, weight=1)


root_window.mainloop()
