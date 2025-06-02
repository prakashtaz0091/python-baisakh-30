import tkinter as tk

# setup
root_window = tk.Tk()
root_window.title("Basic Calculator")  # set title
root_window.geometry("600x400")  # set size (width x height)

# vars
result = tk.StringVar()

math_expression = tk.Entry(root_window, width=500, font=("Monospace", 25))
math_expression.pack()


# handlers
def calculate():
    expression = math_expression.get()

    try:
        # result.set(eval(expression))
        r = eval(expression)
    except Exception:
        # result.set("Invalid expression")
        math_expression.delete(0, tk.END)
        math_expression.insert(0, "Invalid expression")
    else:
        # 123
        math_expression.delete(0, tk.END)
        math_expression.insert(0, str(r))


def clear():
    math_expression.delete(0, tk.END)


calc_button = tk.Button(
    root_window, text="calculate", width=500, font=("Monospace", 30), command=calculate
).pack(pady=10)
clear_button = tk.Button(
    root_window, text="clear", font=("Monospace", 30), command=clear
).pack(pady=10)
result_label = tk.Label(root_window, textvariable=result, font=("Monospace", 30)).pack()


# main loop
root_window.mainloop()  # "Start the GUI, show the window, and wait for user interaction like button clicks, key presses, etc."
