from src.analysis.protein_analysis import analyze_protein
from src.models.protein_result import ProteinResult



def test_analyze_protein():

    sequence = "MKTAA"



    result = analyze_protein(
        sequence,
        3
    )



    assert isinstance(
        result,
        ProteinResult
    )


    assert result.length == 5


    assert result.composition["A"] == 2