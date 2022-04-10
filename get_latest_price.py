from one_inch_swap import *





sell_contract_id = ""
buy_contract_id = ""
sender_address = ""
slippage = ""
gasPrice = ""
amount = ""

token_lis = get_one_inch_bian_tokens(chain='bsc')

print(len(token_lis))



dex_price, transac = get_price_and_build_transaction(sender_address, sell_contract_id, buy_contract_id, amount, gasPrice, slippage)
# get dex_price




# get cex_price

from binance.spot import Spot as Client
client_spot = Client(key='', secret='', base_url='https://api.binance.com')
def get_spot_price(pair_lis):
    spot_price_lis = []
    for pair in pair_lis:
        spot_trade_list = client_spot.trades(pair, limit=1)
        price = float(spot_trade_list[0]['price'])
        spot_price_lis.append(price)
    spot_price = dict(zip(pair_lis, spot_price_lis))
    return spot_price

spot_latest_price = get_spot_price(spot_pair_lis)
print(spot_latest_price)


def caculate_spread(dex_price, spot_price):
    spread_lis = []
    pair_lis = []
    for key, value in spot_latest_price.items():
        spread = (value - dex_price[key]) / dex_price[key]
        if spread >= 0.01:
            spread_lis.append(spread)
            pair_lis.append(key)
        latest_spread = dict(zip(pair_lis, spread_lis))
        return latest_spread
    else:
        pass

