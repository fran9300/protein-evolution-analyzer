import logging

from src.constants import (
    STANDARD_AMINO_ACIDS,
    UNKNOWN_AMINO_ACID
)


logger = logging.getLogger(__name__)



def validate_sequence(sequence: str) -> bool:

    """
    Validates protein sequence.

    Allows X as unknown amino acid.
    """


    sequence = sequence.upper()



    invalid_characters = (
        set(sequence)
        - STANDARD_AMINO_ACIDS
        - {UNKNOWN_AMINO_ACID}
    )



    if invalid_characters:


        logger.warning(
            "Invalid amino acids found: %s",
            invalid_characters
        )


        return False



    logger.info(
        "Protein sequence validation successful"
    )


    return True





def count_unknown_residues(sequence: str) -> int:

    """
    Counts unknown amino acids.
    """


    return sequence.upper().count(
        UNKNOWN_AMINO_ACID
    )





def calculate_unknown_percentage(sequence: str) -> float:

    """
    Calculates percentage of unknown residues.
    """


    if not sequence:

        return 0.0



    unknown = count_unknown_residues(
        sequence
    )


    percentage = (
        unknown / len(sequence)
    ) * 100



    logger.debug(
        "Unknown residue percentage calculated: %.2f%%",
        percentage
    )


    return percentage





def remove_unknown_residues(sequence: str) -> str:

    """
    Removes unknown amino acids (X)
    for physicochemical calculations.
    """


    cleaned_sequence = sequence.upper().replace(
        UNKNOWN_AMINO_ACID,
        ""
    )


    removed = (
        len(sequence)
        -
        len(cleaned_sequence)
    )


    if removed > 0:

        logger.info(
            "Removed %s unknown residues",
            removed
        )


    return cleaned_sequence