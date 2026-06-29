import logging

from src.reports.csv_report import generate_report
from src.reports.json_report import generate_json_report

from src.visualization.plots import (
    plot_amino_acid_composition,
    plot_hydrophobicity_profile,
    plot_hydrophobicity_comparison
)


logger = logging.getLogger(__name__)



def generate_outputs(
        protein_id,
        analysis
):


    logger.info(
        "Generating outputs for %s",
        protein_id
    )


    results = analysis.protein_result



    generate_report(

        protein_id,

        results.length,

        analysis.unknown,

        analysis.unknown_percentage,

        results.weight,

        results.pI,

        results.hydrophobicity,

        results.instability_index,

        results.extinction_coefficient,

        results.secondary_structure,

        results.aliphatic_index

    )



    generate_json_report(

        protein_id,

        results.length,

        results.composition,

        analysis.unknown,

        analysis.unknown_percentage,

        results.weight,

        results.pI,

        results.hydrophobicity,

        results.instability_index,

        results.extinction_coefficient,

        results.secondary_structure,

        results.aliphatic_index

    )



    plot_amino_acid_composition(

        results.composition

    )



    plot_hydrophobicity_profile(

        results.hydro_profile

    )



    plot_hydrophobicity_comparison(

        results.hydro_profile,

        results.window_profile

    )



    logger.info(
        "Outputs generated successfully"
    )