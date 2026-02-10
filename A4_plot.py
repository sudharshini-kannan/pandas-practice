import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("genes.csv")

# bar plot
plt.bar(df["gene"], df["length"])

plt.xlabel("Gene")
plt.ylabel("Length")
plt.title("Gene Lengths")

plt.show()
