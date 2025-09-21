import streamlit as st, pandas as pd, joblib, matplotlib.pyplot as plt

st.set_page_config(page_title="AGI Path Predictor", layout="wide")
st.title("🤖 AGI Path Predictor — Grok 5 Inspired")

bench = pd.read_csv("data/bench_timeseries.csv", parse_dates=['date'])
tweets = pd.read_csv("data/tweets_with_sentiment.csv", parse_dates=['date'])
model = joblib.load("data/agi_predictor.pkl")

st.sidebar.header("Scenario controls")
simulate_arc = st.sidebar.slider("Simulate next ARC score increase (%)", -5, 50, 10)
simulate_sent = st.sidebar.slider("Simulate sentiment shift (−1 to +1)", -1.0, 1.0, 0.0)

st.subheader("ARC Benchmark vs Musk/xAI Sentiment")
fig, ax = plt.subplots(2,1,sharex=True,figsize=(8,5))
ax[0].plot(bench['date'], bench['arc_score_pct'], marker='o')
ax[0].set_ylabel("ARC score (%)")
sent_month = tweets.groupby(tweets['date'].dt.to_period('M').dt.to_timestamp()).sentiment.mean()
ax[1].bar(sent_month.index.astype(str), sent_month.values)
ax[1].set_ylabel("Mean sentiment")
plt.xticks(rotation=30)
st.pyplot(fig)

last = bench.iloc[-1]
X_input = pd.DataFrame([{
    'arc_score_pct': last['arc_score_pct'] * (1 + simulate_arc/100.0),
    'mean_sentiment': (sent_month.iloc[-1] if len(sent_month)>0 else 0.0) + simulate_sent,
    'arc_delta': last['arc_score_pct'] - bench.iloc[-2]['arc_score_pct']
}])
pred = model.predict(X_input)[0]
st.metric("Predicted AGI-progress index (0-1)", f"{pred:.3f}")

st.markdown("⚠️ This is a *proxy forecast* based on benchmarks + sentiment. Not a true AGI probability.")
