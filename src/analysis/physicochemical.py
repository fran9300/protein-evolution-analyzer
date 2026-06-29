from Bio.SeqUtils.ProtParam import ProteinAnalysis

from src.constants import HYDROPHOBICITY_WINDOW_SIZE


def calculate_molecular_weight(sequence: str) -> float:
    """
    Calculates protein molecular weight in Daltons.
    """

    analysis = ProteinAnalysis(sequence)

    return analysis.molecular_weight()



def calculate_isoelectric_point(sequence: str) -> float:
    """
    Calculates theoretical isoelectric point (pI).
    """

    analysis = ProteinAnalysis(sequence)

    return analysis.isoelectric_point()



def calculate_hydrophobicity(sequence: str) -> float:
    """
    Calculates GRAVY hydrophobicity score.

    Positive values:
    more hydrophobic

    Negative values:
    more hydrophilic
    """

    analysis = ProteinAnalysis(sequence)

    return analysis.gravy()


def calculate_hydrophobicity_profile(sequence: str) -> list:
    """
    Calculates hydrophobicity value
    for each amino acid position.
    """


    hydrophobicity_profile = []


    for amino_acid in sequence:


        analysis = ProteinAnalysis(
            amino_acid
        )


        value = analysis.gravy()


        hydrophobicity_profile.append(
            value
        )


    return hydrophobicity_profile


def calculate_sliding_window_hydrophobicity(
        sequence: str,
        window_size: int = HYDROPHOBICITY_WINDOW_SIZE
) -> list:
    """
    Calculates average hydrophobicity
    using a sliding window.
    """


    values = []


    for i in range(
        len(sequence) - window_size + 1
    ):


        window = sequence[
            i:i + window_size
        ]


        analysis = ProteinAnalysis(
            window
        )


        values.append(
            analysis.gravy()
        )


    return values


def calculate_instability_index(sequence: str) -> float:

    analysis = ProteinAnalysis(sequence)

    return analysis.instability_index()



def calculate_extinction_coefficient(sequence: str) -> dict:

    analysis = ProteinAnalysis(sequence)

    reduced, oxidized = analysis.molar_extinction_coefficient()

    return {

        "reduced": reduced,

        "oxidized": oxidized

    }


def calculate_secondary_structure(sequence: str) -> dict:

    analysis = ProteinAnalysis(sequence)

    helix, turn, sheet = (
        analysis.secondary_structure_fraction()
    )


    return {

        "alpha_helix": helix,

        "turn": turn,

        "beta_sheet": sheet

    }


    
def calculate_aliphatic_index(sequence: str) -> float:

    analysis = ProteinAnalysis(sequence)

    composition = analysis.count_amino_acids()


    length = len(sequence)


    alanine = composition["A"] / length
    valine = composition["V"] / length
    isoleucine = composition["I"] / length
    leucine = composition["L"] / length


    return (
        alanine
        +
        (2.9 * valine)
        +
        (3.9 * (isoleucine + leucine))
    ) * 100