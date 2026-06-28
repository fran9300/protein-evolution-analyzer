from Bio.Seq import Seq


def calculate_length(sequence):
    """
    Calculates the number of amino acids in a protein sequence.
    """

    return len(sequence)


def calculate_amino_acid_composition(sequence):
    """
    Calculates the frequency of each amino acid.
    """

    amino_acids = {}

    for amino_acid in sequence:

        if amino_acid in amino_acids:
            amino_acids[amino_acid] += 1

        else:
            amino_acids[amino_acid] = 1


    return amino_acids