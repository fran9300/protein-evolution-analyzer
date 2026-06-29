AMINO_ACIDS = set(
    "ACDEFGHIKLMNPQRSTVWY"
)


UNKNOWN_AMINO_ACID = "X"



def validate_sequence(sequence: str) -> bool:

    """
    Validates protein sequence.

    Allows X as unknown amino acid.
    """

    sequence = sequence.upper()


    invalid_characters = (
        set(sequence)
        - AMINO_ACIDS
        - {UNKNOWN_AMINO_ACID}
    )


    if invalid_characters:

        print(
            "Invalid amino acids found:",
            invalid_characters
        )

        return False


    return True



def count_unknown_residues(sequence: str) -> int:

    """
    Counts unknown amino acids.
    """

    return sequence.upper().count("X")



def calculate_unknown_percentage(sequence: str) -> float:

    """
    Calculates percentage of unknown residues.
    """

    unknown = count_unknown_residues(sequence)


    return (
        unknown / len(sequence)
    ) * 100


def remove_unknown_residues(sequence: str) -> str:

    """
    Removes unknown amino acids (X)
    for physicochemical calculations.
    """

    return sequence.upper().replace("X", "")