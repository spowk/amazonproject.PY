{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3298441c-7138-435b-82c3-71e5ec18d2c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import geopandas as gpd\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv(\"Amazon Sale Report.csv\")\n",
    "\n",
    "# Convert Date column to datetime format\n",
    "df[\"Date\"] = pd.to_datetime(df[\"Date\"], format=\"%m-%d-%y\")\n",
    "\n",
    "# Calculate Profit if cost and revenue data are available\n",
    "df[\"Profit\"] = df[\"Selling Price\"] - df[\"Cost Price\"]\n",
    "\n",
    "# Group by SKU and sum the profit\n",
    "top_profitable_products = df.groupby(\"SKU\")[\"Profit\"].sum().reset_index()\n",
    "\n",
    "# Sort by profit in descending order\n",
    "top_profitable_products = top_profitable_products.sort_values(by=\"Profit\", ascending=False).head(10)\n",
    "\n",
    "# Visualization of top profitable products\n",
    "plt.figure(figsize=(12, 6))\n",
    "sns.barplot(x=\"Profit\", y=\"SKU\", data=top_profitable_products, palette=\"Blues_r\")\n",
    "plt.xlabel(\"Total Profit\")\n",
    "plt.ylabel(\"Product SKU\")\n",
    "plt.title(\"Top 10 Most Profitable Products\")\n",
    "plt.show()\n",
    "\n",
    "# Geographic Analysis: Sales by Country in Europe\n",
    "country_sales = df.groupby(\"ship-country\")[\"Qty\"].sum().reset_index()\n",
    "country_sales = country_sales.sort_values(by=\"Qty\", ascending=False)\n",
    "\n",
    "# Load a map of Europe\n",
    "europe_map = gpd.read_file(gpd.datasets.get_path(\"naturalearth_lowres\"))\n",
    "europe_map = europe_map[europe_map[\"continent\"] == \"Europe\"]\n",
    "\n",
    "# Merge sales data with geographic data\n",
    "europe_map = europe_map.merge(country_sales, left_on=\"iso_a3\", right_on=\"ship-country\", how=\"left\")\n",
    "\n",
    "# Plot the map\n",
    "fig, ax = plt.subplots(1, 1, figsize=(12, 8))\n",
    "europe_map.plot(column=\"Qty\", cmap=\"OrRd\", linewidth=0.8, edgecolor=\"black\", legend=True, ax=ax)\n",
    "plt.title(\"Sales Distribution Across Europe\")\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
