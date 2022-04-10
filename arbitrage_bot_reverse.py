from one_inch_swap import *
from CEX import *

sender_address = "0xe6A2C8A9a0642797b583835D905145bb7630e8D1"
private_key = ""
buy_contract_id = web3.toChecksumAddress("0x55d398326f99059fF775485246999027B3197955")
gasPrice = 6000000000
slippage = 0.5
one_inch_contract_id = web3.toChecksumAddress("0x1111111254fb6c44bac0bed2854e76f90643097d")
bian_address = "0xF8c78155657d9C3455Cd019Db4f8774e07718a89"


bsc_tokens = get_one_inch_bian_tokens('bsc')



for key, value in bsc_tokens.items():
    try:
        sell_contract_id = value
        amount = 100
        dex_price, transac = get_price_and_build_transaction(sender_address, sell_contract_id, buy_contract_id, amount,
                                                             gasPrice, slippage)
        pair = key + 'USDT'
        cex_price = get_cex_price(pair)

        spread = (dex_price - cex_price)/cex_price * 100
        print(f"{key}, dexprice is {dex_price} cex_price is {cex_price} spread is {spread}")


    except:
        import traceback

        print(key)
        traceback.print_exc()
        pass