import json
import pandas as pd
import matplotlib.pyplot as plt

def load_results():
    records = []
    with open("results/runs.jsonl") as f:
        for line in f:
            records.append(json.loads(line))
    return pd.DataFrame(records)

df = load_results()

avg = df.groupby("algorithm")["time"].mean()
avg.sort_values().plot(kind="bar")
plt.title("Average Runtime by Algorithm")
plt.ylabel("Seconds")
plt.show()
