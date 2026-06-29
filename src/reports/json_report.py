import json
import logging
import re

from src.config import RESULTS_DIR


logger = logging.getLogger(__name__)



def generate_json_report(
        protein_id,
        length,
        composition,
        unknown_residues,
        unknown_percentage,
        molecular_weight,
        isoelectric_point,

        hydrophobicity,
        hydro_profile,
        window_profile,

        instability_index,
        extinction_coefficient,
        secondary_structure,
        aliphatic_index
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

        "protein": {

            "id": protein_id

        },

        "sequence_quality": {

            "unknown_residues": unknown_residues,

            "unknown_percentage": unknown_percentage

        },


        "sequence_analysis": {

            "length": length,

            "amino_acid_composition": composition

        },


        "physicochemical_properties": {

            "molecular_weight": round(molecular_weight, 2),

            "isoelectric_point":  round(isoelectric_point,2),

            "hydrophobicity_analysis": {

                "average": round(
                    hydrophobicity,
                    2
                ),

                "profile": hydro_profile,

                "sliding_window": window_profile

            },

            "instability_index":  round(instability_index, 2),

            "extinction_coefficient": extinction_coefficient,

            "secondary_structure": {

            "alpha_helix_percentage": round(
                secondary_structure["alpha_helix"] * 100,
                2
                ),

            "turn_percentage": round(
                secondary_structure["turn"] * 100,
                2
                ),

            "beta_sheet_percentage": round(
                secondary_structure["beta_sheet"] * 100,
                2
                )

            },

            "aliphatic_index":  round(aliphatic_index, 3)

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



    logger.info(
        "JSON report generated: %s",
        output_file
    )