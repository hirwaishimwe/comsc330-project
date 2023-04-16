from group import group
from section import section
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from typing import List

class run:
    """
    A class to represent a collection of groups and generate a report on their performance.

    Attributes
    ----------
    run_file : str
        The name of the file containing information about the groups in the run.

    Methods
    -------
    get_name() -> str:
        Returns the name of the run.

    get_groups() -> List[str]:
        Returns a list of the names of the groups in the run.

    reports() -> List[Paragraph]:
        Generates a report on the performance of the groups in the run.

    ouput_text() -> List[Paragraph]:
        Generates the introductory text for the report.

    output() -> None:
        Generates a PDF report on the performance of the groups in the run and saves it to disk.
    """
    
    def __init__(self, runfile: str) -> None:
        """
        Constructor for the run class.
        
        :param runfile: (str) the name of the file containing the run data.
        """
        self.run_file: str = runfile

    def get_name(self) -> str:
        """
        Get the name of the run from the run file.
        
        :return: (str) the name of the run.
        """
        with open(self.run_file, 'r') as file:
            name = file.readline().strip()
        return name
    
    def get_groups(self) -> List[str]:
        """
        Get a list of the group names in the run file.
        
        :return: (List[str]) a list of group names.
        """
        with open(self.run_file, 'r') as file:
            line = file.readline()
            groups = []
            while line:
                line = file.readline().strip()
                if line != '':
                    groups.append(line)
        return groups
    
    def reports(self) -> List[Paragraph]:
        """
        Get a list of paragraphs containing the reports for each group in the run.
        
        :return: (List[Paragraph]) a list of Paragraph objects containing the reports.
        """
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
    
    def ouput_text(self) -> List[Paragraph]:
        """
        Add an introduction to the report.
        
        :return: (List[Paragraph]) a list of Paragraph objects containing the report introduction.
        """
        styles = getSampleStyleSheet()
        full_report = []
        groups =''
        for grp in self.get_groups():
            grp_ = group(grp)
            groups += grp_.get_name() + "&nbsp;&nbsp;&nbsp;"
        intro_txt = f'''
        Run File: {self.get_name()} <br/>
        Groups in Run: &nbsp;{groups} <br/>
        <br/>
        '''
        paragraph = Paragraph(intro_txt, style = styles["Normal"])
        full_report.append(paragraph)
        full_report.append(Spacer(1, 12))
        return full_report + self.reports()

    def output(self) -> None:
            """
            Generates a PDF report containing the group and section reports for the run.
            
            :return: None
            """
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
