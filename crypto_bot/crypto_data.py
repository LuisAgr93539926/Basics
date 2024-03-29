import requests
from typing import Final

BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"  # Api to GET crypto info


class Coin:
    name: str
    symbol: str
    price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float
    market_cap: int
    market_cap_rank: int

    def __init__(
        self,
        *,
        name,
        symbol,
        price,
        high_24h,
        low_24h,
        price_change_24h,
        price_change_percentage_24h,
        market_cap,
        market_cap_rank,
    ) -> None:
        self.name = name
        self.symbol = symbol
        self.price = price
        self.high_24h = high_24h
        self.low_24h = low_24h
        self.price_change_24h = price_change_24h
        self.price_change_percentage_24h = price_change_percentage_24h
        self.market_cap = market_cap
        self.market_cap_rank = market_cap_rank

    def __str__(self):
        return f"#{self.market_cap_rank:<5} {self.name:<25} ({self.symbol:^5}): ${self.price:9.2f} CAD"


def get_coins() -> list[Coin]:
    parameters: dict = {"vs_currency": "cad"}
    data = requests.get(BASE_URL, params=parameters)
    json: dict = data.json()

    coin_list: list[Coin] = []
    for coin in json:
        current_coin: Coin = Coin(
            name=coin.get("name"),
            symbol=coin.get("symbol"),
            price=coin.get("current_price"),
            high_24h=coin.get("high_24h"),
            low_24h=coin.get("low_24h"),
            price_change_24h=coin.get("price_change_24h"),
            price_change_percentage_24h=coin.get("price_change_percentage_24h"),
            market_cap=coin.get("market_cap"),
            market_cap_rank=coin.get("market_cap_rank"),
        )
        coin_list.append(current_coin)

    return coin_list


if __name__ == "__main__":
    coins = get_coins()
    for coin in coins:
        print(coin)
