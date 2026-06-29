from src.constants import REPORT_SEPARATOR_LENGTH



def print_header():

    print("=" * REPORT_SEPARATOR_LENGTH)

    print(
        "Protein Analysis Report"
    )

    print("=" * REPORT_SEPARATOR_LENGTH)



def print_protein_info(
        protein_id,
        length
):

    print(
        "Protein ID:",
        protein_id
    )

    print(
        "Sequence length:",
        length,
        "aa"
    )



def print_sequence_quality(
        unknown,
        percentage
):

    print()

    print(
        "Sequence quality:"
    )

    print(
        "Unknown residues:",
        unknown
    )

    print(
        "Unknown percentage:",
        round(
            percentage,
            2
        ),
        "%"
    )



def print_sequence_analysis(
        length,
        composition
):

    print()

    print(
        "Sequence analysis:"
    )

    print(
        "Length:",
        length,
        "aa"
    )

    print(
        "Amino acid composition:"
    )

    print(
        composition
    )



def print_physicochemical_results(
        weight,
        pI,
        hydro,
        hydro_profile,
        window_profile,
        instability_index,
        extinction_coefficient,
        secondary_structure,
        aliphatic_index
):

    print()

    print(
        "Physicochemical properties:"
    )


    print(
        "Molecular weight:",
        round(weight,2),
        "Da"
    )


    print(
        "Isoelectric point:",
        round(pI,2)
    )


    print(
        "Hydrophobicity (GRAVY):",
        round(hydro,3)
    )


    print(
        "Hydrophobicity profile calculated:",
        len(hydro_profile),
        "values"
    )


    print(
        "Sliding window profile calculated:",
        len(window_profile),
        "values"
    )

    print(
        "instability_index:",
        round(instability_index,2)
    )

    print(
        "extinction_coefficient:",
        extinction_coefficient,
    )

    print(
        "secondary_structure:",
        secondary_structure,
    )

    print(
        "aliphatic_index:",
        round(aliphatic_index,2)
    )



def print_success():

    print()

    print(
        "Analysis completed successfully"
    )