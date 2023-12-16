
import csv
import os.path
import pandas as pd
from typing import List , Dict
from binance import Client
api_key = os.environ['BINANCE_API_KEY_TEST']
api_secret = os.environ['BINANCE_API_SECRET_TEST']
client = Client(api_key , api_secret)

# coins list contains some of the well known crypto pairs
coins  = ["BTC" , "ETH" , "BNB" , "DOG" ,"SOL" , "XRP"]
pairs = ["BTCUSD" , "BNBUSD" , "ETHUSD" , "DOGBNB"]
class Binance_Account:

    def __init__(self , account , balance):
        self.account = account
        self.balance = balance
    # account: should your verified binance accound
    def account_info(self , account):
        account = client.get_account()
        btc_balance = client.get_asset_balance("BTC")
        eth_balance = client.get_asset_balance("ETH")
        acc_status = client.get_account_status()
        status_data = pd.DataFrame(acc_status)
        status_data.head()
        #safe it to csv file
        with open("data.csv" , newline='') as file:
            write = csv.writer(file , acc_status=acc_status)
            write .writerow()
            write.writerows(acc_status)
        for keys , values in acc_status.items():
            print(f"{keys} : {values} ")
    def orders_info(self , pairs:List[str]) -> Dict:
        for pair in pairs:
            orders = client.get_all_orders(pair)
            open = client.get_open_orders(pair)

    def transaction_history(self):
        deposits = client.get_deposit_history()
        withdraws = client.get_withdraw_history()

        for coin in coins:
            trans_address = client.get_asset_balance(coin)
            if trans_address is None or trans_address == 0:
                print("you have no balance in the aforementioned coin")
                pass
            else:
                print(trans_address)
    def getKline(self , pair:List):
        klines = get_historical_klines(pain , Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
        for kline in client.get_historical_klines_generator("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 Dec, 2017", "1 Jan, 2018"):
            print(kline)
def main():
    binance = Binance_Account()
    binance.account_info()
    binance.transaction_history()
if __name__ == '__main__':
    main()
