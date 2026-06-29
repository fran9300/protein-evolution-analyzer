from src.analysis.sequence import (
    calculate_length,
    calculate_amino_acid_composition
)


def test_calculate_length():

    sequence = "MKTAA"

    result = calculate_length(sequence)

    assert result == 5



def test_amino_acid_composition():

    sequence = "MKTAA"

    result = calculate_amino_acid_composition(sequence)


    assert result["A"] == 2
    assert result["M"] == 1
    assert result["K"] == 1
    assert result["T"] == 1