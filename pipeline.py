from pathlib import Path
from extract_genotypes import extract_text_from_pdf, extract_genotypes
from db_config import init_table, insert_genotypes

def batch_process(folder_path, default_patient="UNKNOWN"):
    init_table()
    all_records = []

    for file_path in Path(folder_path).glob("*.pdf"):
        print(f"Processing: {file_path.name}")
        text = extract_text_from_pdf(file_path)
        genotypes = extract_genotypes(text)
        for gene, variant in genotypes:
            all_records.append((default_patient, gene, variant, file_path.name))

    if all_records:
        insert_genotypes(all_records)
        print(f"Inserted {len(all_records)} records into the database.")
    else:
        print("No genotypes found.")

if __name__ == "__main__":
    batch_process("clinical_reports/")