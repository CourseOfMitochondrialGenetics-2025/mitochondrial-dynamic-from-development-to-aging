# Educational Webinar: Mitochondrial dynamic from development to aging

## Project Overview

This project is designed to teach students about **mitochondrial DNA (mtDNA) deletions and secondary structure analysis** as part of a scientific webinar on aging mutation signatures. 

The educational materials guide students through replicating the methodology from the research article:
**"Secondary structure of the human mitochondrial genome affects formation of deletions"** (BMC Biology, 2023)

### Learning Objectives

By completing this project, students will learn:

1. **Biological Concepts:**
   - Role of mtDNA in cellular aging
   - Types of mtDNA mutations (deletions)
   - Connection between DNA secondary structure and mutation formation
   - Concept of "direct repeats" and "inverted repeats"
   - The "contact zone" hypothesis

2. **Bioinformatics Skills:**
   - Data retrieval and parsing from biological databases (MitoBreak)
   - Statistical analysis of mutation distributions
   - Sequence analysis (repeats detection)
   - Visualization of genomic data
   - Computational modeling of DNA secondary structure

3. **Programming Skills:**
   - Python data manipulation and analysis
   - Working with genomic data formats
   - Creating publication-quality visualizations
   - Statistical testing and logistic regression

---

## Installation Guide

### System Requirements

- **Python:** 3.8 or higher
- **Operating System:** macOS, Linux, or Windows
- **RAM:** Minimum 4GB (8GB recommended)
- **Storage:** ~2GB for data and dependencies

### Step 1: Install Python

#### macOS (using Homebrew)
```bash
brew install python3
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

#### Windows
Download Python 3.8+ from [python.org](https://www.python.org) and run the installer. **Important:** Check "Add Python to PATH" during installation.

### Step 2: Create a Virtual Environment

A virtual environment isolates project dependencies from your system Python.

```bash
# Navigate to your project directory
cd /path/to/your/project

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Required Libraries

First, upgrade pip:
```bash
pip install --upgrade pip
```

Then install all dependencies:
```bash
pip install -r requirements.txt
```

### Requirements File (requirements.txt)

Create a file named `requirements.txt` in your project root with the following content:

```
numpy==1.24.3
pandas==2.0.3
scipy==1.11.2
matplotlib==3.7.2
seaborn==0.12.2
biopython==1.81
requests==2.31.0
scikit-learn==1.3.0
```

### Step 4: Verify Installation

Test that everything is installed correctly:

```bash
python3 -c "import numpy, pandas, scipy, matplotlib, seaborn, Bio, sklearn; print('All packages installed successfully!')"
```

You should see: `All packages installed successfully!`

### Step 5: Download Project Data

The project uses data from the MitoBreak database. Download the latest mtDNA deletion 

```bash
# Create data directory
mkdir -p data/raw

# Download will happen automatically in Script 1
```

---

## Project Structure

```
mitochondrial-aging-analysis/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── scripts/
│   ├── 01_mtdna_basics_intro.py       # Educational Script 1: Introduction
│   ├── 02_deletion_distribution.py    # Educational Script 2: Distribution analysis
│   ├── 03_repeat_analysis.py          # Educational Script 3: Repeat analysis
│   └── 04_secondary_structure.py      # Educational Script 4: Structure prediction
├── data/
│   ├── raw/                           # Original data files
│   ├── processed/                     # Cleaned/processed data
│   └── reference/                     # Reference sequences
├── notebooks/
│   └── exploration.ipynb              # Jupyter notebook for interactive analysis
└── output/
    ├── figures/                       # Generated plots
    └── results/                       # Analysis results
```

---

## Quick Start

### For First-Time Users

1. **Complete the installation steps above**

2. **Run the first educational script:**
   ```bash
   python3 scripts/01_mtdna_basics_intro.py
   ```

3. **Follow the comments and instructions** in each script

4. **Run scripts sequentially** (01 → 02 → 03 → 04)

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pandas'"

**Solution:** Make sure your virtual environment is activated:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

Then reinstall:
```bash
pip install pandas
```

### Issue: "Command 'python3' not found"

**Solution:** 
- On Windows, use `python` instead of `python3`
- Ensure Python is in your PATH environment variable

### Issue: Permission denied on macOS/Linux

**Solution:** Use `sudo` if needed:
```bash
sudo pip install -r requirements.txt
```

---

## Learning Resources

### Online References

- **BioPython Documentation:** https://biopython.org/wiki/Documentation
- **Pandas Tutorial:** https://pandas.pydata.org/docs/user_guide/index.html
- **Scientific Python Stack:** https://www.scipy.org/
- **mtDNA Resources:** https://mitoclub.org/

### Key Concepts Glossary

- **mtDNA:** Mitochondrial DNA - circular DNA found in mitochondria
- **Deletion:** Loss of a segment of DNA
- **Direct repeat:** Identical DNA sequence occurring twice in the same orientation
- **Inverted repeat:** Identical DNA sequence occurring twice in opposite orientations
- **Contact zone:** Region where spatially distant DNA sequences come into close proximity
- **Microhomology:** Short regions of sequence similarity between DNA regions
- **Heteroplasmy:** Presence of multiple mtDNA variants in a single cell

