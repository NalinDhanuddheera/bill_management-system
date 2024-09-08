import tkinter as tk
from tkinter import messagebox, filedialog

class BillManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Management System")
        self.root.geometry("700x500")

        # Variables to store item quantities
        self.quantities = {}
        self.total_amount = tk.StringVar(value="Rs. 0.00")

        # List of 10 Electric items and their prices
        self.items = {
            "Fan": 1500,
            "Light Bulb": 100,
            "Electric Iron": 800,
            "Television": 30000,
            "Refrigerator": 25000,
            "Oven": 7000,
            "Mixer": 4000,
            "Air Conditioner": 35000,
            "Water Heater": 5000,
            "Microwave": 8000
        }

        # Create frames for layout
        menu_frame = tk.Frame(self.root, bg="lightgreen", padx=10, pady=10)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        entry_frame = tk.Frame(self.root, bg="lightblue", padx=10, pady=10)
        entry_frame.pack(side=tk.LEFT, fill=tk.Y, expand=True)

        total_frame = tk.Frame(self.root, bg="lightyellow", padx=10, pady=10)
        total_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Left side menu (Items and prices)
        tk.Label(menu_frame, text="Item Menu", font=("Arial", 14, "bold"), bg="lightgreen").pack(anchor="w", padx=10, pady=10)

        for item, price in self.items.items():
            item_label = tk.Label(menu_frame, text=f"{item} - Rs.{price}", bg="lightgreen", anchor="w", font=("Arial", 12))
            item_label.pack(anchor="w", padx=10, pady=5)

        # Middle section for quantity input
        tk.Label(entry_frame, text="Enter Quantity", font=("Arial", 14, "bold"), bg="lightblue").pack(anchor="w", padx=10, pady=10)

        for item in self.items.keys():
            self.quantities[item] = tk.StringVar()
            entry = tk.Entry(entry_frame, textvariable=self.quantities[item], font=("Arial", 12), width=20)
            entry.pack(padx=10, pady=5, fill=tk.X)

        # Buttons
        button_frame = tk.Frame(entry_frame, bg="lightblue")
        button_frame.pack(pady=10, fill=tk.X)

        reset_button = tk.Button(button_frame, text="Reset", font=("Arial", 12), command=self.reset_fields, bg="red", fg="white")
        reset_button.pack(side=tk.LEFT, padx=5)

        total_button = tk.Button(button_frame, text="Total", font=("Arial", 12), command=self.calculate_total, bg="blue", fg="white")
        total_button.pack(side=tk.LEFT, padx=5)

        # Total section
        tk.Label(total_frame, text="Bill Total", font=("Arial", 14, "bold"), bg="lightyellow").pack(anchor="w", padx=10, pady=10)
        self.total_label = tk.Label(total_frame, textvariable=self.total_amount, font=("Arial", 14), bg="lightyellow")
        self.total_label.pack(anchor="w", padx=10, pady=10)

        save_button = tk.Button(total_frame, text="Save Bill", font=("Arial", 12), command=self.save_bill, bg="green", fg="white")
        save_button.pack(pady=5)

        print_button = tk.Button(total_frame, text="Print Bill", font=("Arial", 12), command=self.print_bill, bg="purple", fg="white")
        print_button.pack(pady=5)

    def reset_fields(self):
        for item in self.items.keys():
            self.quantities[item].set("")
        self.total_amount.set("Rs. 0.00")

    def calculate_total(self):
        total = 0
        receipt_text = "-----Receipt-----\n"
        for item, price in self.items.items():
            quantity = self.quantities[item].get()
            if quantity.isdigit():
                total_item = price * int(quantity)
                total += total_item
                receipt_text += f"{item}: {quantity} x Rs.{price} = Rs.{total_item}\n"
            elif quantity != "":
                messagebox.showerror("Error", f"Invalid quantity for {item}")
                return
        self.total_amount.set(f"Rs. {total:.2f}")
        receipt_text += f"Total: Rs. {total:.2f}\n"
        return receipt_text

    def save_bill(self):
        bill_content = self.calculate_total()
        if bill_content:
            file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Text files', '.txt'), ('All files', '.*')])
            if file:
                file.write(bill_content)
                file.close()

    def print_bill(self):
        bill_content = self.calculate_total()
        if bill_content:
            file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Text files', '.txt'), ('All files', '.*')])
            if file:
                file.write(bill_content)
                file.close()
                messagebox.showinfo("Print", f"The bill has been saved to {file.name}. You can print it from there.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillManagementSystem(root)
    root.mainloop()
