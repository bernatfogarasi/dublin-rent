import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV


def train(X: pd.DataFrame, y: pd.Series, save_path=None) -> XGBRegressor:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    param_grid = {
        "learning_rate": [0.3, 0.2, 0.1, 0.01, 0.001],
        "n_estimators": [20, 30, 50, 100, 200, 300],
        "max_depth": [2, 3, 4],
    }

    regressor = XGBRegressor(enable_categorical=True, random_state=42)

    grid_search = GridSearchCV(
        estimator=regressor,
        param_grid=param_grid,
        cv=5,
        scoring="neg_mean_squared_error",
    )

    grid_search.fit(X_train, y_train)

    if save_path:
        grid_search.best_estimator_.save_model(save_path)

    return grid_search.best_estimator_


def main():
    df = pd.read_csv("./data.csv")
    X = df.drop("monthly_price", axis=1)
    X["ber"] = X["ber"].astype("category")
    y = df["monthly_price"]
    train(X, y, "model.json")


if __name__ == "__main__":
    main()
