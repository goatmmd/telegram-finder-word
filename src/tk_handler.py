import tkinter as tk


def get_word_input():
    # Set the locale to Persian

    def submit():
        global input_text

        input_text = entry.get()
        root.destroy()  # Close the window after getting input
        return input_text

    root = tk.Tk()
    root.title("Word")

    # Set the font to support Persian characters
    font = ("Arial", 12, "normal")

    label = tk.Label(root, text="Enter Your Text:")
    label.pack(pady=10)

    entry = tk.Entry(root, font=font)
    entry.pack(pady=10)

    button = tk.Button(root, text="Submit", command=submit)
    button.pack(pady=10)

    root.mainloop()

    return input_text


def get_links_input():
    def submit():
        global link_input
        link_input = entry.get()
        root.destroy()  # Close the window after getting input
        return link_input

    root = tk.Tk()
    root.title("Chat input")

    # Set the font to support Persian characters
    font = ("Arial", 12, "normal")

    label = tk.Label(root, text="Enter Chat (ID-LINK-NAME):")
    label.pack(pady=10)

    entry = tk.Entry(root, font=font)
    entry.pack(pady=10)

    button = tk.Button(root, text="Submit", command=submit)
    button.pack(pady=10)

    root.mainloop()

    return link_input
