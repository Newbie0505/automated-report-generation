from src.data_loader import load_data
from src.analyzer import analyze_data
from src.chart_gen import generate_charts
from src.report_gen import generate_report

def main():
    print('Step 1: Loading data...')
    df = load_data('data/sales_data.csv')

    print('Step 2: Analysing data...')
    stats = analyze_data(df)

    print('Step 3: Generating charts...')
    chart_paths = generate_charts(df)

    print('Step 4: Creating PDF report...')
    generate_report(df, stats, chart_paths, 'output/final_report.pdf')

    print('Done! Open output/final_report.pdf')

if __name__ == '__main__':
    main()