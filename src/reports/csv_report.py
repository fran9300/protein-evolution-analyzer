import csv
import logging

from src.config import RESULTS_DIR


logger = logging.getLogger(__name__)



def generate_report(
        protein_id,
        length,
        unknown_residues,
        unknown_percentage,
        molecular_weight,
        isoelectric_point,
        hydrophobicity,
        instability_index,
        extinction_coefficient,
        secondary_structure,
        aliphatic_index
):

    """
    Generates a CSV report with protein analysis results.
    """


    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    file_path = RESULTS_DIR / "protein_report.csv"



    with open(
        file_path,
        "w",
        newline=""
    ) as file:


        writer = csv.writer(file)



        writer.writerow([

            "Protein",

            "Length",

            "Unknown Residues",

            "Unknown Percentage",

            "Molecular Weight",

            "Isoelectric Point",

            "Hydrophobicity",

            "instability_index",

            "extinction_coefficient",

            "secondary_structure",

            "aliphatic_index"

        ])



        writer.writerow([

            protein_id,

            length,

            unknown_residues,

            unknown_percentage,

            molecular_weight,

            isoelectric_point,

            hydrophobicity,

            instability_index,

            extinction_coefficient,

            secondary_structure,

            aliphatic_index

        ])



    logger.info(
        "CSV report generated: %s",
        file_path
    )