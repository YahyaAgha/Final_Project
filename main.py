from currency_converter import CurrencyConverter
from currency_converter_app import CurrencyConverterApp

def main():
    api_key = "c18637b2ad0c747253385b54"  # Replace with your ExchangeRate-API key
    converter = CurrencyConverter(api_key)  # Create an instance of CurrencyConverter
    app = CurrencyConverterApp(converter)  # Create an instance of the application
    app.mainloop()  # Run the application

if __name__ == "__main__":
    main()  # Run the main function if this script is executed
