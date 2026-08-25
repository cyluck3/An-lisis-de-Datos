# Amazon Products Exploratory Data Analysis (EDA)

A Python-based data analysis and visualization pipeline that explores product pricing, discount distributions, sentiment ratings, and final post-discount prices from the Kaggle Amazon Sales dataset.

---

## 📌 Project Overview

This project analyzes a representative sample of Amazon product listings to uncover patterns in catalog pricing strategies and customer feedback. Using `pandas` for data preprocessing and cleaning, and `matplotlib` combined with `numpy` for visual Analytics, the script processes raw currency and rating metrics into an intuitive 2x2 visual grid dashboard.

### Key Insights & Metrics Visualized
1. **Price Distribution (`Prices`)**: Histogram of raw catalog prices with threshold indicators for maximum and minimum discount percentages.
2. **Discount Distribution (`Discounts`)**: Frequency analysis of discount percentages with an overlaid trend curve across percentage bins.
3. **Rating Sentiment Breakdown (`Rating`)**: Horizontal bar plot categorizing products into positive ($\ge 4.0$) vs. negative ($< 4.0$) user sentiment.
4. **Final Price Impact (`Prices + Discounts`)**: Post-discount price distribution showing effective consumer prices along with a filled trend envelope.

---

## 🚀 Features

- **Automated Data Cleaning**:
  - Currency symbol stripping (e.g., converting `₹` strings into standard floating-point numerical values).
  - Clean parsing of percentage formatting strings.
  - Robust handling of non-numeric rating values using coerced coercion logic.
- **Representative Sampling**: Uses reproducible random sampling (`frac=0.1`, `random_state=42`) to standardise dataset exploratory execution.
- **Custom Aesthetic Visualization**:
  - Uses explicit visual styling (Serif font family, custom hex color palettes such as `#1A2530`, `#C5A059`, `#8C4336`, `#1B3B2B`).
  - Custom binning logic for high clarity across varied dynamic ranges.
  - Clean graph design with hidden top/right spines and light grid lines.

---

## 🛠️ Tech Stack & Requirements

- **Python**: 3.8+
- **Pandas**: Data manipulation and DataFrame filtering.
- **NumPy**: Histogram bin calculations and trendline point computations.
- **Matplotlib**: Subplot visualization layout and styling.

### Installation

Clone the repository and install dependencies:

```bash
pip install pandas numpy matplotlib
```

---

## 📊 Dataset Setup

The script expects the Kaggle Amazon Sales dataset structure located at:

```
kaggle/
└── amazon sales/
    └── amazon.csv
```

### Raw Dataset Columns Handled:
- `actual_price`: Raw price values formatted as strings with currency markers.
- `discount_percentage`: Discount values with `%` markers.
- `rating`: Customer rating scores.
- Additional non-analytical metadata columns (`product_id`, `product_name`, `about_product`, `user_id`, etc.) are dropped automatically during execution.

---

## ⚙️ How to Run

Simply execute the main Python script:

```bash
python main.py
```

---

## 📈 Dashboard Preview Logic

The generated plot features four key panels arranged as follows:

| Subplot | Analysis Type | Key Highlight / Feature |
| :--- | :--- | :--- |
| **Top-Left** | Catalog Prices | Max & Min discount reference horizontal lines |
| **Top-Right** | Discount % | Binned counts with dashed trendline overlay |
| **Bottom-Left** | Sentiment Binary | Positive ($\ge 4.0$) vs Negative ($< 4.0$) votes |
| **Bottom-Right** | Effective Prices | Final post-discount distribution with area fill trend |

![Data Visualization]("amazon_sales.png).

---



## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.