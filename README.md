# Tumor Genotype Extraction

This project extracts tumor genotypes from clinical PDF reports and stores them in a PostgreSQL database.

## Setup

1. Install dependencies:
    pip3 install -r requirements.txt

2. Configure your PostgreSQL database in `db_config.py`.

3. Place clinical PDF files in the `clinical_reports/` folder.

4. Run the pipeline:
    python pipeline.py
