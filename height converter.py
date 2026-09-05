import tkinter as tk

# function
def convert():
    cm = cm_entry.get()
    foot = foot_entry.get()

    if cm != "":
        cm_value = float(cm)
        cm_to_foot = cm_value / 30.48
        output.config(text=f"{cm_to_foot:.2f} feet")
    elif foot != "":
        foot_value = float(foot)
        foot_to_cm = foot_value * 30.48
        output.config(text=f"{foot_to_cm:.2f} cm")
    elif cm == "" and foot == "":
        output.config(text="enter a value!")
    cm_entry.delete(0, tk.END)
    foot_entry.delete(0, tk.END)
# window
root = tk.Tk()
root.geometry("400x500")
root.title("height converter by nikoZEN99")

# cm label
cm_label = tk.Label(root, text="cm:", font=("Arial", 20))
cm_label.pack(pady=10)

# cm entry box
cm_entry = tk.Entry(root, font=("Arial", 20))
cm_entry.pack(pady=10)

# foot label
foot_label = tk.Label(root, text="foot:", font=("Arial", 20))
foot_label.pack(pady=10)

# foot entry box
foot_entry = tk.Entry(root, font=("Arial", 20))
foot_entry.pack(pady=10)

# output label
output = tk.Label(root, font=("Arial", 20))
output.pack(pady=10)

# submit button
submit_button = tk.Button(root, text="convert", font=("Arial", 20), command=convert)
submit_button.pack(pady=10)

# watermark label
watermark = tk.Label(root, text="made by @NikoZEN99", font=("Arial", 20))
watermark.pack(pady=10)

root.mainloop()