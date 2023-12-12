import pandas as pd

from xgboost import XGBRegressor


"""

Example input:

{
    "bedrooms": 1,
    "bathrooms": 1,
    "latitude": 53.3490556,
    "longitude": -6.2447174,
    "ber": "B",
    "is_apartment": True,
}

"""


def predict(
    beds: int,
    baths: int,
    latitude: float,
    longitude: float,
    ber: str,
    is_apartment: bool,
    model: XGBRegressor,
):
    df = pd.DataFrame(
        {
            "bathrooms": baths,
            "bedrooms": beds,
            "ber": ber,
            "latitude": latitude,
            "longitude": longitude,
            "is_apartment": is_apartment,
        },
        index=[0],
    )
    df["ber"] = df["ber"].astype("category")
    return model.predict(df)[0]


def main():
    model = XGBRegressor()
    model.load_model("./model.json")
    prediction = predict(
        beds=1,
        baths=1,
        latitude=53.3490556,
        longitude=-6.2447174,
        ber="B",
        is_apartment=True,
        model=model,
    )
    print(prediction)


if __name__ == "__main__":
    main()
