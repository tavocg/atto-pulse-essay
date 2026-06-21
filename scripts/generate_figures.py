from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Circle, Rectangle


OUT = Path("res/figures")
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.titlesize": 13,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
})


def save(fig, name):
    fig.savefig(OUT / name, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def time_scales():
    labels = [
        "Segundo\nvida cotidiana",
        "Milisegundo\nneuronas",
        "Microsegundo\ncircuitos",
        "Nanosegundo\ntransistores",
        "Picosegundo\nvibraciones",
        "Femtosegundo\nnúcleos",
        "Attosegundo\nelectrones",
    ]
    exponents = np.array([0, -3, -6, -9, -12, -15, -18])
    colors = ["#23395B", "#406E8E", "#5A9A78", "#D9A441", "#D96C3D", "#A23E48", "#5E3C99"]

    fig, ax = plt.subplots(figsize=(8.2, 2.8))
    ax.scatter(exponents, np.zeros_like(exponents), s=230, c=colors, zorder=3)
    for x, label, color in zip(exponents, labels, colors):
        ax.vlines(x, -0.08, 0.08, color=color, lw=2)
        ax.text(x, 0.18 if x % 2 == 0 else -0.28, label, ha="center", va="center", color="#222")

    ax.hlines(0, exponents.min(), exponents.max(), color="#333", lw=1.5)
    ax.set_xlim(0.8, -18.8)
    ax.set_ylim(-0.55, 0.55)
    ax.set_xlabel("Escala temporal log10(segundos)")
    ax.set_yticks([])
    ax.set_title("La attociencia desplaza la observación hacia el tiempo natural del electrón")
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "time_scales.png")


def hhg_three_step():
    fig, ax = plt.subplots(figsize=(8.2, 3.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    nucleus = Circle((1.1, 2.0), 0.32, color="#A23E48")
    ax.add_patch(nucleus)
    ax.text(1.1, 1.42, "ion", ha="center", fontsize=10)

    steps = [
        (2.5, "1. Túnel", "el campo IR\nlibera el electrón"),
        (5.0, "2. Aceleración", "el electrón gana\nenergía en el campo"),
        (7.5, "3. Recolisión", "recombina y emite\nfotón XUV"),
    ]
    for x, title, body in steps:
        ax.add_patch(Rectangle((x - 0.95, 0.45), 1.9, 0.95, facecolor="#F4F1DE", edgecolor="#333", lw=0.8))
        ax.text(x, 1.17, title, ha="center", va="center", weight="bold", color="#222")
        ax.text(x, 0.78, body, ha="center", va="center", fontsize=9, color="#333")

    path_x = np.linspace(1.45, 8.35, 200)
    path_y = 2.0 + 0.55 * np.sin((path_x - 1.45) * np.pi / 3.45)
    ax.plot(path_x, path_y, color="#23395B", lw=2)
    ax.scatter([2.5, 5.0, 7.5], [2.55, 2.3, 1.95], s=70, color="#23395B")

    for start, end in [((1.5, 2.0), (2.25, 2.48)), ((2.8, 2.55), (4.55, 2.35)), ((5.35, 2.25), (7.15, 2.0))]:
        ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=14, lw=1.4, color="#23395B"))

    ax.add_patch(FancyArrowPatch((7.7, 2.05), (9.2, 2.75), arrowstyle="-|>", mutation_scale=18, lw=2, color="#D9A441"))
    ax.text(9.25, 2.83, "XUV", color="#8A5A00", fontsize=12, weight="bold", va="center")
    ax.text(4.95, 3.55, r"$E_c \approx I_p + 3.17U_p$", ha="center", fontsize=13)
    ax.set_title("Modelo de tres pasos de la generación de armónicos altos (HHG)")
    save(fig, "hhg_three_step.png")


def research_flow():
    labels = [
        ("1987", "Meseta de HHG\nL'Huillier"),
        ("1993-94", "Modelo de tres pasos\ny teoría cuántica"),
        ("2001", "Trenes de 250 as\nAgostini/RABBITT"),
        ("2001", "Pulso único 650 as\nKrausz/streaking"),
        ("2010-17", "Retardos de fotoemisión\ny correlación electrónica"),
        ("2020+", "Líquidos, sólidos,\nXUV y rayos X blandos"),
    ]
    fig, ax = plt.subplots(figsize=(8.2, 3.0))
    ax.set_xlim(0, len(labels) - 1)
    ax.set_ylim(-0.4, 1.4)
    ax.axis("off")
    ax.hlines(0.45, 0, len(labels) - 1, color="#333", lw=1.4)
    for i, (year, text) in enumerate(labels):
        color = "#5E3C99" if i in (2, 3) else "#406E8E"
        ax.scatter(i, 0.45, s=210, color=color, zorder=3)
        ax.text(i, 0.45, str(i + 1), ha="center", va="center", color="white", weight="bold")
        ax.text(i, 0.88, year, ha="center", va="bottom", weight="bold", color="#222")
        ax.text(i, 0.08, text, ha="center", va="top", fontsize=9, color="#222")
    ax.set_title("Hilo conductor: fuente coherente -> pulso medible -> dinámica electrónica")
    save(fig, "research_flow.png")


if __name__ == "__main__":
    time_scales()
    hhg_three_step()
    research_flow()
