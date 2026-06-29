from src.models.dashboard_result import DashboardResult



def build_dashboard_result(
        protein_id,
        analysis
):

    results = analysis.protein_result


    return DashboardResult(

        protein_id=protein_id,


        length=results.length,


        molecular_weight=round(
            results.weight,
            2
        ),


        isoelectric_point=round(
            results.pI,
            2
        ),


        hydrophobicity=round(
            results.hydrophobicity,
            3
        ),


        instability_index=round(
            results.instability_index,
            2
        ),


        aliphatic_index=round(
            results.aliphatic_index,
            2
        ),


        composition=results.composition,


        secondary_structure={

            "alphaHelix": round(
                results.secondary_structure["alpha_helix"] * 100,
                2
            ),

            "turn": round(
                results.secondary_structure["turn"] * 100,
                2
            ),

            "betaSheet": round(
                results.secondary_structure["beta_sheet"] * 100,
                2
            )

        },


    )