# Healthcare Absence Management Pipeline

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/smauguixo/contract-management.git/main?labpath=absence_report_data_processing.ipynb)

Effective management of healthcare contracts and personnel is crucial for ensuring high-quality public health services. In large municipal health systems, this task involves processing vast amounts of data from multiple sources, often leading to inefficiencies and errors when done manually. This project presents a comprehensive data pipeline developed to automate the processing and consolidation of absence reports and professional records for healthcare workers within a public-private partnership framework.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

This data pipeline automates tasks like data cleaning, normalization, consolidation, and report generation using Python and `pandas`. Key features include:

- **Data Integration**: Combining absence reports with facility data into a unified dataset.
- **Data Cleaning and Normalization**: Standardizing fields and correcting inconsistencies to maintain data quality.
- **Business Rule Application**: Implementing business logic, such as reclassifying medical leaves and flagging manual review items.
- **Data Consolidation**: Aggregating absences and consolidating professional records for easier reporting and analysis.
- **Automated Report Generation**: Producing reports that streamline documentation processes, including a `LEGAL_ABSENCES` field.

**Note:** This project is intentionally limited in scope to highlight core data transformation skills. While elements like modularization, error handling, logging, and testing are not fully developed, this is to keep the focus on the data processing pipeline without making the project overly extensive.

## Project Structure

    .
    ├── .gitignore
    ├── absence_report_data_processing.ipynb
    ├── README.md
    ├── requirements.txt
    ├── data
    │   ├── facility_id_lookup.csv
    │   └── absence_report
    │       └── 2024-08
    │           ├── rel_2141_2024_08.csv
    │           └── rel_2141_2024_08.xlsx
    ├── output
    │   └── absence_report
    │       ├── 001_excluded_professionals.csv
    │       ├── 002_consolidation_failures.csv
    │       ├── 003_absences_consolidated.csv
    │       └── 004_professionals_consolidated.csv
    └── scripts
        └── utils.py

- **absence_report_data_processing.ipynb**: The main Jupyter Notebook containing the data pipeline code and explanations.
- **data/**: Directory containing input data files.
  - **facility_id_lookup.csv**: CSV file mapping facility names to their unique identifiers.
  - **absence_report/**: Directory containing monthly absence reports.
    - **rel_2141_2024_08.csv / .xlsx**: August 2024 absence reports in CSV and Excel formats.
- **output/**: Directory where the processed reports and outputs are saved.
  - **absence_report/**: Contains the generated CSV reports after processing.
    - **001_excluded_professionals.csv**: Report on excluded professionals.
    - **002_consolidation_failures.csv**: Report on data consolidation failures.
    - **003_absences_consolidated.csv**: Final consolidated absence report.
    - **004_professionals_consolidated.csv**: Final consolidated professionals report.
- **scripts/**: Contains auxiliary Python scripts and utilities.
  - **utils.py**: Utility functions used in the notebook.
- **requirements.txt**: Lists all Python dependencies required to run the project.

## Installation and Setup

You can either run this project in Binder (no local setup needed) or set it up locally.

### Run in Binder:
Click the Binder badge at the top of this README to launch the notebook in your browser without any setup.

### Run Locally:
To set up the project locally, follow these steps:

1. **Clone the repository**:

       git clone https://github.com/yourusername/your-repo-name.git

2. **Navigate to the project directory**:

       cd your-repo-name

3. **Create a virtual environment** (optional but recommended):

       python -m venv venv

4. **Activate the virtual environment**:

   - On Windows:

         venv\Scripts\activate

   - On Unix or MacOS:

         source venv/bin/activate

5. **Install the required dependencies**:

       pip install -r requirements.txt

## Usage

### Prepare the Data:

- Place the monthly absence reports in the appropriate subdirectories under `data/absence_report/`. Reports can be in CSV or Excel format.
- Ensure the `facility_id_lookup.csv` file is in the `data/` directory.

### Run the Notebook:

- Open the Jupyter Notebook:

       jupyter notebook absence_report_data_processing.ipynb

- Execute the cells sequentially to run the data pipeline. The notebook includes detailed explanations and outputs at each step.

### View the Outputs:

- Processed reports and CSV files will be saved in the `output/absence_report/` directory.
- Key output files include:
  - `001_excluded_professionals.csv`: Professionals excluded based on predefined criteria.
  - `002_consolidation_failures.csv`: Records that failed to consolidate due to data inconsistencies.
  - `003_absences_consolidated.csv`: Consolidated absence records.
  - `004_professionals_consolidated.csv`: Consolidated professional records with generated legal absences.

## Dependencies

- `pandas==2.2.2`
- `unidecode==1.3.8`
- `IPython==8.27.0`
- `openpyxl==3.1.5`

All dependencies are listed in the `requirements.txt` file and can be installed using the command:

    pip install -r requirements.txt

## Contributing

This project is part of my portfolio and is intended to demonstrate my skills in data processing and automation. While contributions are not expected, feedback or suggestions for improvements are welcome.

If you have any thoughts or find issues, feel free to open an issue.

## Note on License and Data Usage

No license is provided for this project. The code and data in this repository are for demonstration purposes only and are not intended for use, distribution, or modification by others. 

All data used in this project is fictional and for illustrative purposes only.