from Bio.SeqUtils.ProtParam import ProteinAnalysis



def calculate_molecular_weight(sequence):
    """
    Calculates protein molecular weight in Daltons.
    """

    analysis = ProteinAnalysis(str(sequence))

    return analysis.molecular_weight()



def calculate_isoelectric_point(sequence):
    """
    Calculates theoretical isoelectric point (pI).
    """

    analysis = ProteinAnalysis(str(sequence))

    return analysis.isoelectric_point()



def calculate_hydrophobicity(sequence):
    """
    Calculates GRAVY hydrophobicity score.

    Positive values:
    more hydrophobic

    Negative values:
    more hydrophilic
    """

    analysis = ProteinAnalysis(str(sequence))

    return analysis.gravy()