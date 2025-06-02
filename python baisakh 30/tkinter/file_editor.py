import tkinter as tk
import tkinter.ttk as ttk

# setup
root_window = tk.Tk()
root_window.title("First GUI")  # set title
root_window.geometry("1920x1080")  # set size (width x height)


# vars
error_message = tk.StringVar()
success_message = tk.StringVar()
file_content = tk.StringVar()

file_name = tk.Entry(root_window, width=500, font=("Monospace", 25))
file_name.pack()


def read_file():
    if file_name.get() == "":
        error_message.set("Please enter a file name")
        return
    try:
        with open(file_name.get(), "r") as f:
            content = f.read()
            file_content.set(content)
            content_text_box.delete("1.0", tk.END)
            content_text_box.insert("1.0", file_content.get())
    except FileNotFoundError:
        error_message.set("File not found")
        content_text_box.delete("1.0", tk.END)
        # file_content.set("")
    else:
        error_message.set("")


def save_text_box_content():
    content = content_text_box.get("1.0", tk.END)
    try:
        with open(file_name.get(), "w") as f:
            f.write(content)
    except FileNotFoundError:
        error_message.set("File not found")
    except Exception:
        error_message.set("Error saving file")
    else:
        success_message.set("File saved successfully")
        content_text_box.delete("1.0", tk.END)


read_file_btn = tk.Button(
    root_window, text="Open file", width=500, font=("Monospace", 20), command=read_file
).pack(pady=10)


error_label = tk.Label(
    root_window, textvariable=error_message, font=("Monospace", 20), fg="red"
).pack()
success_label = tk.Label(
    root_window, textvariable=success_message, font=("Monospace", 20), fg="green"
).pack()

# content_label = tk.Label(
#     root_window, textvariable=file_content, font=("Monospace", 20), fg="green"
# ).pack()
content_text_box = tk.Text(
    root_window,
    font=("Monospace", 20),
    fg="green",
)
# content_text_box.pack(pady=10, fill="x", expand=True)

save_btn = tk.Button(
    root_window,
    text="Save file",
    width=500,
    font=("Monospace", 20),
    command=save_text_box_content,
)
save_btn.pack()

combobox = ttk.Combobox(root_window, values=["Option 1", "Option 2", "Option 3"])
combobox.pack()

# main loop
root_window.mainloop()  # "Start the GUI, show the window, and wait for user interaction like button clicks, key presses, etc."
