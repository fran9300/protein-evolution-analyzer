# 🧬 Protein Evolution Analyzer

<p>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/python-3.13-blue.svg" alt="Python Version">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
  </a>
  <a href="https://github.com/fran9300/protein-evolution-analyzer">
    <img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests">
  </a>
</p>

Bioinformatics analysis engine developed in Python for protein sequence processing from FASTA files.

This project is responsible for protein sequence validation, physicochemical analysis, and biological property calculation. It can be used independently through a local CLI or integrated as a service through FastAPI.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Mode](#api-mode)
- [Testing](#testing)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Overview

**Protein Evolution Analyzer** is the bioinformatics analysis component of the *Protein Evolution Explorer* platform.

The system processes FASTA protein sequences and generates biological analysis data including:

* **Sequence validation:** Detection of unknown amino acids and length verification.
* **Physicochemical analysis:** Molecular weight, isoelectric point (pI), GRAVY index, instability, and aliphatic index.
* **Structural properties:** Alpha helix, beta sheet, and turn percentages.

The analyzer can run locally through a command-line interface or expose its functionality through a FastAPI service, which is currently integrated with a Spring Boot backend that manages persistence.

---

## Features

### Sequence Analysis
* FASTA file loading and validation.
* Unknown amino acid detection.
* Amino acid composition and sequence length calculation.

### Physicochemical Analysis
* Molecular weight and Isoelectric point (pI) estimation.
* GRAVY hydrophobicity index and hydrophobicity profile generation.
* Instability and aliphatic index calculation.

### Structural Analysis
* Alpha helix percentage.
* Beta sheet percentage.
* Turn percentage.

### Reports & Visualization
Generates structured reports and data visualizations:

```text
results/
├── protein_report.json
├── protein_report.csv
└── figures/
    ├── amino_acid_composition.png
    ├── hydrophobicity_profile.png
    └── hydrophobicity_comparison.png
```

---

## Project Architecture

The analyzer follows a modular architecture separating biological analysis, API exposure, and local execution.

```text
src/
├── analysis/
│   ├── sequence.py
│   ├── physicochemical.py
│   └── protein_analysis.py
├── cli/
│   └── analyze_local.py
├── api/
│   └── routes.py
├── models/
├── services/
├── reports/
├── visualization/
├── utils/
├── exceptions.py
├── validation.py
└── main.py
```

### Core Components

* **Analysis Layer:** Responsible for FASTA processing, protein sequence calculations, and biological property extraction.
* **CLI Layer:** Provides local execution for manual FASTA analysis, local experiments, and report generation.
* **API Layer:** FastAPI service responsible for receiving analysis requests and returning structured protein analysis data to external applications (e.g., Spring Boot backend).

---

## Technologies

* **Language:** Python 3.13
* **Main Libraries:** Biopython, FastAPI, Pydantic, Matplotlib, Pandas, Pytest
* **Bioinformatics:** FASTA processing, amino acid composition, and physicochemical property workflows.
* **Development Tools:** Git, Virtual environments, REST APIs, Docker *(planned integration)*.

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/fran9300/protein-evolution-analyzer.git
cd protein-evolution-analyzer
```

2. **Create a virtual environment:**
```bash
python -m venv .venv
```

3. **Activate the environment:**
* **Windows:**
```bash
.venv\Scripts\activate
```
* **Linux / macOS:**
```bash
source .venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## Usage

### Local CLI Analysis
To run the manual analysis pipeline, execute:
```bash
python src/cli/analyze_local.py
```
The CLI will load the FASTA file, validate the sequence, perform the protein analysis, and generate the corresponding reports and visualizations.

---

## API Mode

To start the FastAPI service:
```bash
uvicorn src.main:app --reload
```
Once running, the interactive API documentation will be available at:
 **http://localhost:8000/docs**

> **Note:** This service is designed to be consumed by the Spring Boot backend as part of the ecosystem of the platform.

---

## Testing

To execute the test suite (includes sequence validation, property calculations, and error handling workflows), run:
```bash
pytest
```

---

## Future Improvements

* [ ] Multiple FASTA files parallel processing.
* [ ] Protein similarity comparison and alignment.
* [ ] Evolutionary analysis workflows.
* [ ] Database integration for caching results.
* [ ] Advanced interactive visualizations.
* [ ] Docker Compose deployment.

---

## Author

**Francisco Kin**
* Bioinformatics Student | Backend Development | Data Analysis
* **GitHub:** [@fran9300](https://github.com/fran9300)