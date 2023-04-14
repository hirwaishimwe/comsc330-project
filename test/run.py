from group import group
from section import section
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

class run:
    #costructor
    def __init__(self, runfile):
        self.run_file = runfile

    #get the run name
    def get_name(self):
        with open(self.run_file, 'r') as file:
            name = file.readline().strip()
        return name
    
    #get the run groups
    def get_groups(self):
        with open(self.run_file, 'r') as file:
            line = file.readline()
            groups = []
            while line:
                line = file.readline().strip()
                if line != '':
                    groups.append(line)
        return groups
    
    ##processing methods

    #get the reports for the run
    def reports(self):
        report_for_all_grp = []
        for grp in self.get_groups():
            grp_ = group (grp)
            report_for_grp = []
            text = grp_.group_report()
            # Get sample styles
            styles = getSampleStyleSheet()
            paragraph = Paragraph(text, style=styles["Normal"])
            report_for_grp.append(paragraph)
            report_for_grp.append(Spacer(1, 6))
            graph_color = '#1f77b4'
            section.make_plot(grp_.get_num_each_grd(), grp_.get_name(), graph_color)
            img = Image(f"{grp_.get_name()}.png", width=300, height=200)
            img.hAlign = 'LEFT'  # Set the horizontal alignment
            report_for_grp.append(img)
            report_for_grp.append(Spacer(1, 12))
            # Add section reports
            section_reports = grp_.get_section_reports()
            report_for_grp.extend(section_reports)
            report_for_all_grp += report_for_grp
            
        text = (
            f'***************************************** END OF THE REPORT *******************************************'
        )
        paragraph = Paragraph(text, style=styles["Normal"])
        report_for_all_grp.append(paragraph)
        report_for_all_grp.append(Spacer(1, 12))
        return report_for_all_grp
    
    #function to add an intro to the ouput text
    def ouput_text(self):
        styles = getSampleStyleSheet()
        full_report = []
        groups =''
        for group in self.get_groups():
            groups += group + " . "
        intro_txt = f'''
        Run File: {self.get_name()} <br/>
        Groups in Run: {groups} <br/>
        <br/>
        '''
        paragraph = Paragraph(intro_txt, style = styles["Normal"])
        full_report.append(paragraph)
        full_report.append(Spacer(1, 12))
        return full_report + self.reports()

    #Output  
    def output(self):
        name = "Report.pdf"
        doc = SimpleDocTemplate(name, pagesize = letter)
        
        # Build the PDF with the flowables
        doc.build(self.ouput_text())

        for grp in self.get_groups():
            grp_ = group (grp)
            os.remove(f'{grp_.get_name()}.png')
            sections = grp_.get_sections()
            for i in range(0,len(sections)):
                sec = section(sections[i])
                os.remove(f'{sec.get_name()}.png')
