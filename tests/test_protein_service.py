from src.services.protein_service import analyze_sequence



def test_analyze_sequence():


    sequence = "MKTAA"



    result = analyze_sequence(
        sequence
    )



    assert result.unknown == 0


    assert result.unknown_percentage == 0


    assert result.protein_result.length == 5