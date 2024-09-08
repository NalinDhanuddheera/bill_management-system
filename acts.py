from tkinter import messagebox, filedialog

def reset_fields(app):
    for item in app.quantities.keys():
        app.quantities[item].set("")
    app.total_amount.set("Rs. 0.00")

def calculate_total(app):
    total = 0
    receipt_text = "-----Receipt-----\n"
    for item, price in app.items.items():
        quantity = app.quantities[item].get()
        if quantity.isdigit():
            total_item = price * int(quantity)
            total += total_item
            receipt_text += f"{item}: {quantity} x Rs.{price} = Rs.{total_item}\n"
        elif quantity != "":
            messagebox.showerror("Error", f"Invalid quantity for {item}")
            return
    app.total_amount.set(f"Rs. {total:.2f}")
    receipt_text += f"Total: Rs. {total:.2f}\n"
    return receipt_text

def save_bill(app):
    bill_content = calculate_total(app)
    if bill_content:
        file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Text files', '.txt'), ('All files', '.*')])
        if file:
            file.write(bill_content)
            file.close()

def print_bill(app):
    bill_content = calculate_total(app)
    if bill_content:
        file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[('Text files', '.txt'), ('All files', '.*')])
        if file:
            file.write(bill_content)
            file.close()
            messagebox.showinfo("Print", f"The bill has been saved to {file.name}. You can print it from there.")
