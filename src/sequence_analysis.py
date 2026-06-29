from Bio.Seq import Seq
from collections import Counter


def calculate_length(sequence: str) -> int:
    """
    Returns protein sequence length.
    """

    return len(sequence)


def calculate_amino_acid_composition(sequence: str) -> dict:
    """
    Calculates amino acid frequency.
    """

    return dict(
        Counter(sequence)
    )