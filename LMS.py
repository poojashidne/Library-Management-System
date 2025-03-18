import tkinter as tk
from tkinter import ttk, messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1200x700")  # Adjusted window size for a better layout
        self.root.configure(bg="#f0f0f0")  # Light gray background

        self.books = []

        # Title Label
        self.title_label = tk.Label(root, text="Library Management System", font=("Arial", 36, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Frame for book input and button
        self.book_frame = tk.Frame(root, bg="#f0f0f0")
        self.book_frame.pack(pady=20)

        self.book_label = tk.Label(self.book_frame, text="Book Title:", font=("Arial", 18), bg="#f0f0f0")
        self.book_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.book_entry = tk.Entry(self.book_frame, font=("Arial", 18), width=40)
        self.book_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.book_frame, text="Add Book", font=("Arial", 18), bg="#4caf50", fg="white", command=self.add_book)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # Listbox inside a frame with scrollbar
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=20)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)

        self.book_listbox = tk.Listbox(self.list_frame, font=("Arial", 18), width=80, height=15, selectbackground="#d32f2f", selectforeground="white", yscrollcommand=self.scrollbar.set)
        self.book_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.config(command=self.book_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Remove Book Button
        self.remove_button = tk.Button(root, text="Remove Selected Book", font=("Arial", 18), bg="#d32f2f", fg="white", command=self.remove_book)
        self.remove_button.pack(pady=20)

    def add_book(self):
        book_title = self.book_entry.get().strip()
        if book_title:
            self.books.append(book_title)
            self.book_listbox.insert(tk.END, book_title)
            self.book_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Book title cannot be empty!")

    def remove_book(self):
        selected_index = self.book_listbox.curselection()
        if selected_index:
            self.book_listbox.delete(selected_index)
            del self.books[selected_index[0]]
        else:
            messagebox.showwarning("Warning", "Please select a book to remove!")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
