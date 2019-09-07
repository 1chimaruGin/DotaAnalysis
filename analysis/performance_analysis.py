import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

data = pd.read_excel('analysis/finale.xlsx')
data = data.dropna()

features = [
 'assists',
 'cluster',
 'deaths',
 'duration',
 'gold_per_min',
 'hero_damage',
 'hero_healing',
 'kda',
 'kills',
 'kills_per_min',
 'last_hits',
 'total_gold',
 'tower_damage',
 'xp_per_min'
]

X = data[features]
y = data['rank_tier']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=6)

regressor = DecisionTreeRegressor(max_depth=23)
regressor.fit(X_train, y_train)

y_prediction = regressor.predict(X_test)


def rank_tier(play):
    return regressor.predict([play])
