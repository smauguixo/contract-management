# A Data Pipeline Analysis: Migrating from Pandas to Polars

> **Author's Note:** This project is a fork of an original implementation that used `pandas` with CSV/Excel files. The goal of this fork is not merely to modernize the tech stack, but to serve as a *case study* on the implications, trade-offs, and opportunities that arise when migrating a data pipeline from an *eager* paradigm (Pandas) to a *lazy*, column-oriented one (Polars/Parquet).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/smauguixo/contract-management/polars-version?labpath=absence_report_data_processing.ipynb)

## Project Overview

This repository contains a data pipeline that automates the processing and consolidation of absence reports for healthcare professionals. The core task is to integrate data from multiple sources, apply complex business rules, clean inconsistencies, and generate actionable reports, including a `LEGAL_ABSENCES` field that automates a previously manual and error-prone process.

## Engineering Analysis: Beyond a Tool Migration

The transition from Pandas/CSV to Polars/Parquet is much more than a simple performance optimization. It represents a fundamental shift in how data is modeled, processed, and interacted with. Below is an analysis of the systemic implications of this migration.

### 1. Second-Order Implications (The Domino Effect)

Changing the core tools introduces consequences that ripple throughout the system:

*   **Development and Debugging Paradigm:** The most significant change is the shift from *eager* execution (each line of code runs immediately) to *lazy* execution (an optimal execution plan is built before any computation occurs). This transforms debugging: instead of inspecting the intermediate *state* of the data, we now analyze the *logic* of the execution plan. The thinking becomes more declarative and functional.
*   **Human-Data Interaction:** Parquet files are not human-readable or easily opened by common office tools like Excel. This machine-centric optimization creates a barrier for non-technical stakeholders who could previously open a `.csv` for a quick spot-check. It highlights the need to design "data interfaces" for different types of users.
*   **Robust Data Contract:** Parquet enforces a type schema at write time. This eliminates an entire class of parsing and type conversion errors that were common with the CSV version (e.g., numeric IDs becoming `float` due to `NaN` values). The pipeline becomes inherently more reliable at its I/O boundaries.

### 2. New Opportunities Unlocked

This more solid technological foundation opens doors that were previously closed:

*   **True Scalability:** The Polars *lazy* engine can process data volumes far exceeding available RAM. Complex historical analyses (e.g., processing 5 years of reports at once), which were unfeasible with the in-memory approach of Pandas, are now possible.
*   **Expressiveness and Robustness of Business Logic:** The absence consolidation logic was re-implemented from an imperative and slow `iterrows` loop to a declarative and performant expression using window functions. This approach forces a more mathematical and abstract definition of business logic, enabling the efficient implementation of far more complex rules.
*   **Path to Production:** Polars code, with its expression-chaining style, is naturally more modular and testable. The gap between a notebook prototype and a robust production script is drastically reduced.

### 3. Technical Debt: Exposed and Created

No change comes without costs. This migration revealed existing issues and introduced new trade-offs:

*   **Exposed Debt (Algorithmic Inefficiency):** The migration forced a rewrite of the consolidation logic, exposing that the original Pandas implementation was sub-optimal even by Pandas standards. The problem wasn't just the tool, but *how* it was being used (e.g., relying on `.apply` and `iterrows`).
*   **Exposed Debt (Static Configuration):** Both projects contain hardcoded file paths (e.g., `.../2024-08/...`). A mature system should parameterize execution dates instead of requiring code changes each month.
*   **Created Debt (Knowledge Barrier):** The logic using window functions (`.over()`, `.shift()`) is more powerful but also more abstract and complex than a simple loop. This increases the learning curve for maintaining the pipeline—a conscious trade-off for performance and scalability.

### 4. Systems Thinking & Underlying Assumptions

Analyzing this pipeline as part of a larger ecosystem leads us to question some underlying assumptions:

*   **Was performance the *real* bottleneck?** The solution focuses on accelerating the processing step. However, the key business value (the `LEGAL_ABSENCES` column) already existed. What if the true bottleneck is the quality of the source data or the time spent on human validation of the final reports? Optimization must be applied to the right part of the system.
*   **The pipeline doesn't operate in a vacuum:** The code assumes the input files simply exist. The shift to Parquet implies that *upstream* processes also changed or that an undocumented conversion step exists. A real-world data system needs clear contracts with its data suppliers and consumers.

## Project Structure

```
.
├── .gitignore
├── absence_report_data_processing.ipynb
├── README.md
├── requirements.txt
├── data
│   ├── facility_id_lookup.parquet
│   └── absence_report
│       └── 2024-08
│           └── rel_2141_2024_08.parquet
├── output
│   └── absence_report
│       ├── 001_excluded_professionals.parquet
│       ├── 002_consolidation_failures.parquet
│       ├── 003_absences_consolidated.parquet
│       └── 004_professionals_consolidated.parquet
└── scripts
    └── utils.py
```

## Installation and Usage

### Run in Binder (No Local Setup):
Click the Binder badge at the top of this README to launch the notebook in your browser.

### Run Locally:
1.  **Clone the repository**: `git clone https://github.com/yourusername/your-repo-name.git`
2.  **Navigate to the project directory**: `cd your-repo-name`
3.  **Create and activate a virtual environment**: `python -m venv venv` and `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4.  **Install dependencies**: `pip install -r requirements.txt`
5.  **Run the Notebook**: `jupyter notebook absence_report_data_processing.ipynb`

Processed reports in Parquet format will be saved in the `output/absence_report/` directory.

## Dependencies

- `unidecode==1.3.8`
- `IPython==8.27.0`
- `polars==1.4.1`
- `pyarrow==16.1.0`

## Note on License and Data Usage

No license is provided for this project. The code and data in this repository are for demonstration purposes only and are not intended for use, distribution, or modification by others.

All data used in this project is fictional and for illustrative purposes only.