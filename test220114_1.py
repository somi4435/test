import time
import pyupbit
import datetime

access = "z62CxziN1VXW4xCvMa7t4K3vxrGG4AmurIpSHdDo"
secret = "rMs0rCDaNjeI7F0AqaWnCKabzbMLpdd5sgJmrdwb"
# access = "3xIrSmvjAsEvcxK36ZMjKgdYuSoOPYx1isMXLJkz"
# secret = "PvQL56FMwyvqKggSG6Yk0UExEOaodcz6g6DPexFx"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETH") # 그냥 9시 가져오는거
        end_time = start_time + datetime.timedelta(days=1)

        #9시 - 8시 59분 50초 사이일 때
        if start_time < now < end_time - datetime.timedelta(seconds=60):
            #이더리움
            target_price = get_target_price("KRW-ETH", 0.5)
            current_price = get_current_price("KRW-ETH")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-ETH", krw*0.9995)

            #니어프로토콜
            target_price = get_target_price("KRW-NEAR", 0.5)
            current_price = get_current_price("KRW-NEAR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-NEAR", krw*0.9995) 

            #도지
            target_price = get_target_price("KRW-DOGE", 0.5)
            current_price = get_current_price("KRW-DOGE")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-DOGE", krw*0.9995) 

            #메디블록
            target_price = get_target_price("KRW-MED", 0.5)
            current_price = get_current_price("KRW-MED")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-MED", krw*0.9995)
            
            #위믹스
            target_price = get_target_price("KRW-WEMIX", 0.5)
            current_price = get_current_price("KRW-WEMIX")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-WEMIX", krw*0.9995)    
            
            #비트코인
            target_price = get_target_price("KRW-BTC", 0.5)
            current_price = get_current_price("KRW-BTC")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)       

            #샌드박스
            target_price = get_target_price("KRW-SAND", 0.5)
            current_price = get_current_price("KRW-SAND")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-SAND", krw*0.9995)   

            #리플
            target_price = get_target_price("KRW-XRP", 0.5)
            current_price = get_current_price("KRW-XRP")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-XRP", krw*0.9995)   

            #파워렛저
            target_price = get_target_price("KRW-POWR", 0.5)
            current_price = get_current_price("KRW-POWR")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-POWR", krw*0.9995)   

            #스테이터스네트워크
            target_price = get_target_price("KRW-SNT", 0.5)
            current_price = get_current_price("KRW-SNT")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-SNT", krw*0.9995)          

            #코스모스
            target_price = get_target_price("KRW-ATOM", 0.5)
            current_price = get_current_price("KRW-ATOM")
            if target_price < current_price:
                krw = get_balance("KRW")
                if krw > 5000: #돈 있으면 산다.
                    upbit.buy_market_order("KRW-ATOM", krw*0.9995)                                                      
        #10초동안 전량 매도
        else:
            btc = get_balance("ETH")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ETH", btc*0.9995)
            btc = get_balance("NEAR")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-NEAR", btc*0.9995)
            btc = get_balance("DOGE")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-DOGE", btc*0.9995)
            btc = get_balance("MED")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-MED", btc*0.9995)
            btc = get_balance("WEMIX")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-WEMIX", btc*0.9995)
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
            btc = get_balance("SAND")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-SAND", btc*0.9995)
            btc = get_balance("XRP")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-XRP", btc*0.9995)
            btc = get_balance("POWR")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-POWR", btc*0.9995)
            btc = get_balance("SNT")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-SNT", btc*0.9995)
            btc = get_balance("ATOM")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ATOM", btc*0.9995)

        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)