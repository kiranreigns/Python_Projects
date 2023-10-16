# Python program to convert the currency
# of one country to that of another country 
 
import requests
amount = float(input("Enter amount in USD: "))
target_currency = str(input('Enter the three letter currency code that you wanna convert to(e.g., EUR): ')).upper()

url = f"https://open.er-api.com/v6/latest"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    if target_currency in data["rates"]:
         exchange_rate = data['rates'][target_currency]
         result = amount * exchange_rate
         print(f"{amount} USD is equal to {result} {target_currency} (Exchange Rate: 1 USD = {exchange_rate} {target_currency}).")
    else:
            print("Target currency not found. Please try again.")
else:
        print("Failed to fetch exchange rates. Please try again later.")

#make sure your data is turned on to fetch the current currency rates



    


 