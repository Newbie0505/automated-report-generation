def analyze_data(df):
    stats = {}
    stats['summary'] = df[['Units_Sold','Revenue','Expenses','Profit']].describe()
    stats['by_product'] = df.groupby('Product').agg(
        Total_Units=('Units_Sold','sum'),
        Total_Revenue=('Revenue','sum'),
        Total_Profit=('Profit','sum')
    ).reset_index()
    stats['monthly'] = df.groupby('Month')['Profit'].sum().reset_index()
    stats['by_region'] = df.groupby('Region')['Revenue'].sum().reset_index()
    return stats