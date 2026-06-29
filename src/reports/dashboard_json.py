import json

from src.config import RESULTS_DIR



def generate_dashboard_json(dashboard):


    report = {


        "proteinId": dashboard.protein_id,


        "summary": {


            "length": dashboard.length,


            "molecularWeight":
                dashboard.molecular_weight,


            "pI":
                dashboard.isoelectric_point,


            "hydrophobicity":
                dashboard.hydrophobicity,


            "instabilityIndex":
                dashboard.instability_index,


            "aliphaticIndex":
                dashboard.aliphatic_index

        },


        "composition":
            dashboard.composition,


        "structure":
            dashboard.secondary_structure,


    }



    output_file = (
        RESULTS_DIR /
        "protein_dashboard.json"
    )


    with open(output_file, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )