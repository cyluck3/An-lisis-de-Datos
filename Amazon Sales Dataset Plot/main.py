import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("kaggle/amazon sales/amazon.csv")

df = pd.DataFrame(dataset)
df = df.sample(frac=0.1, random_state=42, ignore_index=True)

# ['product_id', 'product_name', 'category', 'discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count','about_product', 'user_id', 'user_name', 'review_id', 'review_title','review_content', 'img_link', 'product_link']

df = df.drop(columns=["product_id", "product_name", "category", "discounted_price", "rating_count", "about_product", "user_id", "user_name", "review_id", "review_title", "review_content", "img_link", "product_link"])

rating = df["rating"]
price = df["actual_price"].str.replace('₹', '').str.replace(',', '').astype(float)
discount = df['discount_percentage'].str.replace('%', '').astype(float)

figure, axes = plt.subplots(2, 2, figsize=(7,4))
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11          # Tamaño base para etiquetas y ticks
plt.rcParams['axes.titlesize'] = 14     # Tamaño para los títulos de cada subgráfico

# Price

axes[0,0].hist(
    [price], 
    bins=range(0,int(price.max())+10,15000), 
    color=["#1A2530"],
    rwidth=0.85)
axes[0,0].spines['top'].set_visible(False)
axes[0,0].spines['right'].set_visible(False)
axes[0,0].grid(axis='y', linestyle='--', alpha=0.5)
axes[0,0].set_title("Prices", fontname="serif")
axes[0,0].set_xlabel("Price (USD)", fontname="serif")
axes[0,0].set_ylabel("N Products", fontname="serif")

axes[0,0].axhline(
    y= discount.max(),
    color="#C5A059",
    linestyle="--",
    linewidth=2,
    label="Max Discount",
)

axes[0,0].axhline(
    y= discount.min(),
    color="#C5A059",
    linestyle=":",
    linewidth=2,
    label="Min Discount",
)

axes[0,0].legend()
# Discounts 

axes[0,1].hist(
    [discount], 
    bins=range(0,int(discount.max())+10,10), 
    color=["#1A2530"], 
    rwidth=0.85)
axes[0,1].spines['top'].set_visible(False)
axes[0,1].spines['right'].set_visible(False)
axes[0,1].grid(axis='y', linestyle='--', alpha=0.5)
axes[0,1].set_title("Discounts", fontname="serif")
axes[0,1].set_xlabel("- N%", fontname="serif")
axes[0,1].set_ylabel("N Products", fontname="serif")
counts, bin_edges = np.histogram(discount, bins=range(0,int(discount.max())+10,10))  
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])  # Centro de cada barra

# Dibujar la línea de tendencia sobre los centros de las barras
axes[0, 1].plot(
    bin_centers,
    counts,
    color="#C5A059",
    linestyle="--",
    marker="o",
    linewidth=2,
    label="Trend",
)
axes[0,1].legend()

# Rating

rating = pd.to_numeric(rating, errors='coerce')
df['is_positive'] = (rating >= 4.0).astype(int)
is_positive = df["is_positive"].value_counts().sort_index()

axes[1,0].barh(["Negative", "Positive"], is_positive, color=["#8C4336", "#1B3B2B"])
axes[1,0].spines['top'].set_visible(False)
axes[1,0].spines['right'].set_visible(False)
axes[1,0].grid(axis='y', linestyle='--', alpha=0.5)
axes[1,0].set_title("Rating", fontname="serif")
axes[1,0].set_xlabel("Votes", fontname="serif")
axes[1,0].set_ylabel("N Products", fontname="serif")

# Prices + Discounts applied

dis = discount / 100
num_to_rest = price * dis
final_price = price - num_to_rest
final_price = final_price.sort_values()

axes[1,1].hist(final_price, bins=range(0,int(final_price.max()+10000), 10000), color="#1B2A4A", rwidth=0.85)
axes[1,1].set_title("Prices + Discounts", fontname="serif")
axes[1,1].spines['top'].set_visible(False)
axes[1,1].spines['right'].set_visible(False)
axes[1,1].grid(axis='y', linestyle='--', alpha=0.5)
axes[1,1].set_xlabel("Final Price (USD)", fontname="serif")
axes[1,1].set_ylabel("N Products", fontname="serif")

counts, bin_edges = np.histogram(final_price, bins=range(0,int(final_price.max()+10000), 10000))  
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])  # Centro de cada barra

# Dibujar la línea de tendencia sobre los centros de las barras
axes[1, 1].plot(
    bin_centers,
    counts,
    color="#C5A059",
    linestyle="--",
    marker="o",
    linewidth=2,
    label="Trend",
)
axes[1, 1].fill_between(bin_centers, counts, color="#C5A059", alpha=0.15)
axes[1,1].legend()

figure.suptitle("Amazon Prices (Sample: 146 products)", fontsize=18, fontweight="normal", fontname="serif")
plt.subplots_adjust(wspace=0.4, hspace=0.3)
plt.tight_layout(rect=(0, 0, 0.5, 0.5))
plt.show()