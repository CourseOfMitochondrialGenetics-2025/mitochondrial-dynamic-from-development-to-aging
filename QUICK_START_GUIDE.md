# Quick Start Guide - Mitochondrial dynamic from development to aging

## 5-Minute Setup (For Experienced Developers)

If you already have Python 3.8+ installed:

```bash
# 1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run first script
python3 01_mtdna_basics_intro.py

# 4. Check output
ls mtdna_deletion_analysis.png  # Verify plot created
cat synthetic_mtdna_deletions.csv | head -5  # Check data
```

## 15-Minute Setup (For Beginners)

See **README.md** for detailed instructions. TL;DR version:

### macOS
```bash
# Install Python (if not already installed)
brew install python3

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python3 01_mtdna_basics_intro.py
```

### Linux (Ubuntu/Debian)
```bash
# Install Python
sudo apt-get install python3 python3-pip python3-venv

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run
python3 01_mtdna_basics_intro.py
```

### Windows
1. Download Python 3.8+ from python.org
2. Run installer (CHECK "Add Python to PATH")
3. Open Command Prompt, navigate to project folder
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python 01_mtdna_basics_intro.py
```

---

## What to Expect

### Script 1 Output

**Terminal Output:**
```
================================================================================
SECTION 1: Importing Required Libraries
================================================================================
✓ Successfully imported:
  - NumPy: Numerical computations
  - Pandas: Data manipulation and analysis
  - Matplotlib: Visualization
  - Seaborn: Statistical graphics

... [explanation sections] ...

✓ Generated 750 synthetic mtDNA deletions
  - 450 deletions in contact zone (hotspot)
  - 300 deletions outside contact zone

... [statistics] ...

✓ Figure saved as 'mtdna_deletion_analysis.png'
```

**Files Created:**
```
mtdna_deletion_analysis.png    (4-panel figure, 300 dpi)
synthetic_mtdna_deletions.csv  (750 deletion records)
```

**Time:** 5-10 minutes execution time

---

## Understanding the Script

### Why mtDNA Matters (The Problem)
```
Neurons & Muscle Cells
      ↓
  HIGH ENERGY DEMAND
      ↓
  MANY MITOCHONDRIA
      ↓
  mtDNA REPLICATION
      ↓
  MUTATIONS ACCUMULATE
      ↓
  CELL DYSFUNCTION → AGING
```

### What Makes This Special (The Insight)
```
Mutations Are NOT Random!
      ↓
  They cluster in "Contact Zones"
      ↓
  Why? DNA secondary structure
      ↓
  Single-stranded mtDNA forms a HAIRPIN LOOP
      ↓
  Distant regions come into PHYSICAL CONTACT
      ↓
  Deletions 3x MORE LIKELY in contact zones
```

### The Figure Interpretation

**Panel 1: Scatterplot (5' vs 3' breakpoints)**
- X-axis: Where deletion starts (5' breakpoint)
- Y-axis: Where deletion ends (3' breakpoint)
- RED dots: In contact zone (clustered in corner)
- GRAY dots: Outside contact zone (scattered)
- BLUE dashed lines: Contact zone boundaries
- **Interpretation:** Clear clustering visible!

**Panel 2: Histogram (Deletion sizes)**
- X-axis: Size of deletion (in kilobases)
- Y-axis: How many deletions this size
- RED bars: In contact zone
- GRAY bars: Outside
- **Interpretation:** Similar size distributions, but more deletions in zone

**Panel 3: Density plot (Along mtDNA)**
- X-axis: Position along mtDNA (0-16.5 kb)
- Y-axis: Number of breakpoints
- Blue shaded: 5' contact zone (6-9 kb)
- Orange shaded: 3' contact zone (13-16 kb)
- **Interpretation:** Peak of 5' breakpoints at 6-9 kb, peak of 3' at 13-16 kb

**Panel 4: Box plot (Size comparison)**
- Compares deletion size distributions
- Red box: Contact zone deletions
- Gray box: Outside contact zone
- **Interpretation:** Medians similar, but zone has more cases

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named..."

**Check 1:** Virtual environment activated?
```bash
which python  # Should show .../venv/bin/python
```

**Check 2:** Packages installed?
```bash
pip list | grep pandas
```

**Check 3:** Reinstall
```bash
pip install pandas --upgrade
```

### Problem: "Python command not found"

**macOS/Linux:**
```bash
which python3  # Should show installation path
python3 --version  # Should show version 3.8+
```

**Windows:**
```bash
python --version  # Should show version 3.8+
```

If not found, reinstall Python from python.org

### Problem: Plot window doesn't appear

**Try adding to top of script:**
```python
import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend
```

**Or save without displaying:**
```bash
# Already saved as PNG! Check directory:
ls -lh mtdna_deletion_analysis.png
```

### Problem: "Permission denied" on macOS/Linux

```bash
# Allow execution
chmod +x 01_mtdna_basics_intro.py

# Run with explicit python
python3 01_mtdna_basics_intro.py
```

---

## Key Concepts (Cheat Sheet)

| Term | Definition | Relevance |
|------|-----------|----------|
| **mtDNA** | Mitochondrial DNA (~16.5 kb circular) | Cell's energy DNA |
| **Deletion** | Missing segment of DNA | Causes cell dysfunction |
| **Direct Repeat** | Same sequence, same orientation | Causes deletions via slippage |
| **Inverted Repeat** | Same sequence, opposite orientation | Forms hairpin structure |
| **Contact Zone** | Region where distant DNA comes close | Where deletions cluster |
| **Heteroplasmy** | Mix of normal and mutant mtDNA | Both coexist in cells |
| **Breakpoint** | Position where deletion starts/ends | 5' (start) and 3' (end) |
| **Microhomology** | Sequence similarity between regions | Aids deletion formation |
| **Haplogroup** | mtDNA genetic variant in population | Affects aging rate |

---

## What You're Learning

### Biological Knowledge
- ✓ mtDNA structure and function
- ✓ How mutations relate to aging
- ✓ Why neurons and muscles are vulnerable
- ✓ DNA secondary structure concepts

### Bioinformatics Skills
- ✓ Python programming for biology
- ✓ Data analysis with Pandas
- ✓ Statistical visualization
- ✓ Data import/export (CSV)

### Research Methodology
- ✓ Hypothesis-driven analysis
- ✓ Exploratory data analysis
- ✓ Statistical comparison
- ✓ Figure generation for publications

---

## Next Steps

### Immediate (After Script 1)

1. **Examine the output plot:**
   - What pattern do you see?
   - Why would contact zone deletions be more damaging?
   - How would this affect an aging neuron?

2. **Analyze the CSV **
   ```bash
   # View the data
   cat synthetic_mtdna_deletions.csv
   
   # Count deletions in contact zone
   grep "True" synthetic_mtdna_deletions.csv | wc -l
   
   # Count deletions outside
   grep "False" synthetic_mtdna_deletions.csv | wc -l
   ```

3. **Read the research article:**
   - Focus on Figure 2A (similar to your plot!)
   - Read Background section for context
   - Understand why this research matters

### Short Term (This Week)

- [ ] Complete Script 1 successfully
- [ ] Understand all 10 sections
- [ ] Interpret the 4-panel figure
- [ ] Modify one parameter and rerun (optional)
- [ ] Compare to article figures

### Medium Term (Script 2 & Beyond)

- [ ] Run Script 2: Statistical analysis
- [ ] Perform hypothesis testing
- [ ] Build logistic regression model
- [ ] Analyze real or more realistic data
- [ ] Contribute to research (potentially!)

---

## Project Files

```
Your Working Directory:
├── README.md                           ← Detailed setup guide
├── QUICK_START_GUIDE.md               ← This file
├── EDUCATIONAL_MATERIALS_SUMMARY.md   ← Full documentation
├── requirements.txt                    ← Dependencies
├── 01_mtdna_basics_intro.py          ← Main script
├── mtdna_deletion_analysis.png        ← Output plot (created)
└── synthetic_mtdna_deletions.csv      ← Output data (created)
```

---

## Discussion Questions

**For Understanding:**
1. Why do you think the contact zone has more deletions?
2. What would happen if someone had many mutations in the contact zone?
3. How could this affect aging vs. living in a younger person?

**For Exploration:**
4. Can you think of other DNA structures that might affect mutations?
5. Would this apply to nuclear DNA? Why or why not?
6. How could we test this hypothesis experimentally?

**For Extension:**
7. What if we could "fix" contact zone regions?
8. Could this lead to anti-aging treatments?
9. How might this vary between individuals (haplogroups)?

---

## Common Questions

**Q: Do I need to know programming?**
A: No! The script explains everything. Python knowledge helps but isn't required.

**Q: Do I need to know biology?**
A: No! Script sections 2-4 teach the biology. Prior knowledge helps but isn't required.

**Q: How long does this take?**
A: Setup (20-30 min) + Running script (5-10 min) + Understanding (20-30 min) = ~1-1.5 hours total.

**Q: Can I modify the script?**
A: Yes! Experiment with:
- Changing the number of deletions
- Adjusting contact zone boundaries
- Adding new plots

**Q: What if something breaks?**
A: See Troubleshooting section above. Most issues are environment-related.

---

## Resources

### For This Project
- README.md - Complete setup instructions
- EDUCATIONAL_MATERIALS_SUMMARY.md - Full documentation
- 01_mtdna_basics_intro.py - The script itself (well-commented)

### External
- [Research Article](https://doi.org/10.1186/s12915-023-01606-1) - Original paper
- [MitoBreak Database](https://mitoclub.github.io/mitobreak/) - Real deletion data
- [Python Tutorial](https://www.python.org/about/gettingstarted/) - Learn Python
- [BioPython](https://biopython.org/) - Biology + Python

---

## Success Criteria

**You've successfully completed Script 1 when:**

✓ Python and packages install without errors
✓ Script runs to completion
✓ PNG figure is generated
✓ CSV data file is created
✓ Can explain the contact zone concept
✓ Can interpret the 4-panel figure
✓ Understand why this matters for aging

---

## Final Thoughts

This script teaches you **real research methodology** using **realistic data patterns** to understand **actual aging mechanisms**.

You're not just running code - you're **replicating published research**, understanding **biological significance**, and developing **bioinformatics skills**.

**Welcome to computational biology!** 🧬

---

**Ready? Let's go!**

```bash
python3 01_mtdna_basics_intro.py
```
