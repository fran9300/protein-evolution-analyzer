from src.validation import (
    validate_sequence,
    count_unknown_residues,
    remove_unknown_residues
)



def test_valid_sequence():

    sequence = "MKWVTFIS"

    assert validate_sequence(sequence)



def test_unknown_residues():

    sequence = "MKWVX"

    assert count_unknown_residues(sequence) == 1



def test_remove_unknown_residues():

    sequence = "MKXWV"

    cleaned = remove_unknown_residues(
        sequence
    )

    assert cleaned == "MKWV"