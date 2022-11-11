import requests


def kurs():
    url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/uzs.json'
    respons = requests.get(url)
    date = respons.json()['date']
    kurs = respons.json()['uzs']
    usd_uzs = f"{date} \n 🇺🇸 USD 1 $: 🇺🇿 UZS {kurs} so'm"

    url1 = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub/uzs.json'
    res = requests.get(url1)
    kurs1 = res.json()['uzs']
    rub_uzs = f"🇷🇺 RUB 1 rub: 🇺🇿 UZS {kurs1} so'm"

    return f"{usd_uzs} \n {rub_uzs}"


