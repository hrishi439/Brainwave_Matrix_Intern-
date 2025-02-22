import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Database Initialization
Db = sqlite3.connect("inventory.db")
cursor = Db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER)''')
Db.commit()

# GUI Class
class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory System")
        self.root.geometry("500x400")
        self.root.configure(bg="#f4f4f4")
        self.create_ui()

    def create_ui(self):
        frame = tk.Frame(self.root, bg="#ffffff", padx=10, pady=10, relief=tk.RIDGE, borderwidth=2)
        frame.pack(pady=20)
        
        tk.Label(frame, text="Product Name:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(frame, text="Stock:", bg="#ffffff").grid(row=1, column=0, padx=5, pady=5)
        self.stock_entry = tk.Entry(frame)
        self.stock_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Button(frame, text="Add Product", command=self.add_product, bg="#4CAF50", fg="white").grid(row=2, column=1, pady=10)
        
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Stock"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Product Name")
        self.tree.heading("Stock", text="Stock")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        self.load_products()

    def add_product(self):
        name = self.name_entry.get()
        stock = self.stock_entry.get()
        if name and stock.isdigit():
            cursor.execute("INSERT INTO products (name, stock) VALUES (?, ?)", (name, int(stock)))
            Db.commit()
            self.load_products()
            messagebox.showinfo("Success", "Product added!")
        else:
            messagebox.showerror("Error", "Invalid input!")
    
    def load_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        cursor.execute("SELECT * FROM products")
        for product in cursor.fetchall():
            self.tree.insert("", "end", values=product)

# Run App
root = tk.Tk()
app = InventoryApp(root)
root.mainloop()
