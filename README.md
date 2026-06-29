# 🧬 Protein Evolution Explorer

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](https://github.com/fran9300/protein-evolution-explorer)

Bioinformatics project developed in Python for protein sequence analysis from FASTA files.

The application processes protein sequences and generates biological, physicochemical, and visualization outputs, following a modular architecture.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
  - [Sequence Analysis](#sequence-analysis)
  - [Physicochemical Analysis](#physicochemical-analysis)
- [Outputs & Reports](#outputs--reports)
  - [CSV Report](#csv-report)
  - [JSON Report](#json-report)
  - [Visualizations](#visualizations)
- [Project Architecture](#project-architecture)
- [Architecture Explanation](#architecture-explanation)
  - [Analysis Layer](#analysis-layer)
  - [Model Layer](#model-layer)
  - [Service Layer](#service-layer)
  - [Reports Layer](#reports-layer)
  - [Visualization Layer](#visualization-layer)
  - [Utils Layer](#utils-layer)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#️-usage)
- [Testing](#testing)
- [Error Handling](#error-handling)
- [Logging](#logging)
- [Example Analysis](#example-analysis)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Overview

**Protein Evolution Explorer** is a bioinformatics analysis tool capable of:

* Reading protein sequences from FASTA files.
* Validating amino acid sequences and detecting unknown residues (`X`).
* Cleaning sequences before downstream analysis.
* Calculating advanced physicochemical properties.
* Generating comprehensive reports and data visualizations.

### Core Focus
* **Clean Architecture & Separation of Responsibilities:** Modular design for scalability.
* **Robustness:** Complete unit testing, global error handling, and structured logging.
* **Reusability:** Highly decoupled services and utility layers.

---

## Features

### Sequence Analysis
* Protein sequence validation.
* Amino acid composition calculation (absolute and percentage frequency).
* Sequence length calculation.
* Unknown residue detection (`X`) and percentage calculation.

### Physicochemical Analysis
* Molecular weight calculation.
* Isoelectric point ($\text{pI}$) estimation.
* GRAVY (Grand Average of Hydropathy) hydrophobicity index.
* Residue-by-residue hydrophobicity profile.
* Sliding window hydrophobicity analysis for identifying hydrophobic regions.

## Outputs & Reports

The system generates structured data and visual charts under the `results/` directory:

```text
results/
├── protein_report.csv
├── sp_P04637_P53_HUMAN_report.json
└── figures/
    ├── amino_acid_composition.png
    ├── hydrophobicity_profile.png
    └── hydrophobicity_comparison.png
```

### CSV Report

Contains:
* Protein identifier.
* Sequence length.
* Unknown residues.
* Molecular weight.
* Isoelectric point.
* Hydrophobicity.

### JSON Report

Contains structured information:
* Sequence quality.
* Amino acid composition.
* Physicochemical properties.

### Visualizations

Generated plots:
* Amino acid composition.
* Hydrophobicity profile.
* Sliding window hydrophobicity comparison.


## Project Architecture

The project follows a layered structure:

```text
src/
├── analysis/
│   ├── sequence.py
│   ├── physicochemical.py
│   └── protein_analysis.py
│
├── models/
│   ├── protein_result.py
│   └── analysis_result.py
│
├── services/
│   ├── fasta_service.py
│   ├── protein_service.py
│   └── output_service.py
│
├── reports/
│   ├── csv_report.py
│   └── json_report.py
│
├── visualization/
│   └── plots.py
│
├── utils/
│   ├── display.py
│   └── logger.py
│
├── exceptions.py
├── validation.py
├── constants.py
├── config.py
└── main.py
```

---

## Architecture Explanation

### Analysis Layer

Responsible for biological calculations.

Examples:
* Sequence properties.
* Hydrophobicity calculations.
* Physicochemical analysis.

### Model Layer

Contains data structures used between components.

Example: `ProteinResult`

Stores:
* Length
* Composition
* Weight
* pI
* Hydrophobicity data

### Service Layer

Contains application logic.

Responsibilities:

### FASTA Service
* Loads protein sequences.

### Protein Service
Coordinates:
* Validation
* Cleaning
* Analysis

### Output Service
Coordinates:
* Reports
* Graph generation

### Reports Layer

Responsible for exporting results.

Formats:
* CSV
* JSON

### Visualization Layer

Responsible for generating biological plots using `matplotlib`.

### Utils Layer

Contains shared utilities:
* Console output.
* Logging configuration.

## Technologies

### Language
* Python 3.13

### Libraries
* Biopython
* Matplotlib
* Pytest

---

## Requirements

- Python >= 3.13
- pip

## Installation

Clone repository:
```bash
git clone https://github.com/fran9300/protein-evolution-explorer.git
```

Move into project:
```bash
cd protein-evolution-explorer
```

Create virtual environment:
```bash
python -m venv .venv
```

Activate environment:
* **Windows:**
  ```bash
  .venv\Scripts\activate
  ```
* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Run application:
```bash
python src/main.py
```

The program will:
1. Load FASTA sequence.
2. Validate protein data.
3. Perform analysis.
4. Generate reports.
5. Generate plots.

---

## Testing

Run tests:
```bash
pytest
```

Current test coverage includes:
* Validation tests.
* Sequence analysis tests.
* Physicochemical calculations.
* Protein analysis.
* FASTA loading.
* Error handling.
* Integration tests.

---

## Error Handling

The project includes custom exceptions.

Example: `InvalidSequenceError`

Used when:
* Invalid amino acids are detected.
* Protein sequences cannot be analyzed.

Also: `FastaFileError`

Used for FASTA loading problems.

---

## Logging

The application uses Python logging.

Tracked events:
* FASTA loading.
* Sequence validation.
* Protein analysis.
* Report generation.
* Visualization generation.

Example:
```text
INFO | FASTA loaded successfully
INFO | Protein physicochemical analysis completed
INFO | JSON report generated
```

---

## Example Analysis

### Input
* `p53.fasta`

### Output
```text
Protein ID:         sp|P04637|P53_HUMAN
Length:             393 aa
Molecular weight:   43652.71 Da
Isoelectric point:  6.33
Hydrophobicity:     -0.756
```

---

## Future Improvements

Possible future additions:
* [ ] Multiple FASTA file analysis.
* [ ] Database integration.
* [ ] Protein similarity comparison.
* [ ] Evolutionary analysis.
* [ ] Web interface.
* [ ] Interactive plots.

---

## Author

**Francisco Kin**
* Bioinformatics Student | Backend Development | Data Analysis
* [GitHub Profile](https://github.com/fran9300)