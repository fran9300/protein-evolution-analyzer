from src.services.protein_service import analyze_sequence
from src.services.output_service import generate_outputs
from src.services.fasta_service import load_protein_sequence

from src.config import FASTA_PATH

from src.exceptions import ProteinAnalysisError, InvalidSequenceError

from src.utils.logger import setup_logging
import logging

from src.utils.display import (
    print_header,
    print_protein_info,
    print_sequence_quality,
    print_sequence_analysis,
    print_physicochemical_results,
    print_success
)


def main():

    setup_logging()

    protein = load_protein_sequence(
        FASTA_PATH
    )


    sequence = str(protein.seq)



    print_header()


    print_protein_info(
        protein.id,
        len(sequence)
    )

    try:

        analysis = analyze_sequence(
            sequence
        )



    except InvalidSequenceError as error:

        logging.error(

            "Protein analysis failed: %s",

            error

        )

        return


    results = analysis.protein_result



    print_sequence_quality(

        analysis.unknown,

        analysis.unknown_percentage

    )



    print_sequence_analysis(

        results.length,

        results.composition

    )



    print_physicochemical_results(

        results.weight,

        results.pI,

        results.hydrophobicity,

        results.hydro_profile,

        results.window_profile

    )



    generate_outputs(

        protein.id,

        analysis

    )



    print_success()



if __name__ == "__main__":


    try:

        main()


    except ProteinAnalysisError as error:

        print(
            f"Analysis error: {error}"
        )