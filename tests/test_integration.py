from src.services.protein_service import analyze_sequence


def test_full_protein_analysis():


    sequence = "MKWVTFISLLLLFSSAYSRGILKDVAK"


    analysis = analyze_sequence(
        sequence
    )


    assert analysis.unknown == 0


    assert analysis.unknown_percentage == 0


    assert analysis.protein_result.length == len(sequence)


    assert len(
        analysis.protein_result.composition
    ) > 0


    assert analysis.protein_result.weight > 0


    assert analysis.protein_result.pI > 0


    assert analysis.protein_result.hydrophobicity != 0


    assert len(
        analysis.protein_result.hydro_profile
    ) == len(sequence)


    assert len(
        analysis.protein_result.window_profile
    ) > 0