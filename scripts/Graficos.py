import matplotlib.pyplot as plt

modelos = [
    "Logistic\nRegression",
    "K-Nearest\nNeighbors",
    "Decision\nTree",
    "Random\nForest"
]

rendimiento = [0.8719, 0.8183, 0.8858, 0.8788]

# Resaltar el mejor modelo
colores = ["#5B9BD5", "#5B9BD5", "#70AD47", "#5B9BD5"]

plt.figure(figsize=(8,5))

barras = plt.bar(modelos, rendimiento, color=colores)

for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width()/2,
        altura + 0.003,
        f"{altura:.4f}",
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

plt.title("Comparación del rendimiento de los modelos de clasificación", fontsize=14, fontweight="bold")
plt.xlabel("Modelos evaluados")
plt.ylabel("Accuracy")
plt.ylim(0.75, 0.92)
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("comparacion_modelos.png", dpi=300)
plt.show()