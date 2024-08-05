import json
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Tuple
from matplotlib import font_manager


def load_data_from_json(file_path: str) -> dict:
    """Just loads colors (and other data) from a json file.

    Args:
        file_path (str): location of the json file.

    Returns:
        dict: stuff in the json file as a dictionary.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def add_font(font_path: str) -> None:
    """Adds a font family to the matplotlib font manager. If you only have one font then it just adds that one.

    Args:
        font_path (str): location of the font folder (the whole typeface).
    """
    for font in font_manager.findSystemFonts(font_path):
        font_manager.fontManager.addfont(font)

def set_visual_style(json_color_path: str='Pyvizman/vizman/colors.json',
                     font_family:str="Atkinson Hyperlegible") -> None:
    """Sets the visual style for the plots. 
    This is basically my taste so feel free to change things (the fonts, e.g.) to your liking.
    But the idea is that the fonts are compatible with some other applications in case you want to edit the pdf file later.
    The black is not pure black but a "better" black for print.
    And some paddings and sizes are adjusted to make the plots look better.
    Args:
        json_color_path (str): location of the colors.json file to get the black from it.
        font_family (str): font family to use.
            Note: at the moment there are three font families with the package that you have to install yourself:
            - Atkinson Hyperlegible
            - IBM Plex Mono
            - Space Mono
            To install them you can run `viz.add_font("Pyvizman/vizman/fonts")`
            I chose these because they are open source and they are extremely readable.
            By default it tries to load Atkinson Hyperlegible.
            If you want to use another font you can add it to the font folder and call `add_font`.
            Honestly, adding fonts is a pain in the ass so it might not work! But if that happens, it just uses its own default font.
    """
    colors = load_data_from_json(json_color_path)
    sns.set_theme(
        style="ticks",
        font_scale=1,
        rc={
            "font.family": font_family,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "font.size": 10,
            "axes.labelsize": 10,
            "axes.titlesize": 10,
            "axes.labelpad": 2,
            "axes.linewidth": 0.5,
            "axes.titlepad": 4,
            "lines.linewidth": 1,
            "legend.fontsize": 8,
            "legend.title_fontsize": 10,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "xtick.major.size": 2,
            "xtick.major.pad": 1,
            "xtick.major.width": 0.5,
            "ytick.major.size": 2,
            "ytick.major.pad": 1,
            "ytick.major.width": 0.5,
            "xtick.minor.size": 2,
            "xtick.minor.pad": 1,
            "xtick.minor.width": 0.5,
            "ytick.minor.size": 2,
            "ytick.minor.pad": 1,
            "ytick.minor.width": 0.5,
            "text.color": colors['neutrals']['HALF_BLACK'],
            "patch.edgecolor": colors['neutrals']['HALF_BLACK'],
            "patch.force_edgecolor": False,
            "hatch.color": colors['neutrals']['HALF_BLACK'],
            "axes.edgecolor": colors['neutrals']['HALF_BLACK'],
            "axes.labelcolor": colors['neutrals']['HALF_BLACK'],
            "xtick.color": colors['neutrals']['HALF_BLACK'],
            "ytick.color": colors['neutrals']['HALF_BLACK'],
        },
    )



def inch_to_cm(figure_size_in_inch: Tuple[float, float]) -> Tuple[float, float]:
    """Converts figure size from inches to centimeters.

    Args:
        figure_size_in_inch: Tuple[float, float]: figure size in inches (x,y).

    Returns:
        float: Tuple[float, float]. figure size in centimeters (x,y).
    """
    return tuple(map(lambda x: x * 2.54, figure_size_in_inch))


def cm_to_inch(figure_size_in_cm: Tuple[float, float]) -> Tuple[float, float]:
    """Converts figure size from centimeters to inches.

    Args:
        figure_size_in_cm: Tuple[float, float]: figure size in centimeters (x,y).

    Returns:
        float: Tuple[float, float]. figure size in inches (x,y).
    """
    return tuple(map(lambda x: x / 2.54, figure_size_in_cm))