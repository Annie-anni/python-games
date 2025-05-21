import requests
import argparse

def get_parser():

    parser = argparse.ArgumentParser(description="Currency exchange tools")
    parser.add_argument("--amount1",type=float,help="Amount 1 USD")
    parser.add_argument("--amount2",type=float,help="Amount 2 USD")
    parser.add_argument("result",choices=["amount1","amount2"],help="Select the currency you want to convert to")
    return parser

def fetch_exchange_rates():
    url = "https://v6.exchangerate-api.com/v6/52b83b9bffe1f69cc6463075/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"RequestException: {e}")
        return None

def main():
    parser = get_parser()
    args = parser.parse_args()
    data = fetch_exchange_rates()

    if data:
        rate_cny = data['conversion_rates']['CNY']
        rate_jpy = data['conversion_rates']['JPY']

        if args.result == 'amount1' and args.amount1 is not None:
            result = args.amount1 * rate_cny
            print(f"{args.amount1} USD = {result:.2f} CNY")
        elif args.result == 'amount2' and args.amount2 is not None:
            result = args.amount2 * rate_jpy
            print(f"{args.amount2} USD = {result:.2f} JPY")
        else:
            print("Please provide the corresponding amount to convert")
if __name__ == '__main__':
    main()