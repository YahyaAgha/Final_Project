import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key  # API key for accessing the ExchangeRate-API
        self.api_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/USD"  # API URL to fetch latest USD exchange rates
        self.rates = self._fetch_rates()  # Fetch the currency rates 
        self.history = []  # To store conversion history to list []
        self.available_currencies = list(self.rates.keys())  # List of available currencies from the fetched rates

    def _fetch_rates(self):
        try:
            response = requests.get(self.api_url)  # Fetch currency data from the API
            data = response.json()  # Parse the response JSON
            if response.status_code == 200:
                return data['conversion_rates']  # return conversion rates if the request is successful
            else:
                print("Error fetching currency data:", data.get("error-type", "Unknown error"))
                return {}
        except requests.RequestException as e:
            print("Request error:", e)  # Print the error if the request fails
            return {}

    def get_available_currencies(self):
        return self.available_currencies  # Return the list of available currencies

    def convert_fiat(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Currency not supported")  # Raise error if the currency is not supported
        from_rate = self.rates[from_currency]  # Get the conversion rate for the from_currency
        to_rate = self.rates[to_currency]  # Get the conversion rate for the to_currency
        converted_amount = (amount / from_rate) * to_rate  # Calculate the converted amount
        self.history.append((amount, from_currency, to_currency, converted_amount))  # Add the conversion to history
        return converted_amount  # Return the converted amount

    def view_history(self):
        if not self.history:
            return "No conversion history available."  # Return message if there is no history
        history_str = ""
        for entry in self.history:
            history_str += f"{entry[0]} {entry[1]} = {entry[3]:.2f} {entry[2]}\n"  # Format the history entries
        return history_str  # Return the formatted history
