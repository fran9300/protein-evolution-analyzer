from Bio.SeqUtils.ProtParam import ProteinAnalysis



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
        window_size: int = 20
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