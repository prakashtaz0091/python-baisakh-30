import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

root = tk.Tk()
root.title("Hyper Humanizer")
root.geometry("1440x720")


DUMMY_TEXT = "Paste you AI generated text here"

humanize_button_text = tk.StringVar()
humanize_button_text.set("Humanize")

ai_text_box = tk.Text(root, font=("Monospace", 20), borderwidth=2)
ai_text_box.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=5,
    pady=5,
)
ai_text_box.insert("1.0", DUMMY_TEXT)
# print(ai_text_box.keys())


human_text_box = tk.Text(root, font=("Monospace", 20), borderwidth=2)
human_text_box.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=5,
    pady=5,
)
human_text_box.insert("1.0", "Your humanized text will appear here")


# dropdown select box (combobox)
CUSTOM_PROMPT_VALUES = {
    "Academic": "Please give answer in academic format, keep it formal not conversational.",
    "Converstational": "Please give answer in conversational format, keep it formal not academic.",
    "Funny": "Please give answer in funny format, keep it formal not academic.",
    "Shorten": "Please give answer in short format, keep it formal not academic.",
}


def on_select(event):
    selected_value = humanize_type.get()
    print(f"You selected: {selected_value}")


humanize_type = ttk.Combobox(root, state="readonly")
humanize_type["values"] = ("Academic", "Converstational", "Funny", "Shorten")
humanize_type.current(0)  # Set the default selected value
# Bind the selection event
humanize_type.bind("<<ComboboxSelected>>", on_select)
humanize_type.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)


def humanize():
    ai_text = ai_text_box.get("1.0", tk.END).strip()

    if ai_text == DUMMY_TEXT:
        messagebox.showwarning(
            "Enter your text",
            "Please enter your AI generated text in the text box, and click Humanize",
        )
        return
    if len(ai_text) < 200:
        messagebox.showwarning(
            "Not enough text",
            "Please paste more than 200 characters of AI generated text",
        )
        return

    API_URL = "https://chatgpt-42.p.rapidapi.com/aitohuman"  # request url (Uniform Resource Locator)

    payload = {
        "text": f"""
                {CUSTOM_PROMPT_VALUES[humanize_type.get()]}
               {ai_text}
               """
    }
    # print(payload)
    headers = {
        "x-rapidapi-key": "place your api key here",
        "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
        "Content-Type": "application/json",
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    response_data = response.json()
    # response_data = {"result": [" dummy text "], "status": True}
    print(response_data)
    if response_data["status"]:
        response_text_list = response_data["result"]
        whole_reponse_text = "\n\n".join(response_text_list)

        human_text = whole_reponse_text

        human_text_box.delete("1.0", tk.END)
        human_text_box.insert("1.0", human_text)
    else:
        messagebox.showerror(
            "Conversion Failed",
            "Please try again later. If the problem persists, please contact the developer",
        )


humanize_button = tk.Button(
    root, textvariable=humanize_button_text, font=("Monospace", 25), command=humanize
)
humanize_button.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

# Configure rows and columns to expand
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
