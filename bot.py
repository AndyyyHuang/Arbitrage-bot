from cex.utils import cex_utils
from dex.utils import dex_utils
from binance.spot import Spot as Client



class bot(cex_utils, dex_utils):

  def __init__(self):
    self.who = input('andy or bob: ')
    assert self.who == 'andy' or self.who == 'bob'
    self.recvWindow = 50000
    cex_utils.__init__(self, self.who)
    dex_utils.__init__(self, self.who)
    self.spot_wallet = [i for i in self.spot.account(recvWindow=self.recvWindow)['balances'] if i['free'] != '0.00000000' and i['free'] != '0.00']
    #self.futures_wallet = self.futures.get_balance()
    #self.history = client_spot.my
    
  


  def screener(self):
    coins = {'CAKE': '0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82', 'DOT': '0x7083609fce4d1d8dc0c979aab8c869ea2c873402', 'UNI': '0xbf5140a22578168fd562dccf235e5d43a02ce9b1', 'LINK': '0xf8a0bf9cf54bb92f17374d9e9a321e6a111a51bd', 'BAND': '0xad6caeb32cd2c308980a548bd0bc5aa4306c6c18', 'ADA': '0x3ee2200efb3400fabb9aacf31297cbdd1d435d47', 'SFP': '0xd41fdb03ba84762dd66a0af1a6c8540ff1ba5dfb', 'XVS': '0xcf6bb5389c92bdda8a3747ddb454cb7a64626c63', 'TWT': '0x4b0f1812e5df2a09796481ff14017e6005508003', 'YFI': '0x88f1a5ae2a3bf98aeaf342d26b30a79438c9142e', 'SXP': '0x47bead2563dcbf3bf2c9407fea4dc236faba485a', 'XRP': '0x1d2f0da169ceb9fc7b3144628db156f3f6c60dbe', 'COMP': '0x52ce071bd9b1c4b00a0b92d298c512478cad67e8', 'REEF': '0xf21768ccbc73ea5b6fd3c687208a7c2def2d966e', 'ALPHA': '0xa1faa113cbe53436df28ff0aee54275c13b40975', 'INJ': '0xa2b726b1145a4773f68593cf171187d8ebe4d495', 'EOS': '0x56b6fb708fc5732dec1afc8d8556423a2edccbd6', 'LTC': '0x4338665cbb7b2485a8855a139b75d5e34ab0db94', 'LIT': '0xb59490ab09a0f526cc7305822ac65f2ab12f9723', 'BCH': '0x8ff795a6f4d97e7887c79bea79aba5cc76444adf', 'BTCST': '0x78650b139471520656b9e7aa7a5e9276814a38e9', 'FIL': '0x0d8ce2a99bb6e3b7db580ed848240e4a0f9ae153', 'ATOM': '0x0eb3a705fc54725037cc9e008bdede697f62f335', '1INCH': '0x111111111117dc0aa78b770fa6a738034120c302', 'BAKE': '0xe02df9e3e622debdd69fb838bb799e3f168902c5', 'MKR': '0x5f0da599bb2cccfcf6fdfd7d81743b6020864350', 'ZEC': '0x1ba42e5193dfa8b03d15dd1b86a3113bbbef8eeb', 'NEAR': '0x1fa4a73a3f0133f0025378af00236f3abdee5d63', 'ETC': '0x3d6545b08693dae087e957cb1180ee38b9e3c25e', 'ONT': '0xfd7b3a77848f1c2d67e05e54d78d174a0c850335', 'BAT': '0x101d82428437127bf1608f699cd651e6abf9766e', 'DODO': '0x67ee3cb086f8a16f34bee3ca72fad36f7db929e2', 'IOTX': '0x9678e42cebeb63f23197d726b29b1cb20d0064e5', 'MIR': '0x5b6dcf557e2abe2323c48445e8cc948910d8c2c9', 'ANKR': '0xf307910a4c7bbc79691fd374889b36d8531b08e3', 'LINA': '0x762539b45a1dcce3d36d080f74d1aed37844b878', 'PAXG': '0x7950865a9140cb519342433146ed5b40c6f210f7', 'YFII': '0x7f70642d88cf1c4a3a7abb072b53b929b653eda5', 'LTO': '0x857b222fc79e1cbbf8ca5f78cb133d1b7cf34bbd', 'BURGER': '0xae9269f27437f0fcbc232d39ec814844a51d6b8f', 'CTK': '0xa8c2b8eec3d368c0253ad3dae65a5f2bbb89c929', 'TCT': '0xca0a9df6a8cad800046c1ddc5755810718b65c44', 'DOGE': '0xba2ae424d960c26247dd6c32edc70b295c744c43', 'ALPACA': '0x8f0528ce5ef7b51152a59745befdd91d97091d2f', 'DEGO': '0x3fda9383a84c05ec8f7630fe10adf1fac13241cc', 'COS': '0x96dd399f9c3afda1f194182f71600f1b65946501', 'BTS': '0xc2e1acef50ae55661855e8dcb72adb182a3cc259', 'HARD': '0xf79037f6f6be66832de4e7516be52826bc3cbcc4', 'DUSK': '0xb2bd0749dbe21f623d9baba856d3b0f0e1bfec9c', 'DEXE': '0x039cb485212f996a9dbb85a9a75d898f94d38da6', 'EPS': '0xa7f552078dcc247c2684336020c03648500c6d9f', 'SUPER': '0x51ba0b044d96c3abfca52b64d733603ccc4f0d4d', 'EGLD': '0xbf7c81fff98bbe61b40ed186e4afd6ddd01337fe', 'TLM': '0x2222227e22102fe3322098e4cbfe18cfebd57c95', 'MBOX': '0x3203c9e46ca618c8c1ce5dc67e7e9d75f5da2377', 'TKO': '0x9f589e3eabe42ebc94a44727b3f3531c0c877809', 'ZIL': '0xb86abcb37c3a4b64f74f59301aff131a1becc787', 'POLS': '0x7e624fa0e1c4abfd309cc15719b7e2580887f570', 'KEY': '0x85c128ee1feeb39a59490c720a9c563554b51d33', 'FARM': '0x4b5c23cac08a567ecf0c1ffca8372a45a5d33743', 'RAMP': '0x8519ea49c997f50ceffa444d240fb655e89248aa', 'PERL': '0x0f9e4d49f25de22c2202af916b681fbb3790497b', 'OM': '0xf78d2e7936f5fe18308a3b2951a93b6c4a41f5e2', 'XTZ': '0x16939ef78684453bfdfb47825f8a5f714f12623a', 'UNFI': '0x728c5bac3c3e370e372fc4671f9ef6916b814d8b', 'KNC': '0xfe56d5892bdffc7bf58f2e84be1b2c32d21c308b'}
    for coin in coins:
      symbol = coin+'USDT'
      binance_price = self.get_spot_price(symbol)
      oneinch_price = self.get_price_and_build_transaction(10)
      print(binance_price, oneinch_price[0], coin)
    #self.get_spot_price(pair)
    signal = None
    return signal


  def cex_dex_arb_bsc(self,symbol, amt):
    quote, asset = symbol[:-4], symbol[-4:]
    #after recieving signal
    #make sure everything's good to go to perform trade
    query = self.spot.isolated_margin_pair(symbol)
    assert query['isMarginTrade'] == True and query['isBuyAllowed'] == True and query['isSellAllowed'] == True


    #trade start
    self.spot_alt.transfer_spot_to_isolated_margin(asset='USDT', symbol=symbol, amount=amt)
    self.spot_alt.create_margin_loan(asset=asset, amount=amt, isIsolated='TRUE', symbol=symbol)
    spot.new_order(symbol=symbol,type='MARKET',side='SELL',quantity='')
    quit()
    #transfer in
    #repay 
    self.spot_alt.repay_margin_loan(asset=asset, amount=amt, isIsolated='TRUE', symbol=symbol)




    buy_quantity = [i for i in self.spot.account()['balances'] if i]
    spot.new_order(symbol=symbol,type='MARKET',side='BUY',quantity='')






address = '0xe6A2C8A9a0642797b583835D905145bb7630e8D1'
#dump_spot(coin,total_amt)
#withdraw_all(coin, float(103), address)

#short('BNBUSDT')
bot1 = bot()
bot1.screener()
quit()
bot1.cex_dex_arb_bsc("BNBUSDT", '12')
#bot1.big_move_screener()
#print(bot1.futures_wallet)

