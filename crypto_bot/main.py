from crypto_data import Coin, get_coins
import time


def alert(symbol: str, bottom: int, top: int, coin_list: list[Coin]):
    for coin in coin_list:
        if coin.symbol == symbol:
            if coin.price > top:
                print(coin, f"⚠️⚠️ ALERT ⚠️⚠️ {coin.name} is UP 📈")
            if coin.price < bottom:
                print(coin, f"⚠️⚠️ ALERT ⚠️⚠️ {coin.name} is DOWN 📉")
            else:
                print(coin)


if __name__ == "__main__":
    coins = get_coins()

    while True:
        time.sleep(30)
        alert("btc", bottom=90000, top=100000, coin_list=coins)
        alert("eth", bottom=4000, top=5000, coin_list=coins)
        alert("bnb", bottom=600, top=800, coin_list=coins)
