import pytest

from src.services.fasta_service import load_protein_sequence
from src.exceptions import FastaFileError



def test_load_fasta_error(monkeypatch):


    def mock_read(*args, **kwargs):

        raise Exception(
            "FASTA not found"
        )


    monkeypatch.setattr(
        "src.services.fasta_service.SeqIO.read",
        mock_read
    )


    with pytest.raises(FastaFileError):

        load_protein_sequence()