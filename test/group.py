from section import section
import statistics
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from typing import List, Dict

class group:
    """
    A class to represent a group of sections in a course.

    Attributes
    ----------
    group_file : str
        The name of the file containing group data.

    Methods
    -------
    get_name() -> str:
        Returns the name of the group.
        
    get_sections() -> List[str]:
        Returns a list of the section names in the group.
        
    get_group_gpa_num() -> float:
        Returns the numerical GPA for the entire group.
        
    get_sections_gpas() -> List[float]:
        Returns a list of the numerical GPAs for each section in the group.
        
    get_num_students() -> int:
        Returns the number of students in the group.
        
    get_num_each_grd() -> Dict[str, int]:
        Returns a dictionary containing the number of students in the group who received each grade.
        
    get_z_scores() -> List[str]:
        Returns a list indicating whether the GPA of each section in the group is significantly different from the group GPA.
        
    signficance_reports() -> List[str]:
        Returns a list of significance reports for each section in the group.
        
    get_section_reports() -> List[Paragraph]:
        Returns a list of report paragraphs and graphs for each section in the group.
        
    group_report() -> str:
        Returns a report on the group.
        
    make_plot(grade_set: Dict[str, int], name: str, color: str) -> None:
        Generates a bar graph showing the grade distribution of a section.

    """
    
    def __init__(self, groupfilename: str) -> None:
        """
        Constructor for the group class.
        
        :param groupfilename: (str) the name of the file containing the group data.
        """
        self.group_file: str = groupfilename

    def get_name(self) -> str:
        """
        Get the name of the group from the group file.
        
        :return: (str) the name of the group.
        """
        with open(self.group_file, 'r') as file:
            name = file.readline().strip()
        return name
    
    def get_sections(self) -> List[str]:
        """
        Get a list of the section names in the group file.
        
        :return: (List[str]) a list of section names.
        """
        with open(self.group_file, 'r') as file:
            line = file.readline()
            sections = []
            while line:
                line = file.readline().strip()
                if line != '':
                    sections.append(line)
        return sections
    
    def get_group_gpa_num(self) -> float:
        """
        Get the numerical GPA for the entire group.
        
        :return: (float) the numerical GPA for the group.
        """
        section_gpa_total = 0
        sections = self.get_sections()
        for i in sections:
            sec = section(i)
            section_gpa_total += sec.get_gpa_num()
        group_gpa_num = section_gpa_total/len(sections)
        return group_gpa_num

    def get_sections_gpas(self) -> List[float]:
        """
        Returns a list of the GPA of each section in the group.

        Returns:
            A list of floats representing the GPA of each section in the group.
        """
        sections_gpas = []
        for i in self.get_sections():
            sec = section(i)
            sections_gpas.append(sec.get_gpa_num())
        return sections_gpas

    def get_num_students(self) -> int:
            """
            Returns the total number of students in the group.

            Returns:
                The total number of students in the group as an integer.
            """
            total_students = 0
            for i in self.get_sections():
                sec = section(i)
                total_students += sec.get_num_students()
            return total_students
        
    def get_section_reports(self) -> List[Paragraph]:
            """
            Returns a list of reportlab Paragraph objects, one for each section in the group.

            Returns:
                A list of reportlab Paragraph objects, one for each section in the group.
            """
            sections_reports = []
            section_significance = self.signficance_reports()
            sections = self.get_sections()
            for i in range(0,len(sections)):
                sec = section(sections[i])
                text = sec.section_report() + f'''{section_significance[i]}'''
                # Get sample styles
                styles = getSampleStyleSheet()
                paragraph = Paragraph(text, style = styles["Normal"])
                sections_reports.append(paragraph)
                sections_reports.append(Spacer(1, 6))
                graph_color = '#87CEFA'
                if section_significance[i] == "Significant":
                    graph_color = '#ff7f0e'
                section.make_plot(sec.get_num_each_grd(), sec.get_name(), graph_color)
                img = Image(f"{sec.get_name()}.png", width = 300, height = 200)
                img.hAlign = 'CENTER'  # Set the horizontal alignment
                sections_reports.append(img)
                sections_reports.append(Spacer(1, 12))
            return sections_reports
        
    def get_num_each_grd(self) -> Dict[str, int]:
            """
            Returns a dictionary containing the number of students in the group who received each grade.

            Returns:
                A dictionary where the keys are valid grades (A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F) and the values are
                the number of students in the group who received each grade.
            """
            grades = []
            for i in self.get_sections():
                sec = section(i)
                grades += sec.get_grades()

            # A List of valid grades
            val_grades = ["A","A-","B+","B","B-","C+","C","C-","D+","D","D-","F"]

            # Create a dictionary from the list of valid grades
            grade_dictionary = dict.fromkeys(val_grades,0)

            # Increment the values of the dictionary keys to get the number of each grade
            for x in grades:
                if x in val_grades:
                    grade_dictionary [x] += 1

            # Delete grades that are not their, ie, == 0
            for i in list(grade_dictionary.keys()): 
                if grade_dictionary[i] == 0:
                    del grade_dictionary[i]
            return grade_dictionary
        
    def get_z_scores(self) -> List[str]:
            """
            Returns a list of strings indicating the significance of the deviation of each section's GPA from the group's GPA.

            Returns:
                A list of strings indicating the significance of the deviation of each section's GPA from the group's GPA.
                The strings are either "Significant" or "Not Significant".
            """
            # A list to store the significance of each section's deviation
            section_deviations = []
            pop_mean = self.get_group_gpa_num()
            pop_stdev = statistics.stdev(self.get_sections_gpas())
            for i in self.get_sections_gpas():
                sample_mean = i
                z = (sample_mean - pop_mean)/ pop_stdev
                if z <= -2 or z >= 2:
                    section_deviations.append("Significant")
                else:
                    section_deviations.append("Not Significant")
            return section_deviations
        
    def signficance_reports(self) -> List[str]:
        """
        Returns a list of strings representing the significance of each section's deviation from the group's GPA.

        Returns:
            A list of strings where each string indicates whether the corresponding section's GPA deviation is significant or not.
        """
        report = []
        sections = self.get_sections()
        z_scores = self.get_z_scores()
        tab = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        for i in range(0,len(sections)):
            report.append(f"{tab}{tab}Difference from group GPA: " + z_scores[i] + "\n")
        return report

    def group_report(self) -> str:
        """
        Generates a report of the group's performance.

        Returns:
            A string containing the report of the group's performance, including the number of courses, number of students,
            number of each grade, and the overall GPA of the group.
        """
        report = (
            f"*************************************************************************************************************<br/>"
            f"*************************************************************************************************************<br/>"
            f"<br/>"
            f"Group Report: {self.get_name()}<br/>"
            f"  Number of courses: {len(self.get_sections())}<br/>"
            f"  Number of students: {self.get_num_students()}<br/>"
            f"  Number of each grade: {self.get_num_each_grd()}<br/>"
            f"  Overall GPA of the group: {self.get_group_gpa_num():0.2f}<br/>"
        )
        return report