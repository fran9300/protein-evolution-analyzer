from Bio import SeqIO

from src.config import FASTA_PATH
from src.constants import FASTA_FORMAT
from src.exceptions import FastaFileError



def load_protein_sequence():


    try:

        protein = SeqIO.read(
            FASTA_PATH,
            FASTA_FORMAT
        )


        return protein


    except Exception as error:


        raise FastaFileError(
            f"Could not load FASTA file: {error}"
        )