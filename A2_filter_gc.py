import pandas as pd

# load table
df = pd.read_csv("genes.csv")

print("Original table:\n")
print(df)

# filter condition
high_gc = df[df["gc"] > 45]

print("\nFiltered (GC > 45):\n")
print(high_gc)

# save new file
high_gc.to_csv("high_gc_genes.csv", index=False)

print("\nSaved to high_gc_genes.csv")
