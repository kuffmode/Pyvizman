import json
import seaborn as sns


def load_data_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


COLOR_PATH = "colors.json"
colors = load_data_from_json(COLOR_PATH)


def set_visual_style():
    sns.set_theme(
        style="ticks",
        font_scale=0.75,
        rc={
            "font.family": "Atkinson Hyperlegible",
            "font.sans-serif": ["Atkinson-Hyperlegible"],
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
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
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
            "text.color": colors.neutrals.HALF_BLACK,
            "patch.edgecolor": colors.neutrals.HALF_BLACK,
            "patch.force_edgecolor": False,
            "hatch.color": colors.neutrals.HALF_BLACK,
            "axes.edgecolor": colors.neutrals.HALF_BLACK,
            "axes.labelcolor": colors.neutrals.HALF_BLACK,
            "xtick.color": colors.neutrals.HALF_BLACK,
            "ytick.color": colors.neutrals.HALF_BLACK,
        },
    )
