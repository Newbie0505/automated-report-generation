import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

CHART_DIR = 'charts'
os.makedirs(CHART_DIR, exist_ok=True)
COLORS = ['#1A3A6B','#2563EB','#3B82F6','#93C5FD']

def generate_charts(df):
    paths = {}

    # Bar chart
    rev = df.groupby('Product')['Revenue'].sum()
    fig, ax = plt.subplots(figsize=(7,4))
    bars = ax.bar(rev.index, rev.values, color=COLORS[:len(rev)])
    ax.bar_label(bars, fmt='%.0f', padding=4)
    ax.set_title('Total Revenue by Product', fontweight='bold')
    ax.spines[['top','right']].set_visible(False)
    path = os.path.join(CHART_DIR, 'bar_chart.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    paths['bar'] = path

    # Line chart
    monthly = df.groupby('Month')['Profit'].sum()
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(monthly.index, monthly.values, marker='o', color='#2563EB', linewidth=2.5)
    ax.fill_between(monthly.index, monthly.values, alpha=0.15, color='#2563EB')
    ax.set_title('Monthly Profit Trend', fontweight='bold')
    ax.spines[['top','right']].set_visible(False)
    plt.xticks(rotation=45, ha='right')
    path = os.path.join(CHART_DIR, 'line_chart.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    paths['line'] = path

    # Pie chart
    region = df.groupby('Region')['Revenue'].sum()
    fig, ax = plt.subplots(figsize=(6,5))
    ax.pie(region.values, labels=region.index, autopct='%1.1f%%',
           colors=COLORS[:len(region)], wedgeprops=dict(edgecolor='white'))
    ax.set_title('Revenue by Region', fontweight='bold')
    path = os.path.join(CHART_DIR, 'pie_chart.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    paths['pie'] = path

    return paths