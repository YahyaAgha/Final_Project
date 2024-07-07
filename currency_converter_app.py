import tkinter as tk
from tkinter import ttk, messagebox
from currency_converter import CurrencyConverter

class CurrencyConverterApp(tk.Tk):
    def __init__(self, converter):
        super().__init__()
        self.converter = converter
        self.title("Currency Converter")
        self.geometry("400x400")

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_label = ttk.Label(self, text="Welcome to Currency Converter!", font=("Helvetica", 16))
        self.welcome_label.pack(pady=50)  # pady stands for padding above and below the welcome label

        self.start_button = ttk.Button(self, text="Start", command=self.start_conversion)
        self.start_button.pack(pady=20)

        self.exit_button = ttk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=20)

        self.footer_label = ttk.Label(self, text="Created by Yahya AGha", font=("Helvetica", 10))
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def start_conversion(self):
        self.welcome_label.pack_forget()
        self.start_button.pack_forget()
        self.exit_button.pack_forget()

        self.amount_label = ttk.Label(self, text="Amount:")
        self.amount_label.pack(pady=5)

        self.amount_entry = ttk.Entry(self)
        self.amount_entry.pack(pady=5)

        self.from_currency_label = ttk.Label(self, text="From Currency:")
        self.from_currency_label.pack(pady=5)

        self.from_currency_entry = ttk.Combobox(self, values=self.converter.get_available_currencies())
        self.from_currency_entry.pack(pady=5)

        self.to_currency_label = ttk.Label(self, text="To Currency:")
        self.to_currency_label.pack(pady=5)

        self.to_currency_entry = ttk.Combobox(self, values=self.converter.get_available_currencies())
        self.to_currency_entry.pack(pady=5)

        self.convert_button = ttk.Button(self, text="Convert", command=self.convert_currency)
        self.convert_button.pack(pady=20)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=5)

        self.history_button = ttk.Button(self, text="View History", command=self.show_history)
        self.history_button.pack(pady=10)

        self.clear_button = ttk.Button(self, text="Clear", command=self.clear_fields)
        self.clear_button.pack(pady=10)

        self.refresh_button = ttk.Button(self, text="Refresh Rates", command=self.refresh_rates)
        self.refresh_button.pack(pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_entry.get().upper()
            to_currency = self.to_currency_entry.get().upper()

            if from_currency in self.converter.rates and to_currency in self.converter.rates:
                result = self.converter.convert_fiat(amount, from_currency, to_currency)
                self.result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
            else:
                raise ValueError("Currency not supported")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def show_history(self):
        history = self.converter.view_history()
        messagebox.showinfo("Conversion History", history)

    def clear_fields(self):
        self.amount_entry.delete(0, tk.END)
        self.from_currency_entry.set('')
        self.to_currency_entry.set('')
        self.result_label.config(text="")

    def refresh_rates(self):
        self.converter.rates = self.converter._fetch_rates()
        messagebox.showinfo("Rates Refreshed", "Exchange rates have been updated.")
