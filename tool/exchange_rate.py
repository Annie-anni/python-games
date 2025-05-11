import requests
import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="USD to CNY")
    parser.add_argument("amount",type=float,help="Enter the amount")
    return parser.parse_args()

def usd_to_cny():
    args = get_parser()
    url = "https://v6.exchangerate-api.com/v6/52b83b9bffe1f69cc6463075/latest/USD"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "conversion_rates" not in data:
        print("Failed to retrieve exchange rate")
        return

    rate = data["conversion_rates"]["CNY"]
    result = args.amount * rate
    print(f"{args.amount} USD = {result:.2f} CNY")

if __name__ == "__main__":
    usd_to_cny()


