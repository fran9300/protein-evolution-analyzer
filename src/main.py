from Bio import SeqIO

from src.config import FASTA_PATH
from src.constants import FASTA_FORMAT

from src.services.protein_service import analyze_sequence
from src.services.output_service import generate_outputs


from src.utils.display import (
    print_header,
    print_protein_info,
    print_sequence_quality,
    print_sequence_analysis,
    print_physicochemical_results,
    print_success
)



def main():


    protein = SeqIO.read(
        FASTA_PATH,
        FASTA_FORMAT
    )


    sequence = str(protein.seq)



    print_header()


    print_protein_info(
        protein.id,
        len(sequence)
    )



    analysis = analyze_sequence(
        sequence
    )


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

    main()