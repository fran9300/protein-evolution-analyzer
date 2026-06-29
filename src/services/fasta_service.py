import logging

from Bio import SeqIO

from src.constants import FASTA_FORMAT
from src.exceptions import FastaFileError


logger = logging.getLogger(__name__)


def load_protein_sequence(
        fasta_path
):

    try:

        logger.info(
            "Loading FASTA file: %s",
            fasta_path
        )


        protein = SeqIO.read(
            fasta_path,
            FASTA_FORMAT
        )


        logger.info(
            "FASTA loaded successfully: %s",
            protein.id
        )


        return protein



    except Exception as error:


        logger.exception(
            "Failed loading FASTA file"
        )


        raise FastaFileError(
            f"Could not load FASTA file: {error}"
        )