import requests

api_key = "62f47743afc0b39c14393502baebffd3"


def get_data(place, forecast_days, kind):
    url = (f"http://api.openweathermap.org/data/2.5/forecast"
           f"?q={place}"
           f"&appid={api_key}")

    response = requests.get(url).json()
    response = response["list"]
    forecast_days = forecast_days * 8
    response = response[:forecast_days]

    if kind == "Temperature":
        data = [item["main"]["temp"] / 10 for item in response]
    if kind == "Sky":
        data = [item["weather"][0]["main"] for item in response]

    dates = [item["dt_txt"] for item in response]

    return data, dates


if __name__ == "__main__":
    dt1, dt2 = get_data("Tokyo", 2, kind="Sky")
    print(type(get_data("Tokyo", 2, kind="Sky")))

    print(dt1)
    print(dt2)
