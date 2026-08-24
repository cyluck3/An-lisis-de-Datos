import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(42)
size = 1000
my_dataset = {
    "type": np.random.choice(["Human", "Zombie"], p=[0.40, 0.60], size=size),
    "age": np.random.randint(18, 80, size=size), 
    "sex": np.random.choice(["Male", "Female"], p=[0.60, 0.40], size=size),
    "health": np.random.randint(5,100, size=size)
}


df = pd.DataFrame(my_dataset)

# Configurar estilo global para todo el gráfico
plt.style.use('fivethirtyeight')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11          # Tamaño base para etiquetas y ticks
plt.rcParams['axes.titlesize'] = 14     # Tamaño para los títulos de cada subgráfico

# Paletas de color elegantes
COLORS_GENDER = ["#2b5c8f", "#d95f87"]  # Azul elegante y Rosa sobrio
COLORS_ZH = ["#2A6F97", "#BC4749"]  # Otro Azul elegante y Naranja elegante para la distribucion humanos / zombies
COLORS_SPECIES = ["#34495e", "#e74c3c"] # Gris pizarra (Humanos) y Rojo apagado (Zombies)
COLORS_HEALTH = ["#1B2A4A", "#D97736"] # (Azul Marino Profundo) y (Cobre Cálido)


figure, axes = plt.subplots(2, 2, figsize=(9, 6))

# Sex   
male = df[df.sex == "Male"]["sex"].count()
female = df[df.sex == "Female"]["sex"].count()

wedges1, texts, autotexts = axes[0,0].pie([male, female], colors=COLORS_GENDER, autopct="%1.1f%%", pctdistance=0.75, wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))
axes[0,0].legend(wedges1, [f"Male:{male}", f"Female:{female}"], title="Gender", loc="upper left", bbox_to_anchor=(1,1))
axes[0,0].set_title("Gender Distribution", fontname="serif")

# Human / Zombie

humans = df[df["type"] == "Human"]["type"].count()
zombies = df[df["type"] == "Zombie"]["type"].count()

wedges2, texts, autotexts, = axes[0,1].pie([humans, zombies], colors=COLORS_ZH, autopct="%1.1f%%", pctdistance=0.75, wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))
axes[0,1].legend(wedges2, [f"Humans:{humans}", f"Zombies:{zombies}"], title="Distribution", loc="upper left", bbox_to_anchor=(1,1))
axes[0,1].set_title("Human / Zombie Distribution", fontname="serif")

# Ages

wedges3, texts, autotexts = axes[1,0].hist([df[df["type"] == "Human"]["age"], df[df["type"] == "Zombie"]["age"]], bins=range(18, 80, 10), color=COLORS_SPECIES)
axes[1,0].legend(wedges3, labels=[f"Humans", f"Zombies"], title="Ages", loc="upper left", bbox_to_anchor=(1, 1))
axes[1,0].set_title(f"Ages Distribution", fontname="serif")
axes[1,0].spines['top'].set_visible(False)
axes[1,0].spines['right'].set_visible(False)
axes[1,0].grid(axis='y', linestyle='--', alpha=0.5) 

# Health

wedges4, texts, autotexts = axes[1,1].hist([df[df["type"]=="Human"]["health"], df[df["type"]=="Zombie"]["health"]], bins=range(5, 100, 10), color=COLORS_HEALTH)
axes[1,1].legend(wedges4, labels=[f"Humans", f"Zombies"], title="Health", loc="upper left", bbox_to_anchor=(1, 1))
axes[1,1].set_title(f"Health Distribution", fontname="serif")
axes[1,1].spines['top'].set_visible(False)
axes[1,1].spines['right'].set_visible(False)
axes[1,1].grid(axis='y', linestyle='--', alpha=0.5)

figure.suptitle("Zombies / Humans (In Videogame)", fontsize=18, fontweight="normal", fontname="serif")
plt.subplots_adjust(wspace=0.4, hspace=0.3)
plt.tight_layout(rect=(0, 0, 1,1))
plt.show()