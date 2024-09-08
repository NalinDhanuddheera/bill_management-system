import tkinter as tk
from tkinter import messagebox, filedialog
from items import ITEMS
from acts import reset_fields, calculate_total, save_bill, print_bill

class BillManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bill Management System")
        self.root.geometry("700x500")

        # Configure grid for the root window
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Variables to store item quantities
        self.quantities = {}
        self.total_amount = tk.StringVar(value="Rs. 0.00")

        # Create frames for layout with colors
        menu_frame = tk.Frame(self.root, bg="lightgreen", padx=10, pady=10)
        menu_frame.grid(row=0, column=0, sticky="nsew")

        entry_frame = tk.Frame(self.root, bg="lightblue", padx=10, pady=10)
        entry_frame.grid(row=0, column=1, sticky="nsew")

        total_frame = tk.Frame(self.root, bg="lightyellow", padx=10, pady=10)
        total_frame.grid(row=0, column=2, sticky="nsew")

        # Configure column and row weights to make it responsive
        menu_frame.columnconfigure(0, weight=1)
        entry_frame.columnconfigure(0, weight=1)
        total_frame.columnconfigure(0, weight=1)

        # Left side menu (Items and prices)
        tk.Label(menu_frame, text="Item Menu", font=("Arial", 14, "bold"), bg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="n")

        row_count = 1
        for item, price in ITEMS.items():
            item_label = tk.Label(menu_frame, text=f"{item} - Rs.{price}", bg="lightgreen", font=("Arial", 12))
            item_label.grid(row=row_count, column=0, sticky="ew", padx=10, pady=5)
            menu_frame.grid_rowconfigure(row_count, weight=1)
            row_count += 1

        # Middle section for quantity input
        tk.Label(entry_frame, text="Enter Quantity", font=("Arial", 14, "bold"), bg="lightblue").grid(row=0, column=0, padx=10, pady=10, sticky="n")

        row_count = 1
        for item in ITEMS.keys():
            self.quantities[item] = tk.StringVar()
            entry = tk.Entry(entry_frame, textvariable=self.quantities[item], font=("Arial", 12), width=10)
            entry.grid(row=row_count, column=0, padx=10, pady=5, sticky="ew")
            row_count += 1

        # Buttons below the entries
        reset_button = tk.Button(entry_frame, text="Reset", font=("Arial", 12), command=lambda: reset_fields(self), bg="red", fg="white")
        reset_button.grid(row=row_count + 1, column=0, pady=10, sticky="ew")

        total_button = tk.Button(entry_frame, text="Total", font=("Arial", 12), command=lambda: calculate_total(self), bg="blue", fg="white")
        total_button.grid(row=row_count + 2, column=0, pady=10, sticky="ew")

        # Total section
        tk.Label(total_frame, text="Bill Total", font=("Arial", 14, "bold"), bg="lightyellow").grid(row=0, column=0, padx=10, pady=10, sticky="n")
        self.total_label = tk.Label(total_frame, textvariable=self.total_amount, font=("Arial", 14), bg="lightyellow")
        self.total_label.grid(row=1, column=0, padx=10, pady=10, sticky="n")

        save_button = tk.Button(total_frame, text="Save Bill", font=("Arial", 12), command=lambda: save_bill(self), bg="green", fg="white")
        save_button.grid(row=2, column=0, pady=10, sticky="ew")

        print_button = tk.Button(total_frame, text="Print Bill", font=("Arial", 12), command=lambda: print_bill(self), bg="purple", fg="white")
        print_button.grid(row=3, column=0, pady=10, sticky="ew")
