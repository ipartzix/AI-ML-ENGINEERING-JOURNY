# NOTE: .groupby() clusters data, then we apply an aggregate function like .mean() or .count().
status_summary = df.groupby('Status')['Hours_Spent'].mean()

print(status_summary)
