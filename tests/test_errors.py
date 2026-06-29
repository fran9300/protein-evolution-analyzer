import pytest


from src.services.protein_service import analyze_sequence
from src.exceptions import InvalidSequenceError



def test_invalid_sequence():


    sequence = "ABC123"



    with pytest.raises(
        InvalidSequenceError
    ):

        analyze_sequence(sequence)