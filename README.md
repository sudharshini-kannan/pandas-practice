# 📊 Pandas Practice – Bioinformatics Data Analysis

This repository contains my hands-on practice for learning **pandas (Python data analysis library)** for bioinformatics workflows.

Background: Biotechnology  
Goal: Become Bioinformatics Analyst / Computational Biologist  

---

# 🎯 Why pandas?

In bioinformatics:
- Biopython → handles sequences (FASTA/FASTQ)
- pandas → handles tables (CSV/TSV/metadata)

Most real-world analysis involves working with tables like:
- gene information
- GC content
- BLAST results
- quality metrics
- expression data

So pandas is an essential skill.

---

# ✅ Topics Covered

✔ Reading CSV files  
✔ DataFrames  
✔ Filtering rows  
✔ Basic statistics (mean, max, min)  
✔ Saving results  
✔ Data visualization (matplotlib plots)

---

# 📂 Project Structure

A1_read_csv.py  
→ Load CSV file into pandas DataFrame  

A2_filter_gc.py  
→ Filter genes based on GC percentage  

A3_stats.py  
→ Calculate summary statistics (mean, max, min)  

A4_plot.py  
→ Plot gene lengths using matplotlib  

genes.csv  
→ Sample dataset for practice  

---

# 🛠 Tech Stack
- Python
- pandas
- matplotlib
- Ubuntu Linux
- VS Code
- Git & GitHub

---

# 🚀 Example Skills Demonstrated

- Data cleaning
- Filtering biological data
- Statistical analysis
- Visualization
- Automation using Python

---

---

# 🆕 Biopython + pandas Mini Pipeline

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

