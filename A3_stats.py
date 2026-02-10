import pandas as pd

df = pd.read_csv("genes.csv")

print("Table:\n")
print(df)

print("\nStatistics:\n")

print("Average length:", df["length"].mean())
print("Max length:", df["length"].max())
print("Min length:", df["length"].min())

print("Average GC%:", df["gc"].mean())
