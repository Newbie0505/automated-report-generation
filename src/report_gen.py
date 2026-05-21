from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
import os

def generate_report(df, stats, chart_paths, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            topMargin=2*cm, bottomMargin=2*cm,
                            leftMargin=2.2*cm, rightMargin=2.2*cm)
    styles = getSampleStyleSheet()
    h1 = ParagraphStyle('h1', fontSize=18, textColor=colors.HexColor('#1A3A6B'),
                         spaceAfter=10, fontName='Helvetica-Bold')
    h2 = ParagraphStyle('h2', fontSize=13, textColor=colors.HexColor('#2563EB'),
                         spaceAfter=6, fontName='Helvetica-Bold')
    story = []

    story.append(Paragraph('Automated Report Generation Using Python', h1))
    story.append(Paragraph('Internship Project — Data Analysis Report', h2))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph('Data Summary', h2))
    table_data = [['Metric','Units Sold','Revenue','Profit']]
    for metric in ['mean','min','max','std']:
        row = [metric.capitalize(),
               f"{stats['summary'].loc[metric,'Units_Sold']:,.0f}",
               f"Rs {stats['summary'].loc[metric,'Revenue']:,.0f}",
               f"Rs {stats['summary'].loc[metric,'Profit']:,.0f}"]
        table_data.append(row)

    tbl = Table(table_data, colWidths=[3.5*cm,3.5*cm,5*cm,5*cm])
    tbl.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1A3A6B')),
        ('TEXTCOLOR',(0,0),(-1,0),colors.white),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#DBEAFE'),colors.white]),
        ('GRID',(0,0),(-1,-1),0.5,colors.lightgrey),
        ('FONTSIZE',(0,0),(-1,-1),10),
        ('TOPPADDING',(0,0),(-1,-1),6),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 0.5*cm))

    for label, key in [('Revenue by Product','bar'),
                        ('Monthly Profit Trend','line'),
                        ('Revenue by Region','pie')]:
        if key in chart_paths:
            story.append(Paragraph(label, h2))
            story.append(Image(chart_paths[key], width=14*cm, height=8*cm))
            story.append(Spacer(1, 0.3*cm))

    doc.build(story)
    print(f'PDF saved: {output_path}')