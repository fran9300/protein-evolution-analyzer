from src.analysis.physicochemical import (
    calculate_molecular_weight,
    calculate_isoelectric_point,
    calculate_hydrophobicity
)



def test_molecular_weight():

    sequence = "AAAA"

    result = calculate_molecular_weight(sequence)


    assert result > 0



def test_isoelectric_point():

    sequence = "AAAA"


    result = calculate_isoelectric_point(sequence)


    assert result > 0



def test_hydrophobicity():

    sequence = "AAAA"


    result = calculate_hydrophobicity(sequence)


    assert result > 0