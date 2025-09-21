import pandas as pd, joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

bench = pd.read_csv("data/bench_timeseries.csv", parse_dates=["date"])
tweets = pd.read_csv("data/tweets_with_sentiment.csv", parse_dates=["date"])

tweets['month'] = tweets['date'].dt.to_period('M').dt.to_timestamp()
sent_agg = tweets.groupby('month').sentiment.mean().reset_index().rename(columns={'month':'date','sentiment':'mean_sentiment'})
df = bench.merge(sent_agg, on='date', how='left').fillna({'mean_sentiment':0.0})
df['arc_delta'] = df['arc_score_pct'].diff().fillna(0)

# Target = next-step ARC delta normalized
y_raw = df['arc_score_pct'].shift(-1) - df['arc_score_pct']
y = ((y_raw - y_raw.min()) / (y_raw.max() - y_raw.min() + 1e-9)).fillna(0)

X = df[['arc_score_pct','mean_sentiment','arc_delta']]

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestRegressor(n_estimators=200, random_state=42))
])
pipe.fit(X.iloc[:-1], y.iloc[:-1])

joblib.dump(pipe, "data/agi_predictor.pkl")
print("✅ Saved model to data/agi_predictor.pkl")
