from binance.client import Client
from binance.enums import *
import time

proxies = {'http': 'http://127.0.0.1:1086',
           'https': 'http://127.0.0.1:1086'}
client = Client(api_key="8YbN0qDgaPhYQCQjW8v2v3JOWNHoTjOZgLkXsF1MeT3BY4Lu1TzVrPCd3SQRSBuf",
                api_secret="GNStPoGYiM5fb03fJUx0uSnltJUK8IPTF8f8nk1LcHl6mqsVHDuEs9AIO0GWHUCe",
                requests_params={'proxies': proxies})


def get_cex_price(pair):
    cex_price = float(client.get_margin_price_index(symbol=pair)['price'])
    return cex_price


def get_fit_amount():
    info = client.get_symbol_info(symbol=pair)
    min_size = float(info['filters'][2]['stepSize'])
    fit_amount = dex_balance // min_size * min_size
    return fit_amount

def cex_leverage():
    client.enable_isolated_margin_account(symbol=pair)
    transaction = client.transfer_spot_to_isolated_margin(asset='USDT',symbol=pair, amount=100)
    client.create_margin_loan(asset=key, amount=fit_amount, isIsolated='TRUE', symbol=pair)
    order = client.create_margin_order(symbol=pair,
                                   side=SIDE_SELL,
                                   type="MARKET",
                                   quantity=fit_amount,
                                   isIsolated='TRUE')


def check_and_close_position():
    while True:
        balance = float(client.get_asset_balance(asset=key)['free'])
        if dex_balance == balance:
            transaction = client.transfer_spot_to_isolated_margin(asset=key, symbol=pair, amount=balance)
            client.repay_margin_loan(asset=key, amount=fit_amount, isIsolated='TRUE', symbol=pair)
            break

        else:
            print("Deposit hasn't been received")
            time.sleep(5)
            continue