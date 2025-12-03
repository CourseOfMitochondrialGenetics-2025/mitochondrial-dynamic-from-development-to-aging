#!/usr/bin/env python3
"""
================================================================================
EDUCATIONAL SCRIPT 1: Introduction to mtDNA and Mutation Signatures of Aging
================================================================================

WEBINAR TOPIC: "Mitochondrial dynamic from development to aging"

PURPOSE:
This script introduces students to the fundamental concepts of mitochondrial DNA
(mtDNA) biology, specifically focusing on:
  1. Basic structure of mtDNA
  2. Understanding mtDNA deletions as mutation signatures of aging
  3. Why neurons and muscle cells are particularly vulnerable
  4. Introduction to bioinformatic analysis framework

RESEARCH ARTICLE:
"Secondary structure of the human mitochondrial genome affects formation of 
deletions" (BMC Biology, 2023)

LEARNING LEVEL: Basic (No prior bioinformatics experience assumed)

ESTIMATED TIME: 30-40 minutes

OUTPUT:
  - Visualizations of mtDNA structure
  - Summary statistics about mtDNA deletions
  - Data files for downstream analysis in Script 2

================================================================================
"""

# SECTION 1: IMPORT REQUIRED LIBRARIES
# ================================================================================
print("\n" + "="*80)
print("SECTION 1: Importing Required Libraries")
print("="*80)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

print("\n✓ Successfully imported:")
print("  - NumPy: Numerical computations")
print("  - Pandas: Data manipulation and analysis")
print("  - Matplotlib: Visualization")
print("  - Seaborn: Statistical graphics")

# Set style for better-looking plots
sns.set_theme(style="whitegrid", palette="husl")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10


# SECTION 2: WHAT IS mtDNA? - CONCEPTUAL OVERVIEW
# ================================================================================
print("\n" + "="*80)
print("SECTION 2: What is mtDNA? - Conceptual Foundation")
print("="*80)

print("""
MITOCHONDRIAL DNA (mtDNA) - THE BASICS:

1. WHAT IS IT?
   - Small circular DNA molecule (~16,569 base pairs in humans)
   - Located inside mitochondria (cellular energy-producing organelles)
   - Encodes proteins essential for energy production (ATP synthesis)
   - Each cell contains hundreds to thousands of mitochondria
   - Each mitochondrion contains multiple mtDNA copies

2. KEY DIFFERENCES FROM NUCLEAR DNA:
   ✓ Much smaller (nuclear DNA: ~3 billion bp vs mtDNA: ~16.5 thousand bp)
   ✓ Multiple copies per cell (hundreds to thousands vs 2 copies)
   ✓ Circular structure (DNA arranged in a ring, not linear like nuclear DNA)
   ✓ Higher mutation rate (~5-10x higher than nuclear DNA)
   ✓ Inherited maternally (from mother only)
   ✓ Limited DNA repair mechanisms

3. WHY DOES mtDNA ACCUMULATE MUTATIONS WITH AGE?
   - Constant energy production → oxidative stress → DNA damage
   - Continuous mtDNA turnover → more replication opportunities for errors
   - Heteroplasmy: Different mtDNA variants can coexist in same cell
   - "Selfish" mutant mtDNA replicates faster, even if dysfunctional
   - Clonal expansion: Mutant mtDNA gradually takes over the cell

4. mtDNA IN AGING:
   - Neurons (brain): First deletions detected around age 50
   - Muscle cells: Accumulation linked to muscle loss (sarcopenia) with age
   - Postmitotic tissues (can't divide): Most affected by mtDNA damage
""")


# SECTION 3: UNDERSTANDING mtDNA DELETIONS
# ================================================================================
print("\n" + "="*80)
print("SECTION 3: mtDNA Deletions - The Main Focus")
print("="*80)

print("""
WHAT IS A DELETION?

Definition: A mutation where a segment of DNA is permanently removed.

Example (simplified):
  Original mtDNA:  ATGCGATAGCTAGCTAGCTAGCTAGCTAG
                   [===========deletion=========]
  After deletion:  ATGCGATAG_________________TAG
                   (segment removed, sequence shortened)

WHY ARE DELETIONS PROBLEMATIC?

1. Loss of critical genes:
   - If deletion removes genes needed for ATP production, energy decreases
   - Cell becomes dysfunctional

2. Accumulation pattern:
   - One mutant mtDNA gets replicated many times
   - Heteroplasmy: Normal and mutant mtDNA coexist
   - When mutant exceeds 50-80% → cell becomes energy-deficient
   - Cell can die or become senescent (stops dividing)

3. Tissue-specific vulnerability:
   - NEURONS: Use massive amounts of ATP
   - MUSCLE CELLS: Also very energy-demanding
   - First tissues to show age-related mtDNA disease

KEY FINDING FROM THE RESEARCH ARTICLE:

Deletions don't randomly occur everywhere in mtDNA.
They cluster in specific "hotspot" regions, particularly:
  → Between 6-9 kb and 13-16 kb positions
  → This region is called the "CONTACT ZONE"
  → Reason: Secondary structure of single-stranded mtDNA
""")


# SECTION 4: DIRECT REPEATS AND INVERTED REPEATS
# ================================================================================
print("\n" + "="*80)
print("SECTION 4: Understanding DNA Repeats")
print("="*80)

print("""
WHAT ARE DIRECT REPEATS?

Definition: Identical DNA sequences appearing twice in the SAME orientation.

Example:
  Sequence:  ATGC.....................ATGC
             [====Direct Repeat====]

Why are they problematic?
  - During DNA replication, the replication machinery can "slip"
  - Like a train jumping between two identical tracks
  - Result: Deletion forms between the two repeats
  - The longer the repeat, the more likely to cause deletion

WHAT ARE INVERTED REPEATS?

Definition: Identical DNA sequences appearing twice in OPPOSITE orientations.

Example:
  Sequence:  ATGC.....................CGTA
             [====Inverted Repeat====]

What do they do?
  - Can fold back on themselves
  - Form hairpin or stem-loop structures
  - Important for DNA secondary structure
  - Important for forming the "CONTACT ZONE"

CONCEPT: "DIID" - The Dangerous Pattern

DIID = Direct-Inverted-Inverted-Direct

A nested pattern where:
  1. Direct repeat at position A (first strand orientation)
  2. Inverted repeats fold the DNA
  3. Another inverted repeat
  4. Direct repeat at position B (same orientation as first)

Result: Creates hotspots where deletions are 3x more likely!
""")


# SECTION 5: CREATING SAMPLE mtDNA DELETION DATA
# ================================================================================
print("\n" + "="*80)
print("SECTION 5: Creating and Exploring Sample mtDNA Deletion Data")
print("="*80)

print("\nGenerating synthetic mtDNA deletion data for educational purposes...\n")

# Set random seed for reproducibility
np.random.seed(42)

# Create sample deletion data
# Based on real patterns from the research article

# Known mtDNA parameters
MTDNA_LENGTH = 16569  # Human mtDNA length in base pairs
MAJOR_ARC_START = 5781
MAJOR_ARC_END = 16569
CONTACT_ZONE_5PRIME = (6000, 9000)  # Contact zone 5' end (6-9 kb)
CONTACT_ZONE_3PRIME = (13000, 16000)  # Contact zone 3' end (13-16 kb)

print(f"mtDNA Total Length: {MTDNA_LENGTH} bp")
print(f"Major Arc Region: {MAJOR_ARC_START} - {MAJOR_ARC_END} bp")
print(f"Contact Zone 5' (where 5' breakpoints cluster): {CONTACT_ZONE_5PRIME[0]}-{CONTACT_ZONE_5PRIME[1]} bp")
print(f"Contact Zone 3' (where 3' breakpoints cluster): {CONTACT_ZONE_3PRIME[0]}-{CONTACT_ZONE_3PRIME[1]} bp")

# Generate synthetic deletion breakpoints
# Real data shows non-uniform distribution - more deletions in contact zone

print("\nGenerating synthetic deletions with realistic hotspot pattern...")

n_deletions_in_contact_zone = 450  # 60% of deletions in contact zone
n_deletions_outside = 300  # 40% outside contact zone

# Deletions IN contact zone (the hotspot)
deletions_in_zone = []
for i in range(n_deletions_in_contact_zone):
    # 5' breakpoint (start of deletion)
    bp_5prime = np.random.randint(CONTACT_ZONE_5PRIME[0], CONTACT_ZONE_5PRIME[1])
    # 3' breakpoint (end of deletion) - must be after 5' breakpoint
    bp_3prime = np.random.randint(CONTACT_ZONE_3PRIME[0], CONTACT_ZONE_3PRIME[1])
    
    deletion_size = bp_3prime - bp_5prime
    if deletion_size > 0:
        deletions_in_zone.append({
            'breakpoint_5prime': bp_5prime,
            'breakpoint_3prime': bp_3prime,
            'deletion_size': deletion_size,
            'in_contact_zone': True,
            'deletion_center': (bp_5prime + bp_3prime) / 2
        })

# Deletions OUTSIDE contact zone
deletions_outside_zone = []
for i in range(n_deletions_outside):
    # Randomly distributed elsewhere
    bp_5prime = np.random.randint(MAJOR_ARC_START, MAJOR_ARC_END - 1000)
    bp_3prime = bp_5prime + np.random.randint(1000, 5000)
    
    deletion_size = bp_3prime - bp_5prime
    if bp_3prime <= MAJOR_ARC_END:
        deletions_outside_zone.append({
            'breakpoint_5prime': bp_5prime,
            'breakpoint_3prime': bp_3prime,
            'deletion_size': deletion_size,
            'in_contact_zone': False,
            'deletion_center': (bp_5prime + bp_3prime) / 2
        })

# Combine into single dataset
all_deletions = deletions_in_zone + deletions_outside_zone
deletions_df = pd.DataFrame(all_deletions)

print(f"\n✓ Generated {len(deletions_df)} synthetic mtDNA deletions")
print(f"  - {len(deletions_in_zone)} deletions in contact zone (hotspot)")
print(f"  - {len(deletions_outside_zone)} deletions outside contact zone")


# SECTION 6: BASIC STATISTICS
# ================================================================================
print("\n" + "="*80)
print("SECTION 6: Descriptive Statistics of mtDNA Deletions")
print("="*80)

print("\nGeneral Statistics:")
print(f"  Mean deletion size: {deletions_df['deletion_size'].mean():.0f} bp")
print(f"  Median deletion size: {deletions_df['deletion_size'].median():.0f} bp")
print(f"  Min deletion size: {deletions_df['deletion_size'].min():.0f} bp")
print(f"  Max deletion size: {deletions_df['deletion_size'].max():.0f} bp")
print(f"  Std deviation: {deletions_df['deletion_size'].std():.0f} bp")

print("\nBreakpoint Positions:")
print(f"  Mean 5' breakpoint: {deletions_df['breakpoint_5prime'].mean():.0f} bp")
print(f"  Mean 3' breakpoint: {deletions_df['breakpoint_3prime'].mean():.0f} bp")
print(f"  Mean deletion center: {deletions_df['deletion_center'].mean():.0f} bp")

print("\nComparison: Contact Zone vs. Outside:")
in_zone = deletions_df[deletions_df['in_contact_zone'] == True]
out_zone = deletions_df[deletions_df['in_contact_zone'] == False]

print(f"  In contact zone: {len(in_zone)} deletions")
print(f"    - Mean size: {in_zone['deletion_size'].mean():.0f} bp")
print(f"  Outside contact zone: {len(out_zone)} deletions")
print(f"    - Mean size: {out_zone['deletion_size'].mean():.0f} bp")


# SECTION 7: VISUALIZATIONS
# ================================================================================
print("\n" + "="*80)
print("SECTION 7: Creating Visualizations")
print("="*80)

print("\nGenerating Figure 1: Distribution of Deletion Breakpoints...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('mtDNA Deletion Analysis - Breakpoint Distributions', 
             fontsize=14, fontweight='bold', y=0.995)

# Plot 1: 5' vs 3' breakpoints (scatter)
ax1 = axes[0, 0]
in_zone_data = deletions_df[deletions_df['in_contact_zone'] == True]
out_zone_data = deletions_df[deletions_df['in_contact_zone'] == False]

ax1.scatter(out_zone_data['breakpoint_5prime'], out_zone_data['breakpoint_3prime'],
           alpha=0.4, s=30, color='gray', label='Outside contact zone')
ax1.scatter(in_zone_data['breakpoint_5prime'], in_zone_data['breakpoint_3prime'],
           alpha=0.6, s=40, color='red', label='In contact zone')

# Add contact zone boundaries
ax1.axvline(x=CONTACT_ZONE_5PRIME[0], color='blue', linestyle='--', alpha=0.5, linewidth=2)
ax1.axvline(x=CONTACT_ZONE_5PRIME[1], color='blue', linestyle='--', alpha=0.5, linewidth=2)
ax1.axhline(y=CONTACT_ZONE_3PRIME[0], color='blue', linestyle='--', alpha=0.5, linewidth=2)
ax1.axhline(y=CONTACT_ZONE_3PRIME[1], color='blue', linestyle='--', alpha=0.5, linewidth=2)

ax1.set_xlabel('5\' Breakpoint Position (bp)', fontweight='bold')
ax1.set_ylabel('3\' Breakpoint Position (bp)', fontweight='bold')
ax1.set_title('Deletion Breakpoints Scatter Plot', fontweight='bold')
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, alpha=0.3)

# Plot 2: Histogram of deletion sizes
ax2 = axes[0, 1]
ax2.hist(in_zone_data['deletion_size']/1000, bins=25, alpha=0.7, 
         label='In contact zone', color='red', edgecolor='black')
ax2.hist(out_zone_data['deletion_size']/1000, bins=25, alpha=0.7,
         label='Outside contact zone', color='gray', edgecolor='black')
ax2.set_xlabel('Deletion Size (kb)', fontweight='bold')
ax2.set_ylabel('Frequency', fontweight='bold')
ax2.set_title('Distribution of Deletion Sizes', fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3, axis='y')

# Plot 3: Density of deletions along mtDNA
ax3 = axes[1, 0]
# Create bins for mtDNA position
bins = np.arange(MAJOR_ARC_START, MAJOR_ARC_END + 500, 500)
hist_5prime, edges = np.histogram(deletions_df['breakpoint_5prime'], bins=bins)
hist_3prime, _ = np.histogram(deletions_df['breakpoint_3prime'], bins=bins)

bin_centers = (edges[:-1] + edges[1:]) / 2 / 1000  # Convert to kb

ax3.bar(bin_centers, hist_5prime, width=0.4, alpha=0.7, label="5' breakpoints", color='steelblue')
ax3.bar(bin_centers + 0.2, hist_3prime, width=0.4, alpha=0.7, label="3' breakpoints", color='coral')

# Highlight contact zone
ax3.axvspan(CONTACT_ZONE_5PRIME[0]/1000, CONTACT_ZONE_5PRIME[1]/1000, 
           alpha=0.2, color='blue', label="5' contact zone")
ax3.axvspan(CONTACT_ZONE_3PRIME[0]/1000, CONTACT_ZONE_3PRIME[1]/1000, 
           alpha=0.2, color='orange', label="3' contact zone")

ax3.set_xlabel('mtDNA Position (kb)', fontweight='bold')
ax3.set_ylabel('Number of Breakpoints', fontweight='bold')
ax3.set_title('Breakpoint Density Along mtDNA', fontweight='bold')
ax3.legend(fontsize=8, loc='upper right')
ax3.grid(True, alpha=0.3, axis='y')

# Plot 4: Box plot comparison
ax4 = axes[1, 1]
data_to_plot = [in_zone_data['deletion_size']/1000, out_zone_data['deletion_size']/1000]
bp = ax4.boxplot(data_to_plot, labels=['In Contact Zone', 'Outside Contact Zone'],
                 patch_artist=True, showmeans=True)

for patch, color in zip(bp['boxes'], ['red', 'gray']):
    patch.set_facecolor(color)
    patch.set_alpha(0.6)

ax4.set_ylabel('Deletion Size (kb)', fontweight='bold')
ax4.set_title('Deletion Size Comparison', fontweight='bold')
ax4.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('mtdna_deletion_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Figure saved as 'mtdna_deletion_analysis.png'")
plt.show()


# SECTION 8: THE "HOTSPOT" CONCEPT EXPLAINED
# ================================================================================
print("\n" + "="*80)
print("SECTION 8: Understanding the 'Hotspot' (Contact Zone)")
print("="*80)

print("""
KEY INSIGHT FROM THE RESEARCH:

The distribution of mtDNA deletions is NOT RANDOM.
They strongly cluster in specific regions - the "CONTACT ZONE"

WHY IS THIS IMPORTANT?

1. STRUCTURAL EXPLANATION:
   - Single-stranded mtDNA (during replication) forms a hairpin loop
   - Like an infinity symbol (∞) shape
   - Brings distant regions into close spatial proximity
   - When 5' breakpoint region (6-9 kb) meets 3' breakpoint region (13-16 kb)
   - Creates a "contact zone" where deletions are 3x more likely

2. BIOLOGICAL SIGNIFICANCE:
   - Not just about direct repeats (sequence similarity)
   - ALSO about 3D DNA structure (spatial proximity)
   - Two factors together determine deletion formation:
     a) Microhomology (sequence similarity between breakpoints)
     b) Spatial proximity (how close the regions are in 3D space)
   - Spatial proximity has STRONGER effect (3x stronger) than microhomology

3. AGING RELEVANCE:
   - Age-related deletions mostly occur in the contact zone
   - This explains why aging specifically increases certain mtDNA mutations
   - Different haplogroups (human genetic variants) have different contact zones
   - This could explain different aging rates in different populations!
""")

print(f"\nOur data shows this pattern:")
percentage_in_zone = (len(in_zone) / len(deletions_df)) * 100
print(f"  {percentage_in_zone:.1f}% of deletions occur in contact zone regions")
print(f"  (Even though these zones only comprise ~15% of the major arc)")
print(f"  → ~{percentage_in_zone/15:.1f}x enrichment in contact zone!")


# SECTION 9: SAVING DATA FOR NEXT SCRIPTS
# ================================================================================
print("\n" + "="*80)
print("SECTION 9: Saving Data for Next Scripts")
print("="*80)

# Save the dataframe
output_file = 'synthetic_mtdna_deletions.csv'
deletions_df.to_csv(output_file, index=False)
print(f"\n✓ Saved deletion data to '{output_file}'")

print("\nData format (first 5 rows):")
print(deletions_df.head())


# SECTION 10: SUMMARY AND NEXT STEPS
# ================================================================================
print("\n" + "="*80)
print("SECTION 10: Summary and Next Steps")
print("="*80)

print("""
WHAT YOU'VE LEARNED IN THIS SCRIPT:

✓ mtDNA is a small circular DNA in mitochondria with high mutation rate
✓ mtDNA deletions accumulate with age in energy-demanding tissues (neurons, muscle)
✓ Deletions don't occur randomly - they cluster in "hotspot" regions
✓ The hotspot (contact zone) is due to DNA secondary structure
✓ Both sequence similarity (repeats) AND spatial structure determine deletions
✓ This can help explain and predict age-related mtDNA diseases

WHAT YOU'LL LEARN IN SCRIPT 2:

Script 2: "Deletion Distribution Analysis"
  - Statistical tests to verify hotspot significance
  - Analyzing deletion center distributions
  - Comparison with theoretical random distributions
  - Introduction to logistic regression modeling
  - Real data analysis methodology

TO RUN SCRIPT 2:

  python3 scripts/02_deletion_distribution.py

OR continue exploring this data with the following analyses:
  - Calculate percentiles of deletion sizes
  - Identify the most common deletion size range
  - Test for correlations between breakpoint positions
  - Compare your findings with the published article figures
""")

print("\n" + "="*80)
print("SCRIPT 1 COMPLETED SUCCESSFULLY!")
print("="*80)
print(f"\nTimestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("\nNext: Run Script 2 to learn statistical analysis methods!\n")
