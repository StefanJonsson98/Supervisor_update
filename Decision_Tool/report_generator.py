import os
import textwrap
import reportlab
from collections import defaultdict
from datetime import datetime
import numpy as np
import data
import pandas as pd
from io import BytesIO
import matplotlib.pyplot as plt
from reportlab.graphics import renderPDF, renderPM
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors
from tempfile import NamedTemporaryFile
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                 Table, TableStyle, PageBreak, Frame,
                                 NextPageTemplate, PageTemplate, Flowable)
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import utils
from data import example_startup_data

class FooterCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_footer(page_count)
            self.draw_header("Valuation Report: " + example_startup_data['company_info']["company_name"])
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_footer(self, page_count):
        page = "Page %s of %s" % (self._pageNumber, page_count)
        x = 128
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.line(66, 78, LETTER[0] - 66, 78)
        self.setFont('Times-Roman', 10)
        self.drawString(LETTER[0]-x, 65, page)
        self.restoreState()
        
    def draw_header(self, title):
        self.saveState()
        self.setStrokeColorRGB(0, 0, 0)
        self.setLineWidth(0.5)
        self.line(66, 760, LETTER[0] - 66, 760)
        self.setFont('Times-Roman', 10)
        self.drawString(66, 770, title)
        self.restoreState()

class Startup_report_generator:
    def __init__(self, startup_data, sections=None):
        self.startup_data = startup_data
        self.styles = self.create_styles()
        self.sections = sections if sections is not None else startup_data.keys()
        self.canvas = canvas.Canvas("report.pdf")

    def create_styles(self):
        styles = getSampleStyleSheet()
        # Big title
        styles.add(ParagraphStyle(name='TitleBig', parent=styles['Normal'], fontSize=24, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='TitleCenter', parent=styles['Title'], alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='Subtitle', parent=styles['Normal'], fontSize=14, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name = 'TableCellHeader', parent = styles['Normal'], fontSize = 10, alignment = TA_CENTER))
        # TextBoxRight style
        styles.add(ParagraphStyle(name='TextBoxRight',
                                parent=styles['Normal'],
                                fontSize=8,
                                leading=14,
                                border=1,
                                borderColor=colors.black,
                                borderRadius=5,
                                padding=10,
                                spaceAfter=2,
                                alignment=TA_RIGHT,
                                width=0.7*inch,
                                wordWrap=None))
        
        # TextBoxRightIndent style, this is the same as TextBoxRight but padding before each paragraph and
        # justified text, The padding is needed to make the text look better when it is wrapped
        styles.add(ParagraphStyle(name='TextBoxRightIndent',
                                parent=styles['Normal'],
                                fontSize=8,
                                leading=14,
                                border=1,
                                borderColor=colors.black,
                                borderRadius=5,
                                padding=10,
                                spaceAfter=2,
                                # Right indent half of the width of the page (letter size is 8.5 inches)
                                leftIndent = 4.25*inch,
                                alignment=TA_JUSTIFY,
                                width=0.7*inch,
                                wordWrap=None))
        
        # TextBoxLeft style
        styles.add(ParagraphStyle(name='TextBoxLeft',
                                parent=styles['Normal'],
                                fontSize=8,
                                leading=14,
                                border=1,
                                borderColor=colors.black,
                                borderRadius=5,
                                padding=10,
                                spaceAfter=2,
                                alignment=TA_LEFT,
                                width=0.7*inch,
                                wordWrap=None))
        # Normal style but bold
        styles.add(ParagraphStyle(name='NormalBold', parent=styles['Normal'], fontName='Helvetica-Bold'))
        
        # Table styles
        styles.add(ParagraphStyle(name='TableHeader', parent=styles['NormalBold'], fontSize=10, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='TableData', parent=styles['Normal'], fontSize=8, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='TableDataLeft', parent=styles['Normal'], fontSize=8, alignment=TA_LEFT))
        styles.add(ParagraphStyle(name='TableDataRight', parent=styles['Normal'], fontSize=8, alignment=TA_RIGHT))
        styles.add(ParagraphStyle(name='TableDataCenter', parent=styles['Normal'], fontSize=8, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='TableDataBold', parent=styles['NormalBold'], fontSize=8, alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='TableDataBoldLeft', parent=styles['NormalBold'], fontSize=8, alignment=TA_LEFT))
        styles.add(ParagraphStyle(name='TableDataBoldRight', parent=styles['NormalBold'], fontSize=8, alignment=TA_RIGHT))
        styles.add(ParagraphStyle(name='TableDataBoldCenter', parent=styles['NormalBold'], fontSize=8, alignment=TA_CENTER))
    

        
        return styles


    def add_logo(self, elements, logo_path, width, height):
        logo = Image(logo_path, width, height)
        elements.append(logo)
        
    
    def add_image(self, path, width=1*inch):
        img = utils.ImageReader(path)
        iw, ih = img.getSize()
        aspect = ih / float(iw)
        return Image(path, width=width, height=(width * aspect))

    def create_text_box(self, text, style_name):
        style = self.styles[style_name]
        max_width = style.width

        paragraphs = []
        for line in textwrap.wrap(text, width=max_width):
            paragraph = Paragraph(line, style)
            paragraphs.append(paragraph)

        return paragraphs
    
    def create_text_box_from_dict(self, data, style_name, key_bold=False, extra_spacing=0):
        style = self.styles[style_name]
        max_width = style.width
        
        paragraphs = []
        for key, value in data.items():
            if key_bold:
                text = f"<b>{key}</b>: {value}"
            else:
                text = f"{key}: {value}"
            for line in textwrap.wrap(text, width=max_width):
                paragraph = Paragraph(line, style)
                paragraphs.append(paragraph)
                
            # Add extra spacing between paragraphs if needed
            paragraphs.append(Spacer(1, extra_spacing))
            
        return paragraphs


    #creates the cover page of the report with the company name, contact info and logo
    def create_cover_page(self, company_name, contact_info, logo_path="logo_nota.png", logo_width=337.2, logo_height=100):
        cover_page_elements = []

        cover_page_elements.append(Spacer(1, 200))
        cover_page_elements.append(Paragraph(f"Valuation Report of {company_name}", self.styles['TitleCenter']))
        cover_page_elements.append(Spacer(1, 12))
        cover_page_elements.append(Paragraph("Internal Report", self.styles['Subtitle']))
        cover_page_elements.append(Spacer(1, 12))
        
        # Add logo
        if logo_path:
            self.add_logo(cover_page_elements, logo_path, logo_width, logo_height)
            cover_page_elements.append(Spacer(1, 24))
            
        cover_page_elements.append(Spacer(1, 100))
        
        
        # Add date of generation
        today = datetime.today().strftime('%Y-%m-%d')
        cover_page_elements.append(Paragraph(f"Date of Generation: {today}", self.styles['Normal']))
        cover_page_elements.append(Spacer(1, 50))
        # Add summary
        text = "This report is intended for internal use only. It contains the results of our analysis of the investment opportunity presented by {}.".format(company_name)
        text_box = self.create_text_box(text, 'TextBoxLeft')
        for paragraph in text_box: cover_page_elements.append(paragraph)
    
        negative_spacer = Spacer(1, -50)
        cover_page_elements.append(negative_spacer)

        # Add contact info at the bottom right
        text_box = self.create_text_box_from_dict(contact_info, 'TextBoxRight')
        for paragraph in text_box: cover_page_elements.append(paragraph)


        # Add page break to start new page
        cover_page_elements.append(PageBreak())

        return cover_page_elements
    


    #creates the table of contents page
    def create_table_of_contents(self, sections):
        toc_elements = []

        toc_elements.append(Paragraph("Table of Contents", self.styles['Heading2']))
        toc_elements.append(Spacer(1, 12))

        for index, section in enumerate(sections, start=1):
            toc_elements.append(Paragraph(f"{index}. {section.capitalize()}", self.styles['Heading3']))
            toc_elements.append(Spacer(1, 6))

        toc_elements.append(PageBreak())

        return toc_elements

    

    #creates the executive summary page
    def create_company_summary(self, company_name):
        # Title 
        elements = []
        elements.append(Paragraph("Company Summary", self.styles['TitleBig']))
        # Company name
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(company_name, self.styles['Heading3']))
        
        # Overview of the industry, left aligned
        elements.append(Spacer(1, 12))
        
        industry_and_overview = {
            'Industry': self.startup_data['company_info']['industry'],
            'Business Activities': self.startup_data['company_info']['business_activities'],
            'Business Model': self.startup_data['company_info']['business_model'],
            'Mission Statement': self.startup_data['company_info']['mission_statement']
        }
        
        textbox_left = self.create_text_box_from_dict(industry_and_overview, 'TextBoxLeft', key_bold=True, extra_spacing=12)
    
        
        for paragraph in textbox_left: 
            elements.append(paragraph)
            
        
        
        # Company info, right aligned
        elements.append(Spacer(1, 12))
        
        company_info = {
            'Address': self.startup_data['company_info']['headquarters'],
            'Year Founded': self.startup_data['company_info']['founded'],
            'Number of Employees': self.startup_data['staff_information']['number_of_employees'],
            'Number of Full-Time Employees': self.startup_data['staff_information']['number_of_employees_excluding_founders_interns_freelancers'],
            'website': self.startup_data['company_info']['website']
        }
        elements.append(Spacer(1, -350))
        
        textbox_right = self.create_text_box_from_dict(company_info, 'TextBoxRightIndent', key_bold=True, extra_spacing=12)
        total_height = 0
        for paragraph in textbox_right: 
            elements.append(paragraph)
            # Font size + line spacing
            total_height += 7 + 12
        
        # Add in posative spacer to move the text box down
        elements.append(Spacer(1, 350 - total_height))
        
        
        # Page break
        elements.append(PageBreak())
        return elements
    

    ######################################### - - - - All visulaizations are created here - - - - #########################################
    ######################################### - - - - - - Used Later in the program  - - - - - -  #########################################
    #financial forecasts 


    def create_forecasts_summary(self, filename):
        # Get the FCF projections from the JSON file
        fcf_projections = {'m.ISK': [2020, 2021, 2022, 2023, 2024, 2025, 2026],
                        'EBIT(1-t)': [-4.39, -10.82, -8.64, 29.21, 82.52, 160.62, 240.00],
                        'Reinvestment': ['-', 24.09, 74.09, 71.46, 51.49, 94.00, 33.67],
                        'Free Cash Flow': [-4.39, -34.91, -82.73, -42.25, 31.03, 66.62, 206.33]}

        # Replace '-' with NaN
        fcf_projections = {k: [np.nan if x == '-' else x for x in v] for k, v in fcf_projections.items()}

        # Create a pandas DataFrame to hold the data for each row in the table
        df = pd.DataFrame(fcf_projections, columns=['m.ISK', 'EBIT(1-t)', 'Reinvestment', 'Free Cash Flow'])
        df['m.ISK'] = pd.to_datetime(df['m.ISK'], format='%Y').dt.year.astype(str)

        # Create a table to hold the data
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.axis('off')
        ax.axis('tight')
        table = ax.table(cellText=df.values, colLabels=['m.ISK', 'EBIT(1-t)', 'Reinvestment', 'Free Cash Flow'], loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1, 2)
        plt.tight_layout()
        plt.savefig(filename, bbox_inches='tight')
        plt.close(fig)

        #past funding rounds
    def generate_funding_rounds(self, filename):

        # Extract data from JSON
        data = [['Date', 'Amount Raised (mISK)', 'Percentage of Equity']]
        for round in self.startup_data['past_funding_rounds']:
            date = round['date']
            amount = round['amount_raised'].replace(".", "").replace(" mISK", "")
            equity = round['percentage_of_equity']
            data.append([date, amount, equity])

        # Create the table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#CCCCCC'),  # Gray background for header row
            ('TEXTCOLOR', (0, 0), (-1, 0), '#FFFFFF'),  # White text for header row
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center align all cells
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header row
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # Font size for header row
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),  # Add padding to bottom of header row
            ('BACKGROUND', (0, 1), (-1, -1), '#F7F7F7'),  # Light gray background for data rows
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Regular font for data rows
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # Font size for data rows
            ('TOPPADDING', (0, 1), (-1, -1), 8),  # Add padding to top of data rows
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),  # Add padding to bottom of data rows
        ]))

        # Save the table as a PNG image
        table.wrapOn(self.canvas, 0, 0)
        table.drawOn(self.canvas, 0, 0)
        self.canvas.saveState()
        return

    #generate a ownership structure pie chart
    def create_pie_chart_with_ownership_structure(self, filename):

        # Create pie chart with the ownership structure of the company
        owners = [shareholder['name'] for shareholder in self.startup_data['ownership']]
        shares = [shareholder['percentage_of_equity'] for shareholder in self.startup_data['ownership']]
        
        # Define a grayscale colormap
        cmap = plt.cm.get_cmap('Greys_r', len(owners))
        colors = [cmap(i) for i in range(len(owners))]
        
        fig, ax = plt.subplots(figsize=(8, 8))
        wedges, labels = ax.pie(shares, colors=colors, startangle=90, wedgeprops={'linewidth': 1, 'edgecolor': 'white'})
        
        # Set font size for labels
        plt.setp(labels, fontsize=12)
        
        # Add percentages outside of the pie chart
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="gray", lw=1)
        kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
        percentages = ['{:.1f}%'.format(share) for share in shares]
        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            x, y = np.cos(np.deg2rad(ang)), np.sin(np.deg2rad(ang))
            xp = np.sign(x) * (1.2 + abs(x))
            ax.annotate(percentages[i], xy=(x, y), xytext=(xp, y), fontsize=12, ha="center", **kw)
        
        # Add legend
        ax.legend(wedges, owners, title='Owners', loc='center left', bbox_to_anchor=(1.5, 0.5), fontsize=18)
        
        # Add title
        ax.set_title('Ownership Structure', fontsize=16, fontweight='bold')
        plt.savefig(filename, bbox_inches='tight')



    #creates a financial projections page with prior funding rounds
    def create_financials_projections_page(self, company_name):
        #Title 
        elements = []
        elements.append(Paragraph("Financial Projections", self.styles['TitleCenter']))
        elements.append(Paragraph("Financial Projections for " + company_name, self.styles['Normal']))
        # Add the forecasts summary
        elements.append(self.create_forecasts_summary('forecast_summary.png'))
        elements.append(self.add_image('forecast_summary.png', width = 8*inch))
        elements.append(self.generate_funding_rounds('funding_rounds.png'))
        elements.append(self.add_image('funding_rounds.png', width = 8*inch))
        elements.append(PageBreak())

        return elements

    #creates a page for current ownership structure
    def create_ownership_structure_page(self, company_name):
        elements = []
        elements.append(Paragraph("Ownership Structure", self.styles['TitleCenter']))
        elements.append(Paragraph("Ownership Structure for " + company_name, self.styles['Normal']))
        # Create the ownership structure pie chart image
        self.create_pie_chart_with_ownership_structure('ownership_structure.png')
        # Add the ownership structure pie chart
        elements.append(self.add_image('ownership_structure.png', width = 8*inch))
        elements.append(PageBreak())
        return elements







    def generate_pdf_report(self, filename, company_name, contact_info):
        elements = []

        # Add the cover page
        elements.extend(self.create_cover_page(company_name, contact_info))

        # Add the table of contents
        elements.extend(self.create_table_of_contents(self.sections))

        # Add the company summary
        elements.extend(self.create_company_summary(company_name))
        
        # Add the company summary
        elements.extend(self.create_financials_projections_page(company_name))

        # Add the ownership structure
        elements.extend(self.create_ownership_structure_page(company_name))


        # Create the PDF document
        doc = SimpleDocTemplate(filename, pagesize=letter)
        doc.build(elements, canvasmaker=FooterCanvas)


# Example usage with the StartupReportGenerator class:
selected_sections = [
    'market', 
    'service', 
    'competition', 
    'financials'
]

company_name = 'PayAnalytics'

contact_info = {
    'Name': 'Stefán Jónsson',
    'Email': 'Stefanj21@ru.is',
    'Phone': '+354 790 4200'
}

report_generator = Startup_report_generator(example_startup_data, sections=selected_sections)
report_generator.generate_pdf_report('valuation_report.pdf', company_name, contact_info)


