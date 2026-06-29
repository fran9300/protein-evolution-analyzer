import matplotlib.pyplot as plt

from src.config import FIGURES_DIR
from src.constants import HYDROPHOBICITY_WINDOW_SIZE, FIGURE_WIDTH, FIGURE_HEIGHT


def create_output_folder():

    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


def plot_amino_acid_composition(composition):

    create_output_folder()


    amino_acids = list(composition.keys())

    counts = list(composition.values())


    plt.figure(figsize=(FIGURE_WIDTH,FIGURE_HEIGHT))


    plt.bar(
        amino_acids,
        counts
    )


    plt.xlabel(
        "Amino acid"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.title(
        "Amino Acid Composition"
    )

    output_file = (
            FIGURES_DIR /
            "amino_acid_composition.png"
    )

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()



def plot_hydrophobicity_profile(profile: list):
    """
    Generates hydrophobicity profile plot.
    """


    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    positions = range(
        1,
        len(profile) + 1
    )


    plt.figure(
        figsize=(FIGURE_WIDTH,FIGURE_HEIGHT)
    )


    plt.plot(
        positions,
        profile
    )


    plt.xlabel(
        "Residue position"
    )


    plt.ylabel(
        "Hydrophobicity"
    )


    plt.title(
        "Protein Hydrophobicity Profile"
    )


    output_file = (
        FIGURES_DIR /
        "hydrophobicity_profile.png"
    )


    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()


    print(
        f"Hydrophobicity profile generated: {output_file}"
    )


def plot_hydrophobicity_comparison(
        profile: list,
        window_profile: list,
        window_size: int = HYDROPHOBICITY_WINDOW_SIZE
):

    """
    Generates comparison between:
    - residue by residue hydrophobicity
    - sliding window hydrophobicity
    """


    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    plt.figure(
        figsize=(FIGURE_WIDTH,FIGURE_HEIGHT)
    )


    # Perfil por residuo

    positions = range(
        1,
        len(profile) + 1
    )


    plt.plot(
        positions,
        profile,
        label="Residue by residue"
    )


    # Sliding window

    window_positions = range(
        window_size,
        len(profile) + 1
    )


    plt.plot(
        window_positions,
        window_profile,
        label=f"Sliding window ({window_size})"
    )


    plt.axhline(
        0,
        linestyle="--"
    )


    plt.xlabel(
        "Residue position"
    )


    plt.ylabel(
        "Hydrophobicity"
    )


    plt.title(
        "Protein Hydrophobicity Analysis"
    )


    plt.legend()



    output_file = (
        FIGURES_DIR /
        "hydrophobicity_comparison.png"
    )


    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()


    print(
        f"Hydrophobicity comparison generated: {output_file}"
    )