from src.analysis.sequence import (
    calculate_length,
    calculate_amino_acid_composition
)

from src.analysis.physicochemical import (
    calculate_molecular_weight,
    calculate_isoelectric_point,
    calculate_hydrophobicity,
    calculate_hydrophobicity_profile,
    calculate_sliding_window_hydrophobicity,
    calculate_instability_index,
    calculate_extinction_coefficient,
    calculate_secondary_structure,
    calculate_aliphatic_index
)

from src.models.protein_result import ProteinResult



def analyze_protein(
        sequence,
        window_size
) -> ProteinResult:


    length = calculate_length(
        sequence
    )


    composition = calculate_amino_acid_composition(
        sequence
    )


    weight = calculate_molecular_weight(
        sequence
    )


    pI = calculate_isoelectric_point(
        sequence
    )


    hydrophobicity = calculate_hydrophobicity(
        sequence
    )

    instability_index = calculate_instability_index(
        sequence
    )

    extinction_coefficient = calculate_extinction_coefficient(
        sequence
    )

    secondary_structure = calculate_secondary_structure(
        sequence
    )

    aliphatic_index = calculate_aliphatic_index(
        sequence
    )


    hydro_profile = calculate_hydrophobicity_profile(
        sequence
    )


    window_profile = calculate_sliding_window_hydrophobicity(
        sequence,
        window_size
    )



    return ProteinResult(

        length=length,

        composition=composition,

        weight=weight,

        pI=pI,

        hydrophobicity=hydrophobicity,

        instability_index=instability_index,

        extinction_coefficient=extinction_coefficient,

        secondary_structure=secondary_structure,

        aliphatic_index=aliphatic_index,

        hydro_profile=hydro_profile,

        window_profile=window_profile

    )