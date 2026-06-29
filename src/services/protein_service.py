from src.validation import (
    validate_sequence,
    count_unknown_residues,
    calculate_unknown_percentage,
    remove_unknown_residues
)

from src.analysis.protein_analysis import analyze_protein

from src.constants import HYDROPHOBICITY_WINDOW_SIZE

from src.models.analysis_result import AnalysisResult

from src.exceptions import InvalidSequenceError



def analyze_sequence(sequence: str):


    if not validate_sequence(sequence):

        raise InvalidSequenceError(
            "Invalid protein sequence"
        )



    unknown = count_unknown_residues(
        sequence
    )


    unknown_percentage = calculate_unknown_percentage(
        sequence
    )


    clean_sequence = remove_unknown_residues(
        sequence
    )



    results = analyze_protein(
        clean_sequence,
        HYDROPHOBICITY_WINDOW_SIZE
    )



    return AnalysisResult(

        unknown=unknown,

        unknown_percentage=unknown_percentage,

        protein_result=results

    )