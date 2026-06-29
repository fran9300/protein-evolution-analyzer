class ProteinAnalysisError(Exception):
    """
    Base exception for protein analysis errors.
    """
    pass



class InvalidSequenceError(ProteinAnalysisError):
    """
    Raised when protein sequence is invalid.
    """
    pass



class FastaFileError(ProteinAnalysisError):
    """
    Raised when FASTA file cannot be loaded.
    """
    pass