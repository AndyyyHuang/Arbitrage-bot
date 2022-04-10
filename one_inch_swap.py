from web3 import Web3
import requests
from web3.middleware import geth_poa_middleware
import time


bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
bian_busd_lis = ['1INCHBUSD', 'AAVEBUSD', 'ADABUSD', 'ADXBUSD', 'AERGOBUSD', 'AGLDBUSD', 'ALGOBUSD', 'ALICEBUSD', 'ALPACABUSD', 'ALPHABUSD', 'AMPBUSD', 'ANKRBUSD', 'ANTBUSD', 'ARBUSD', 'ATABUSD', 'ATOMBUSD', 'AUCTIONBUSD', 'AUDBUSD', 'AUDIOBUSD', 'AVABUSD', 'AVAXBUSD', 'AXSBUSD', 'BADGERBUSD', 'BAKEBUSD', 'BALBUSD', 'BANDBUSD', 'BATBUSD', 'BCHBUSD', 'BELBUSD', 'BETABUSD', 'BIFIBUSD', 'BLZBUSD', 'BNBBUSD', 'BNTBUSD', 'BNXBUSD', 'BONDBUSD', 'BTCBUSD', 'BTCSTBUSD', 'BTGBUSD', 'BTTBUSD', 'BURGERBUSD', 'BZRXBUSD', 'C98BUSD', 'CAKEBUSD', 'CELRBUSD', 'CFXBUSD', 'CHESSBUSD', 'CHRBUSD', 'CHZBUSD', 'CKBBUSD', 'CLVBUSD', 'COMPBUSD', 'COTIBUSD', 'COVERBUSD', 'CREAMBUSD', 'CRVBUSD', 'CTKBUSD', 'CTSIBUSD', 'DARBUSD', 'DASHBUSD', 'DATABUSD', 'DEGOBUSD', 'DEXEBUSD', 'DFBUSD', 'DGBBUSD', 'DIABUSD', 'DNTBUSD', 'DOCKBUSD', 'DODOBUSD', 'DOGEBUSD', 'DOTBUSD', 'DYDXBUSD', 'EGLDBUSD', 'ENJBUSD', 'ENSBUSD', 'EOSBUSD', 'EPSBUSD', 'ERNBUSD', 'ETCBUSD', 'ETHBUSD', 'EURBUSD', 'FARMBUSD', 'FILBUSD', 'FIOBUSD', 'FIROBUSD', 'FISBUSD', 'FLMBUSD', 'FLOWBUSD', 'FORBUSD', 'FORTHBUSD', 'FRONTBUSD', 'FTMBUSD', 'FTTBUSD', 'FXSBUSD', 'GALABUSD', 'GBPBUSD', 'GNOBUSD', 'GRTBUSD', 'GTCBUSD', 'HARDBUSD', 'HBARBUSD', 'HEGICBUSD', 'HIVEBUSD', 'HNTBUSD', 'HOTBUSD', 'ICPBUSD', 'ICXBUSD', 'IDEXBUSD', 'ILVBUSD', 'INJBUSD', 'IOSTBUSD', 'IOTABUSD', 'IOTXBUSD', 'IQBUSD', 'IRISBUSD', 'JSTBUSD', 'KAVABUSD', 'KEEPBUSD', 'KLAYBUSD', 'KMDBUSD', 'KNCBUSD', 'KSMBUSD', 'LINABUSD', 'LINKBUSD', 'LITBUSD', 'LPTBUSD', 'LRCBUSD', 'LTCBUSD', 'LTOBUSD', 'LUNABUSD', 'MANABUSD', 'MASKBUSD', 'MATICBUSD', 'MBOXBUSD', 'MDXBUSD', 'MINABUSD', 'MIRBUSD', 'MKRBUSD', 'MLNBUSD', 'MOVRBUSD', 'NANOBUSD', 'NEARBUSD', 'NEOBUSD', 'NMRBUSD', 'NUBUSD', 'OCEANBUSD', 'OMBUSD', 'OMGBUSD', 'ONEBUSD', 'ONTBUSD', 'PERPBUSD', 'PHABUSD', 'POLSBUSD', 'POLYBUSD', 'PONDBUSD', 'PROMBUSD', 'QIBUSD', 'QNTBUSD', 'QTUMBUSD', 'QUICKBUSD', 'RADBUSD', 'RAMPBUSD', 'RAREBUSD', 'RAYBUSD', 'REEFBUSD', 'REPBUSD', 'RGTBUSD', 'RNDRBUSD', 'ROSEBUSD', 'RSRBUSD', 'RUNEBUSD', 'RVNBUSD', 'SANDBUSD', 'SCBUSD', 'SFPBUSD', 'SHIBBUSD', 'SKLBUSD', 'SLPBUSD', 'SNXBUSD', 'SOLBUSD', 'SRMBUSD', 'STORJBUSD', 'STPTBUSD', 'STRAXBUSD', 'STXBUSD', 'SUPERBUSD', 'SUSHIBUSD', 'SXPBUSD', 'SYSBUSD', 'THETABUSD', 'TKOBUSD', 'TLMBUSD', 'TOMOBUSD', 'TORNBUSD', 'TRBBUSD', 'TRIBEBUSD', 'TRXBUSD', 'TVKBUSD', 'TWTBUSD', 'UNFIBUSD', 'UNIBUSD', 'VETBUSD', 'VTHOBUSD', 'WAVESBUSD', 'WAXPBUSD', 'WINGBUSD', 'WNXMBUSD', 'WRXBUSD', 'XECBUSD', 'XLMBUSD', 'XMRBUSD', 'XRPBUSD', 'XTZBUSD', 'XVGBUSD', 'XVSBUSD', 'YFIBUSD', 'YFIIBUSD', 'YGGBUSD', 'ZECBUSD', 'ZENBUSD', 'ZILBUSD', 'ZRXBUSD']
bian_usdt_lis = ['1INCHUSDT', 'AAVEUSDT', 'ADAUSDT', 'AGLDUSDT', 'AIONUSDT', 'AKROUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPACAUSDT', 'ALPHAUSDT', 'AMPUSDT', 'ANKRUSDT', 'ANTUSDT', 'ARDRUSDT', 'ARPAUSDT', 'ARUSDT', 'ATAUSDT', 'ATOMUSDT', 'AUDIOUSDT', 'AUDUSDT', 'AVAXUSDT', 'AXSUSDT', 'BADGERUSDT', 'BAKEUSDT', 'BALUSDT', 'BANDUSDT', 'BATUSDT', 'BCHUSDT', 'BEAMUSDT', 'BELUSDT', 'BETAUSDT', 'BLZUSDT', 'BNBUSDT', 'BNTUSDT', 'BNXUSDT', 'BONDUSDT', 'BTCSTUSDT', 'BTCUSDT', 'BTGUSDT', 'BTSUSDT', 'BTTUSDT', 'BURGERUSDT', 'BUSDUSDT', 'BZRXUSDT', 'C98USDT', 'CAKEUSDT', 'CELOUSDT', 'CELRUSDT', 'CFXUSDT', 'CHESSUSDT', 'CHRUSDT', 'CHZUSDT', 'CKBUSDT', 'CLVUSDT', 'COCOSUSDT', 'COMPUSDT', 'COSUSDT', 'COTIUSDT', 'CRVUSDT', 'CTKUSDT', 'CTSIUSDT', 'CTXCUSDT', 'CVCUSDT', 'DARUSDT', 'DASHUSDT', 'DATAUSDT', 'DCRUSDT', 'DEGOUSDT', 'DENTUSDT', 'DEXEUSDT', 'DGBUSDT', 'DIAUSDT', 'DNTUSDT', 'DOCKUSDT', 'DODOUSDT', 'DOGEUSDT', 'DOTUSDT', 'DREPUSDT', 'DUSKUSDT', 'DYDXUSDT', 'EGLDUSDT', 'ENJUSDT', 'ENSUSDT', 'EOSUSDT', 'EPSUSDT', 'ERNUSDT', 'ETCUSDT', 'ETHUSDT', 'EURUSDT', 'FARMUSDT', 'FETUSDT', 'FILUSDT', 'FIOUSDT', 'FIROUSDT', 'FISUSDT', 'FLMUSDT', 'FLOWUSDT', 'FORTHUSDT', 'FTMUSDT', 'FTTUSDT', 'FUNUSDT', 'GALAUSDT', 'GBPUSDT', 'GNOUSDT', 'GRTUSDT', 'GTCUSDT', 'GTOUSDT', 'GXSUSDT', 'HARDUSDT', 'HBARUSDT', 'HIVEUSDT', 'HNTUSDT', 'HOTUSDT', 'ICPUSDT', 'ICXUSDT', 'IDEXUSDT', 'ILVUSDT', 'INJUSDT', 'IOSTUSDT', 'IOTAUSDT', 'IOTXUSDT', 'IRISUSDT', 'JSTUSDT', 'KAVAUSDT', 'KEEPUSDT', 'KEYUSDT', 'KLAYUSDT', 'KMDUSDT', 'KNCUSDT', 'KSMUSDT', 'LENDUSDT', 'LINAUSDT', 'LINKUSDT', 'LITUSDT', 'LPTUSDT', 'LRCUSDT', 'LSKUSDT', 'LTCUSDT', 'LTOUSDT', 'LUNAUSDT', 'MANAUSDT', 'MASKUSDT', 'MATICUSDT', 'MBLUSDT', 'MBOXUSDT', 'MDTUSDT', 'MDXUSDT', 'MFTUSDT', 'MINAUSDT', 'MIRUSDT', 'MITHUSDT', 'MKRUSDT', 'MLNUSDT', 'MOVRUSDT', 'MTLUSDT', 'NANOUSDT', 'NBSUSDT', 'NEARUSDT', 'NEOUSDT', 'NKNUSDT', 'NMRUSDT', 'NPXSUSDT', 'NULSUSDT', 'NUUSDT', 'OCEANUSDT', 'OGNUSDT', 'OGUSDT', 'OMGUSDT', 'OMUSDT', 'ONEUSDT', 'ONGUSDT', 'ONTUSDT', 'ORNUSDT', 'OXTUSDT', 'PAXGUSDT', 'PERLUSDT', 'PERPUSDT', 'PHAUSDT', 'PNTUSDT', 'POLSUSDT', 'POLYUSDT', 'PONDUSDT', 'PUNDIXUSDT', 'QIUSDT', 'QNTUSDT', 'QTUMUSDT', 'QUICKUSDT', 'RADUSDT', 'RAMPUSDT', 'RAREUSDT', 'RAYUSDT', 'REEFUSDT', 'RENUSDT', 'REPUSDT', 'RGTUSDT', 'RLCUSDT', 'RNDRUSDT', 'ROSEUSDT', 'RSRUSDT', 'RUNEUSDT', 'RVNUSDT', 'SANDUSDT', 'SCUSDT', 'SFPUSDT', 'SHIBUSDT', 'SKLUSDT', 'SLPUSDT', 'SNXUSDT', 'SOLUSDT', 'SRMUSDT', 'STMXUSDT', 'STORJUSDT', 'STPTUSDT', 'STRAXUSDT', 'STXUSDT', 'SUNUSDT', 'SUPERUSDT', 'SUSHIUSDT', 'SXPUSDT', 'TCTUSDT', 'TFUELUSDT', 'THETAUSDT', 'TKOUSDT', 'TLMUSDT', 'TOMOUSDT', 'TORNUSDT', 'TRBUSDT', 'TRIBEUSDT', 'TROYUSDT', 'TRUUSDT', 'TRXUSDT', 'TWTUSDT', 'UMAUSDT', 'UNFIUSDT', 'UNIUSDT', 'UTKUSDT', 'VETUSDT', 'VITEUSDT', 'VTHOUSDT', 'WANUSDT', 'WAVESUSDT', 'WAXPUSDT', 'WINGUSDT', 'WINUSDT', 'WNXMUSDT', 'WRXUSDT', 'WTCUSDT', 'XECUSDT', 'XEMUSDT', 'XLMUSDT', 'XMRUSDT', 'XRPUSDT', 'XTZUSDT', 'XVSUSDT', 'XZCUSDT', 'YFIIUSDT', 'YFIUSDT', 'YGGUSDT', 'ZECUSDT', 'ZENUSDT', 'ZILUSDT', 'ZRXUSDT']

def get_one_inch_bian_tokens(chain):
    busd_tokens_lis = [x[:-4] for x in bian_busd_lis]
    usdt_tokens_lis = [x[:-4] for x in bian_usdt_lis]
    if chain == 'bsc':
        base_url = "https://api.1inch.exchange/v4.0/56/"
        url = "tokens"
        r = requests.get(url=base_url + url)
        data = r.json()['tokens']
        value_lis = []
        key_lis = []
        for key, value in data.items():
            key_lis.append(value['symbol'].upper())
            value_lis.append(key)
        token_lis = dict(zip(key_lis, value_lis))

    elif chain == 'ethereum':
        base_url = "https://api.1inch.exchange/v4.0/1/"
        url = "tokens"
        r = requests.get(url=base_url + url)
        data = r.json()['tokens']
        value_lis = []
        key_lis = []
        for key, value in data.items():
            key_lis.append(value['symbol'].upper())
            value_lis.append(key)
        token_lis = dict(zip(key_lis, value_lis))
    del token_lis['ETH']
    del token_lis['BUSD']
    del token_lis['BNB']
    del token_lis['KEY']
    del token_lis['YFII']
    del token_lis['BTS']

    token_lis = {key: value for key, value in token_lis.items() if key in usdt_tokens_lis}
    return token_lis


def check_allowance(sell_contract_id, sender_address, url='approve/allowance'):
    base_url = "https://api.1inch.exchange/v4.0/56/"
    params = {'tokenAddress': sell_contract_id, 'walletAddress': sender_address}
    r = requests.get(url=base_url + url, params=params)
    return r.json()


def approve_one_inch(sell_contract_id, sellAbi, sender_address, private_key, gasPrice, one_inch_contract_id=web3.toChecksumAddress("0x1111111254fb6c44bac0bed2854e76f90643097d")):
    sellTokenContract = web3.eth.contract(sell_contract_id, abi=sellAbi)
    balance = sellTokenContract.functions.balanceOf(sender_address).call()
    approve = sellTokenContract.functions.approve(one_inch_contract_id, balance).buildTransaction({
        'from': sender_address,
        'gasPrice': gasPrice,
        'nonce': web3.eth.get_transaction_count(sender_address)
    })
    signed_txn = web3.eth.account.sign_transaction(approve, private_key=private_key)
    approve_tx = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(check_allowance(sell_contract_id, sender_address))
    return approve_tx

def cal_and_bulid(data, gasPrice, slippage, sender_address):
    spend_amount = (float(data['fromTokenAmount']) + data['tx']['gas']*gasPrice)/pow(10, data['fromToken']['decimals'])
    quote_amount = (float(data['toTokenAmount'])/pow(10, data['toToken']['decimals'])) * (1-slippage/200)
    price = spend_amount/quote_amount
    gas = data['tx']['gas'] * 1.5  # 提高gaslimit
    transac = data['tx']
    transac['gas'] = gas
    transac['gasPrice'] = gasPrice
    transac['nonce'] = web3.eth.get_transaction_count(sender_address)
    del transac['value']
    return price, transac

def get_price_and_build_transaction(sender_address, sell_contract_id, buy_contract_id, amount, gasPrice, slippage, url="swap"):
    base_url = "https://api.1inch.exchange/v4.0/56/"
    params = {"fromTokenAddress": web3.toChecksumAddress(sell_contract_id),
         "toTokenAddress": web3.toChecksumAddress(buy_contract_id),
         "amount": web3.toWei(amount, 'ether'),
         "fromAddress": web3.toChecksumAddress(sender_address),
         "slippage": slippage}   # 0.5 represent 0.5%slippage
    r = requests.get(url=base_url+url, params=params)
    if r.status_code == 200:
        price, transac = cal_and_bulid(r.json(), gasPrice, slippage, sender_address)
        return price, transac
    elif r.status_code == 503:
        time.sleep(5)
        r = requests.get(url=base_url+url, params=params)
        price, transac = cal_and_bulid(r.json(), gasPrice, slippage, sender_address)
        return price, transac
    else:
        print(r.json())
        pass


def swap(transac, private_key):
    signed_txn = web3.eth.account.sign_transaction(transac, private_key=private_key)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    web3.eth.wait_for_transaction_receipt(tx_token, timeout=120, poll_latency=0.1)
    return tx_token

def get_balance(senderAddress, tokenContractAddress, tokenContractAbi):
    tokenContract = web3.eth.contract(address=tokenContractAddress, abi=tokenContractAbi)
    balance = tokenContract.functions.balanceOf(senderAddress).call()
    balance_readable = web3.fromWei(balance, 'ether')
    return balance_readable


def get_dex_balance(senderAddress, tokenContractAddress, tokenContractAbi):
    tokenContract = web3.eth.contract(address=tokenContractAddress, abi=tokenContractAbi)
    balance = tokenContract.functions.balanceOf(senderAddress).call()
    dex_balance = web3.fromWei(balance, 'ether')
    return dex_balance, tokenContract

def transfer(senderAddress, toAddress, tokenContractAddress, tokenContractAbi, private_key):
    tokenContract = web3.eth.contract(address=tokenContractAddress, abi=tokenContractAbi)
    balance = tokenContract.functions.balanceOf(senderAddress).call()
    symbol = tokenContract.functions.symbol().call()
    readable = web3.fromWei(balance, 'ether')
    tokenValue = balance
    print('balance: ' + str(readable) + symbol)
    tx_hash = tokenContract.functions.transfer(toAddress, tokenValue).buildTransaction({
        'from': senderAddress,
        'gasPrice': web3.toWei(6, 'gwei'),
        'nonce': web3.eth.get_transaction_count(senderAddress)
    })
    signed_txn = web3.eth.account.sign_transaction(tx_hash, private_key=private_key)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tokenContract.functions.allowance(senderAddress, toAddress).call()
    print("Transfer: " + web3.toHex(tx_token))





if __name__ == '__main__':
    sender_address = ""
    private_key = ""
    sell_contract_id = web3.toChecksumAddress("0x55d398326f99059fF775485246999027B3197955")
    sellAbi = """[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"_decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getOwner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]"""
    one_inch_contract_id = web3.toChecksumAddress("0x1111111254fb6c44bac0bed2854e76f90643097d")
    gasPrice = 6000000000  # low speed 15000000000 high speed
    base_url = "https://api.1inch.exchange/v4.0/56/"
    slippage = 0.5


