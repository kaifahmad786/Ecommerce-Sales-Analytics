print(df.columns.tolist())
category_analysis = df.groupby('Category')[['Total_Sales', 'Profit']].sum()

category_analysis.plot(kind='bar', figsize=(9, 6))

plt.title('Sales vs Profit by Category')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.xticks(rotation=0)
plt.legend(['Sales', 'Profit'])

plt.tight_layout()
plt.show()