import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gene_filtered.csv")

print(df.columns)   # debug line

# Length histogram
plt.figure()
plt.hist(df["Length"], bins=10)
plt.xlabel("Gene Length")
plt.ylabel("Count")
plt.title("Gene Length Distribution")
plt.savefig("length_hist.png")
plt.close()

# GC histogram
plt.figure()
plt.hist(df["GC_percent"], bins=10)
plt.xlabel("GC %")
plt.ylabel("Count")
plt.title("GC Content Distribution")
plt.savefig("gc_hist.png")
plt.close()

print("Plots saved: length_hist.png, gc_hist.png")

# -------------------------
# Scatter: Length vs GC
# -------------------------
plt.figure()
plt.scatter(df["Length"], df["GC_percent"])
plt.xlabel("Gene Length")
plt.ylabel("GC %")
plt.title("Length vs GC Content")
plt.savefig("length_vs_gc.png")
plt.close()
