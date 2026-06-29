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