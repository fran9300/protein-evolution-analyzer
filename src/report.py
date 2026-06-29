import csv
import os

from src.config import RESULTS_DIR


def generate_report(
        protein_id,
        length,
        molecular_weight,
        isoelectric_point,
        hydrophobicity
):
    """
    Generates a CSV report with protein analysis results.
    """

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = RESULTS_DIR / "protein_report.csv"


    with open(file_path, "w", newline="") as file:

        writer = csv.writer(file)


        writer.writerow([
            "Protein",
            "Length",
            "Molecular Weight",
            "Isoelectric Point",
            "Hydrophobicity"
        ])


        writer.writerow([
            protein_id,
            length,
            molecular_weight,
            isoelectric_point,
            hydrophobicity
        ])


    print(f"Report generated: {file_path}")