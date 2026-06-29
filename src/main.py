from Bio import SeqIO

from report import generate_report

from physicochemical import (
    calculate_molecular_weight,
    calculate_isoelectric_point,
    calculate_hydrophobicity
)

from sequence_analysis import (
    calculate_length,
    calculate_amino_acid_composition
)

from visualization import (
    plot_amino_acid_composition
)


fasta_file = "../data/example.fasta"


protein = SeqIO.read(
    fasta_file,
    "fasta"
)


sequence = protein.seq


print("Protein ID:")
print(protein.id)


print()


print("Length:")

length = calculate_length(sequence)

print(length)


print()


print("Amino acid composition:")

composition = calculate_amino_acid_composition(sequence)

plot_amino_acid_composition(
    composition
)

print(composition)

print()


print("Physicochemical properties:")


weight = calculate_molecular_weight(sequence)

print(
    "Molecular weight:",
    round(weight, 2),
    "Da"
)


pI = calculate_isoelectric_point(sequence)

print(
    "Isoelectric point:",
    round(pI, 2)
)


hydro = calculate_hydrophobicity(sequence)

print(
    "Hydrophobicity (GRAVY):",
    round(hydro, 3)
)

generate_report(
    protein.id,
    length,
    weight,
    pI,
    hydro
)