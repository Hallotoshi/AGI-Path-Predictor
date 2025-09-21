import json, subprocess, os, datetime as dt
import pandas as pd
from textblob import TextBlob

os.makedirs("data", exist_ok=True)

# ---- 1) ARC-AGI benchmark proxy (synthetic demo) ----
dates = pd.date_range(end=dt.date.today(), periods=20, freq='M')
arc_scores = pd.Series([max(0, min(100, 5 + i*4 + (i%3)*3)) for i in range(len(dates))], index=dates)

bench_df = pd.DataFrame({"date": dates, "arc_score_pct": arc_scores.values})
bench_df.to_csv("data/bench_timeseries.csv", index=False)
print("✅ Saved data/bench_timeseries.csv")

# ---- 2) X (Twitter) posts sentiment via snscrape ----
def snscrape_search(query, limit=200):
    out = subprocess.run(
        ["snscrape", "--jsonl", "twitter-search", query],
        capture_output=True, text=True
    )
    lines = out.stdout.strip().splitlines()
    return [json.loads(l) for l in lines[:limit]]

queries = ['"Grok" lang:en', '"xAI" lang:en', 'from:elonmusk lang:en']
tweets = []
for q in queries:
    try:
        tweets += snscrape_search(q)
    except Exception as e:
        print("⚠️ snscrape failed:", e)

seen, clean = set(), []
for t in tweets:
    if t.get('id') not in seen:
        seen.add(t['id'])
        clean.append({
            "id": t.get('id'),
            "date": t.get('date'),
            "content": t.get('content'),
            "user": t.get('user', {}).get('username')
        })

tweets_df = pd.DataFrame(clean)
def sentiment_score(txt): return TextBlob(txt).sentiment.polarity
tweets_df['sentiment'] = tweets_df['content'].fillna("").apply(sentiment_score)

tweets_df.to_csv("data/tweets_with_sentiment.csv", index=False)
print("✅ Saved data/tweets_with_sentiment.csv")
