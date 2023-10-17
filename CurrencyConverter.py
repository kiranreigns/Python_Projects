def currency_converter():
    """
    This program allows you to convert USD to your desired currency based on the current exchange rate.
    Make sure your data is turned on to fetch the current currency rates.
    """
    try:
        amount = float(input("Enter amount in USD: "))
        target_currency = input('Enter the three-letter currency code that you want to convert to (e.g., EUR): ').upper()

        url = f"https://v6.exchangerate-api.com/v6/4cf75332213cbde50a3a9a16/latest/USD"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if target_currency in data["conversion_rates"]:
                exchange_rate = data['conversion_rates'][target_currency]
                result = amount * exchange_rate
                print(f"{amount} USD is equal to {result} {target_currency} (Exchange Rate: 1 USD = {exchange_rate} {target_currency}).")
            else:
                print("Unsupported currency! Please enter a valid currency code.")

    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    except KeyError:
        print("Target currency not found!!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Failed to fetch exchange rates. Please try again later.")

if __name__ == "__main__":
    currency_converter()



    


 
