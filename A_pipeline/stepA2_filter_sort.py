from Bio import SeqIO
import pandas as pd

table = []

for record in SeqIO.parse("genes.fasta", "fasta"):
    seq = record.seq

    length = len(seq)
    gc = (seq.count("G") + seq.count("C")) / length * 100
    protein = seq.translate(to_stop=True)

    table.append([
        record.id,
        length,
        round(gc, 2),
        len(protein)
    ])

df = pd.DataFrame(table, columns=[
    "Gene_ID",
    "Length",
    "GC_percent",
    "Protein_length"
])

print("\nOriginal table:\n", df)

# ✅ Filter
df_filtered = df[df["GC_percent"] > 40]

# ✅ Sort
df_filtered = df_filtered.sort_values("Protein_length", ascending=False)

print("\nFiltered + Sorted:\n", df_filtered)

df_filtered.to_csv("gene_filtered.csv", index=False)

print("\nSaved → gene_filtered.csv")
