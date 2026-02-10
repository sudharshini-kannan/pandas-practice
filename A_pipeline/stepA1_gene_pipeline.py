from Bio import SeqIO
import pandas as pd

records = []
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

print(df)

df.to_csv("gene_summary.csv", index=False)

print("\nSaved results → gene_summary.csv")
