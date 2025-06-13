import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sign Up")
root.geometry("400x500")
root.configure(bg="#1a1a2e")

header = tk.Label(root, text="Sign Up", bg="#ff9900", fg="yellow", font=("Arial", 16, "bold"))
header.pack(fill="x")

form = tk.Frame(root, bg="#1a1a2e", padx=20, pady=20)
form.pack(fill="both", expand=True)

def create_entry_row(label_text, row, show=None):
    label = tk.Label(form, text=label_text, bg="#1a1a2e", fg="yellow", anchor="w")
    label.grid(row=row, column=0, sticky="w", pady=5)
    entry = tk.Entry(form, show=show, width=30)
    entry.grid(row=row, column=1, pady=5)
    return entry

first_name = create_entry_row("First Name", 0)
last_name = create_entry_row("Last Name", 1)
screen_name = create_entry_row("Screen Name", 2)

dob_label = tk.Label(form, text="Date of Birth", bg="#1a1a2e", fg="yellow")
dob_label.grid(row=3, column=0, sticky="w", pady=5)
months = ttk.Combobox(form, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], width=6)
months.grid(row=3, column=1, sticky="w")
months.set("May")
days = ttk.Combobox(form, values=list(range(1, 32)), width=4)
days.grid(row=3, column=1)
days.set("5")
years = ttk.Combobox(form, values=list(range(1950, 2026)), width=6)
years.grid(row=3, column=1, sticky="e")
years.set("1985")

gender_label = tk.Label(form, text="Gender", bg="#1a1a2e", fg="yellow")
gender_label.grid(row=4, column=0, sticky="w", pady=5)
gender_var = tk.StringVar()
male_rb = tk.Radiobutton(form, text="Male", variable=gender_var, value="1", bg="#1a1a2e", fg="yellow")
female_rb = tk.Radiobutton(form, text="Female", variable=gender_var, value="2", bg="#1a1a2e", fg="yellow")
male_rb.grid(row=4, column=1, sticky="w")
female_rb.grid(row=4, column=1)

country = create_entry_row("Country", 5)
country1 = ttk.Combobox(form, values=[
    "USA", "China", "India", "Indonesia", "Pakistan", "Brazil", "Nigeria",
    "Bangladesh", "Russia", "Mexico", "Japan", "Ethiopia", "Philippines", "Egypt",
    "Vietnam", "Germany", "Turkey", "Democratic Republic of Congo", "Iran", "United Kingdom"], width=27)
country1.grid(row=5, column=1)
country1.set('USA')

email = create_entry_row("E-mail", 6)
phone = create_entry_row("Phone", 7)
password = create_entry_row("Password", 8, show="*")
confirm_password = create_entry_row("Confirm Password", 9, show="*")

agree_var = tk.IntVar()
agree = tk.Checkbutton(form, text="I agree to the Terms of Use", variable=agree_var, bg="#1a1a2e", fg="yellow", activebackground="#1a1a2e")
agree.grid(row=10, column=1, sticky="w", pady=10)

btn_frame = tk.Frame(root, bg="#ff9900")
btn_frame.pack(fill="x", pady=10)

submit_btn = tk.Button(btn_frame, text="submit", bg="green", fg="white", width=10)
submit_btn.pack(side="left", padx=50, pady=10)

cancel_btn = tk.Button(btn_frame, text="Cancel", bg="red", fg="white", width=10)
cancel_btn.pack(side="right", padx=50, pady=10)

root.mainloop()