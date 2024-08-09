import json
from typing import Tuple
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager
import numpy as np
import pandas as pd
from cycler import cycler
import matplotlib.patches as patches

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


def set_visual_style(json_color_path: str='vizman/colors.json',
                     font_family:str="Atkinson Hyperlegible",
                     change_colors:bool=True) -> None:
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
            To install them you can run `viz.add_font("vizman/fonts")`
            I chose these because they are open source and they are extremely readable.
            By default it tries to load Atkinson Hyperlegible.
            If you want to use another font you can add it to the font folder and call `add_font`.
            Honestly, adding fonts is a pain in the ass so it might not work! 
            But if that happens, it just uses its own default font.
        change_colors (bool): changes the default color cycler to something less ugly!
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
            "axes.linewidth": 1,
            "axes.titlepad": 4,
            "lines.linewidth": 1,
            "legend.fontsize": 8,
            "legend.title_fontsize": 10,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "xtick.major.size": 2,
            "xtick.major.pad": 1,
            "xtick.major.width": 1,
            "ytick.major.size": 2,
            "ytick.major.pad": 1,
            "ytick.major.width": 1,
            "xtick.minor.size": 2,
            "xtick.minor.pad": 1,
            "xtick.minor.width": 1,
            "ytick.minor.size": 2,
            "ytick.minor.pad": 1,
            "ytick.minor.width": 1,
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
    if change_colors:
        cycling_colors = [colors["neutrals"]["OLIVE_GRAY"],
                        colors["colds"]["LAKE_BLUE"],
                        colors["warms"]["ORANGE"],
                        colors["purples"]["PURPLE"],
                        colors["greens"]["SLOW_GREEN"],
                        colors["neutrals"]["HALF_BLACK"],
                        colors["colds"]["INK_BLUE"],
                        colors["warms"]["LECKER_RED"],
                        colors["purples"]["PINK"],
                        colors["greens"]["LUXUARY_GREEN"],
                        colors["neutrals"]["GRAY"],
                        colors["colds"]["TEAL"],
                        colors["warms"]["YELLOW"],
                        colors["purples"]["PURPLER"],]
        matplotlib.rcParams["axes.prop_cycle"]= cycler(color=cycling_colors)



def give_colormaps(json_color_path: str='vizman/colors.json') -> dict:
    colors = load_data_from_json(json_color_path)

    colormaps = {
        "db_bw_lr":sns.blend_palette([colors["colds"]["DEEP_BLUE"],
                                      colors["neutrals"]["BONE_WHITE"],
                                      colors["warms"]["LECKER_RED"]],
                                     as_cmap=True),
        "nb_bw_dr":sns.blend_palette([colors["colds"]["NIGHT_BLUE"],
                                      colors["neutrals"]["BONE_WHITE"],
                                      colors["warms"]["DEEP_RED"]],
                                     as_cmap=True),
        "sg_bw_pi":sns.blend_palette([colors["greens"]["SLOW_GREEN"],
                                      colors["neutrals"]["BONE_WHITE"],
                                      colors["purples"]["PINK"]],
                                     as_cmap=True),
        "bw_lr":sns.blend_palette([colors["neutrals"]["BONE_WHITE"],
                                   colors["warms"]["LECKER_RED"]],
                                  as_cmap=True),
        "bw_db":sns.blend_palette([colors["neutrals"]["BONE_WHITE"],
                                   colors["colds"]["DEEP_BLUE"]],
                                  as_cmap=True),
        "bw_hb":sns.blend_palette([colors["neutrals"]["BONE_WHITE"],
                                   colors["neutrals"]["HALF_BLACK"]],
                                  as_cmap=True),
        }
    return colormaps

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


def plot_matrix(adjmat:np.ndarray|pd.DataFrame,
                cbar:bool=False,
                community_labels:np.ndarray[int]|list[int]=None,
                community_cmap:str|dict=None,
                axis:matplotlib.axes = None,
                sns_kwargs:dict=None) -> None:
    sns_kwargs = sns_kwargs or {}
    if axis is None:
        axis = plt.figure().add_axes([0,0,1,1])
    
    if np.any(adjmat<0):
        sns.heatmap(adjmat, ax=axis, center = 0, cbar=False, square=True,**sns_kwargs)
    else:
        sns.heatmap(adjmat, ax=axis, cbar=False, square=True,**sns_kwargs)
    
    pos = axis.get_position()
    height = pos.height
    width = pos.width
    left = pos.x0 + pos.width + 0.03
    bottom = pos.y0
    
    if cbar:
        cax = plt.gcf().add_axes([left, bottom, 0.03, height])
        plt.colorbar(axis.collections[0], cax=cax)
    
    if community_labels:
        comm_ax = plt.gcf().add_axes([pos.x0, pos.y0 + height + 0.02, width, 0.05])
        
        community_labels = np.array(community_labels).reshape(1, -1)
        if community_cmap:
            sns.heatmap(community_labels, ax=comm_ax, cmap=community_cmap,
                        cbar=False, xticklabels=False, yticklabels=False, square=False)
        unique_labels = np.unique(community_labels)
        for label in unique_labels:
            indices = np.where(community_labels[0] == label)[0]
            start = indices[0]
            end = indices[-1] + 1
            rect = patches.Rectangle((start, 0), end - start, 1, edgecolor='black', facecolor='none')
            comm_ax.add_patch(rect)
        for label in unique_labels:
            indices = np.where(community_labels[0] == label)[0]
            start = indices[0]
            end = indices[-1] + 1
            rect = patches.Rectangle((start, start), end - start, end - start, edgecolor='black', facecolor='none')
            axis.add_patch(rect)
    sns.despine(top=False, right=False, left=False, bottom=False)
    return axis

def plot_eigenspectrum(adjmat:np.ndarray|pd.DataFrame,
                       axis:matplotlib.axes=None,
                       spectral_radius_color:str|dict='black',
                       unit_circle:bool=False,
                       sns_kwargs:dict=None) -> None:
    sns_kwargs = sns_kwargs or {}
    if axis is None:
        axis = plt.figure().add_axes([0,0,1,1])
    
    if isinstance(adjmat, pd.DataFrame):
        adjmat = adjmat.to_numpy()
    
    eigenvalues = np.linalg.eigvals(adjmat)
    spectral_radius_index = np.argmax(np.abs(eigenvalues))
    spectral_radius_value = eigenvalues[spectral_radius_index]
    
    sns.scatterplot(x=eigenvalues.real, y=eigenvalues.imag, ax=axis, **sns_kwargs)
    axis.scatter(spectral_radius_value.real, spectral_radius_value.imag, color=spectral_radius_color, marker = "X")
    if unit_circle:
        circle = patches.Circle((0,0),radius=1, edgecolor=spectral_radius_color, facecolor='none')
        axis.add_patch(circle)
    axis.set_aspect('equal', adjustable='box')

    plt.axvline(0, c="black", lw=1)
    plt.axhline(0, c="black", lw=1)
    sns.despine(top=False, right=False, left=False, bottom=False)
    return axis