import logging

import matplotlib.pyplot as plt

from src.config import FIGURES_DIR
from src.constants import (
    HYDROPHOBICITY_WINDOW_SIZE,
    FIGURE_SIZE
)


logger = logging.getLogger(__name__)


def create_output_folder():

    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )



def plot_amino_acid_composition(composition):

    create_output_folder()


    amino_acids = list(composition.keys())

    counts = list(composition.values())


    plt.figure(
        figsize=FIGURE_SIZE
    )


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


    plt.grid(
        True
    )


    output_file = (
        FIGURES_DIR /
        "amino_acid_composition.png"
    )


    plt.tight_layout()


    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()


    logger.info(
        "Amino acid composition generated: %s",
        output_file
    )



def plot_hydrophobicity_profile(profile: list):

    """
    Generates hydrophobicity profile plot.
    """


    create_output_folder()


    positions = range(
        1,
        len(profile) + 1
    )


    plt.figure(
        figsize=FIGURE_SIZE
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


    plt.grid(
        True
    )


    output_file = (
        FIGURES_DIR /
        "hydrophobicity_profile.png"
    )


    plt.tight_layout()


    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()


    logger.info(
        "Hydrophobicity profile generated: %s",
        output_file
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


    create_output_folder()



    plt.figure(
        figsize=FIGURE_SIZE
    )



    positions = range(
        1,
        len(profile) + 1
    )



    # Raw residue profile

    plt.plot(
        positions,
        profile,
        alpha=0.3,
        label="Residue by residue"
    )



    # Sliding window profile

    window_positions = range(
        window_size,
        len(profile) + 1
    )


    plt.plot(
        window_positions,
        window_profile,
        linewidth=2,
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


    plt.grid(
        True
    )



    output_file = (
        FIGURES_DIR /
        "hydrophobicity_comparison.png"
    )


    plt.tight_layout()


    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()


    logger.info(
        "Hydrophobicity comparison generated: %s",
        output_file
    )



def plot_secondary_structure_fraction(structure_fraction: dict):

    """
    Generates secondary structure composition plot.
    """

    create_output_folder()


    labels = list(
        structure_fraction.keys()
    )


    values = list(
        structure_fraction.values()
    )


    plt.figure(
        figsize=FIGURE_SIZE
    )


    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )


    plt.title(
        "Predicted Secondary Structure Composition"
    )


    output_file = (
        FIGURES_DIR /
        "secondary_structure_fraction.png"
    )


    plt.tight_layout()


    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )


    plt.close()


    logger.info(
        "Secondary structure plot generated: %s",
        output_file
    )