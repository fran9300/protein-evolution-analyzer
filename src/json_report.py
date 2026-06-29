import json
import re

from config import RESULTS_DIR



def generate_json_report(
        protein_id,
        length,
        composition,
        unknown_residues,
        unknown_percentage,
        molecular_weight,
        isoelectric_point,
        hydrophobicity
):

    """
    Generates a JSON file containing
    protein analysis results.
    """


    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    report = {


        "protein": protein_id,


        "sequence_quality": {

            "unknown_residues": unknown_residues,

            "unknown_percentage": unknown_percentage

        },


        "sequence_analysis": {


            "length": length,


            "amino_acid_composition": composition

        },


        "physicochemical_properties": {


            "molecular_weight": molecular_weight,


            "isoelectric_point": isoelectric_point,


            "hydrophobicity": hydrophobicity

        }

    }

    safe_protein_id = re.sub(
        r'[\\/*?:"<>|]',
        "_",
        protein_id
    )

    output_file = (
            RESULTS_DIR /
            f"{safe_protein_id}_report.json"
    )



    with open(
        output_file,
        "w"
    ) as file:


        json.dump(
            report,
            file,
            indent=4
        )



    print(
        f"JSON report generated: {output_file}"
    )