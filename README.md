# Final_Project

# Currency Converter

Overview
---------
This is a Python application that converts amounts between different currencies using real-time exchange rates from the ExchangeRate-API. The application is built using the tkinter library for the GUI and the requests library to fetch exchange rates.

Features
---------
- Convert between different currencies.
- View conversion history.
- Clear input fields.
- Refresh exchange rates.

Requirements 
------------
- Python 3.x
- requests library
- tkinter library (standard with Python)

Install the required libraries:

pip install requests
pip install tkinter

Usage:

Replace "api_key" with your ExchangeRate-API key in the main function.
https://app.exchangerate-api.com/dashboard/

# Code Explanation

Imports:

{""
import requests
import tkinter as tk
from tkinter import ttk, messagebox
""}

* requests: For making HTTP requests to fetch exchange rates.
* tkinter: For creating the GUI.
* ttk and messagebox from tkinter: For enhanced GUI components and message dialogs.

CurrencyConverter Class

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/USD"
        self.rates = self._fetch_rates()
        self.history = []
        self.available_currencies = list(self.rates.keys())


> Initializes the class with the API key.
> Fetches the latest exchange rates and stores them.
> Initializes an empty history list to store conversion history.
> Stores the available currencies.

Fetch Rates:

def _fetch_rates(self):
    try:
        response = requests.get(self.api_url)
        data = response.json()
        if response.status_code == 200:
            return data['conversion_rates']
        else:
            print("Error fetching currency data:", data.get("error-type", "Unknown error"))
            return {}
    except requests.RequestException as e:
        print("Request error:", e)
        return {}

> Fetches exchange rates from the API.
> Returns the conversion rates if the request is successful; otherwise, prints an error message and returns an empty dictionary.


Get Availabile currencies:

def get_available_currencies(self):
    return self.available_currencies

- Returns a list of available currencies.

convert_fiat: 

def convert_fiat(self, amount, from_currency, to_currency):
    if from_currency not in self.rates or to_currency not in self.rates:
        raise ValueError("Currency not supported")
    from_rate = self.rates[from_currency]
    to_rate = self.rates[to_currency]
    converted_amount = (amount / from_rate) * to_rate
    self.history.append((amount, from_currency, to_currency, converted_amount))
    return converted_amount

* Converts an amount from one currency to another.
* Stores the conversion in the history list.


view_history method:

def view_history(self):
    if not self.history:
        return "No conversion history available."
    history_str = ""
    for entry in self.history:
        history_str += f"{entry[0]} {entry[1]} = {entry[3]:.2f} {entry[2]}\n"
    return history_str

Return a formatted string of the conversion history.

# CurrencyConverterApp Class 

Initialize GUI interface for user to interact with convert curr options.


class CurrencyConverterApp(tk.Tk):
    def __init__(self, converter):
        super().__init__()
        self.converter = converter
        self.title("Currency Converter")
        self.geometry("400x400")

        self.create_welcome_screen()


1. Initializes the main application window with the specified title and size.
2. Calls create_welcome_screen to set up the initial screen.

Create Welcome Window:

def create_welcome_screen(self):
    self.welcome_label = ttk.Label(self, text="Welcome to Currency Converter!", font=("Helvetica", 16))
    self.welcome_label.pack(pady=50)

    self.start_button = ttk.Button(self, text="Start", command=self.start_conversion)
    self.start_button.pack(pady=20)

    self.exit_button = ttk.Button(self, text="Exit", command=self.quit)
    self.exit_button.pack(pady=20)

    self.footer_label = ttk.Label(self, text="Created by Yahya AGha", font=("Helvetica", 10))
    self.footer_label.pack(side=tk.BOTTOM, pady=10)

#Creates the welcome screen with a welcome message ("Welcome to currency converter!"), start button to start the conversion, exit button to exit directly from program, and footer label.


Start Conversion Window:

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

##Hides the welcome screen elements.
##Creates and packs the elements for the conversion screen: input fields, labels, and buttons.

Convert currency Window:

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

* Converts the entered amount and updates the result label.
* Displays an error message if the conversion fails.

  SHow History window:

  def show_history(self):
    history = self.converter.view_history()
    messagebox.showinfo("Conversion History", history)

>>> show the conversion history results with message box.


Clear Option :

def clear_fields(self):
    self.amount_entry.delete(0, tk.END)
    self.from_currency_entry.set('')
    self.to_currency_entry.set('')
    self.result_label.config(text="")

##Clear the fields if user clicked on Clear option.

^^_^^ Clears all input fields and the result label.

def refresh_rates(self):
    self.converter.rates = self.converter._fetch_rates()
    messagebox.showinfo("Rates Refreshed", "Exchange rates have been updated.")

** Refreshes the exchange rates and notifies the user.


# Main Func:

def main():
    api_key = "c18637b2ad0c747253385b54"  # Replace with your ExchangeRate-API key
    converter = CurrencyConverter(api_key)
    app = CurrencyConverterApp(converter)
    app.mainloop()

if __name__ == "__main__":
    main()

##Set up the API key, creates instances of CurrencyConverter and CurrencyConverterApp, and runs the application.


References
----------
- [ExchangeRate-API](https://www.exchangerate-api.com/docs/overview) - The API used for fetching exchange rates.
- [Requests Library](https://docs.python-requests.org/en/latest/) - Documentation for the requests library.
- [tkinter Library](https://docs.python.org/3/library/tkinter.html) - Documentation for the tkinter library.
- [Python Official Documentation](https://docs.python.org/3/) - The official documentation for Python.


Yahya AGha
Regards (:/


