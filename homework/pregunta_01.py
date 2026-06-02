"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd
import os
# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    # Lee el archivo CSV
    df = pd.read_csv("files/input/news.csv")

    os.makedirs("files/plots", exist_ok=True)

    colors = {"Television": "blue", "Internet": "green", "Radio": "red", "Newspaper": "orange"}
    zorder = {"Television": 2, "Internet": 3, "Radio": 1, "Newspaper": 1}
    linewidth = {"Television": 2, "Internet": 5, "Radio": 1, "Newspaper": 1}

    # Crear la figura y el eje
    plt.figure(figsize=(10, 6))
    plt.title("News Views Over Years")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    years = df["Unnamed: 0"]

    for col in df.columns[1:]:
        y = df[col]
        plt.plot(years,y, label=col,color=colors.get(col, "black"), zorder=zorder.get(col, 0), linewidth=linewidth.get(col, 1),)
        
        # Valor inicial
        plt.text(years.iloc[0] - 0.2, y.iloc[0], f"{col}: {y.iloc[0]}%", color=colors.get(col, "black"), fontsize=9, va="center", ha="right",)
        #Valor Final
        plt.text(years.iloc[-1] + 0.1, y.iloc[-1], f"{y.iloc[-1]}%", color=colors.get(col, "black"), fontsize=9, va="center", ha="left",)

    # Etiquetas
    plt.xlabel("Year")

    # Elementos de la gráfica
    plt.legend()
    plt.grid(True)

    # Guardar imagen
    plt.savefig("files/plots/news.png")
    plt.close()