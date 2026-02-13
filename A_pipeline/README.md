# Biopython + pandas Mini Pipeline

Today I combined **Biopython + pandas** to build a small real-world bioinformatics workflow.

## 📌 Task
Analyze FASTA sequences and create a filtered gene table.

## ⚙️ Steps Performed
1. Read FASTA using Biopython (SeqIO)
2. Compute:
   - sequence length
   - GC %
3. Store results in pandas DataFrame
4. Filter genes (length and GC thresholds)
5. Export results to CSV

## 📂 Files Added

A_pipeline/a1_pipeline.py  
→ End-to-end FASTA → statistics → filtered CSV pipeline  

A_pipeline/genes.fasta  
→ Input sequences  

A_pipeline/gene_filtered.csv  
→ Filtered output table  

## ▶️ Run

```bash
cd panda/A_pipeline
python a1_pipeline.py
```

## ✅ Skills Practiced
- Sequence parsing (Biopython)
- DataFrames (pandas)
- Data filtering
- CSV export
- Building mini bioinformatics pipelines

