import matplotlib.pyplot as plt
import math
from typing import List, Dict

class section:
    """
    A class to represent a section of a course.

    Attributes
    ----------
    section_file : str
        The name of the file containing section data.

    Methods
    -------
    get_name() -> str:
        Returns the name of the section.
        
    get_grades() -> List[str]:
        Returns a list of the grades in the section.
        
    get_gpa_num() -> float:
        Returns the numerical GPA of the section.
        
    get_num_students() -> int:
        Returns the number of students in the section.
        
    get_num_each_grd() -> Dict[str, int]:
        Returns a dictionary containing the number of each grade in the section.
        
    section_report() -> str:
        Returns a report on the section.
        
    make_plot(grade_set: Dict[str, int], name: str, color: str) -> None:
        Generates a bar graph showing the grade distribution of the section.
    """

    def __init__(self, sectionfilename: str) -> None:
        self.section_file = sectionfilename

    def get_name(self) -> str:
        """
        Get the name of the section from the section_file.
        Returns:
            str: The name of the section.
        """
        try:
            with open(self.section_file, 'r') as file:
                name = file.readline().strip()
            return name
        except FileNotFoundError:
            print(f"File not found: {self.section_file}")
            return ""
    
    def get_grades(self) -> List[str]:
        """
        Returns a list of the grades in the section.

        Returns:
            List[str]: A list of the grades in the section.
        """
        with open(self.section_file, 'r') as file:
            line = file.readline().strip()
            grades =[]
            while line:
                line = file.readline().strip().strip('\"')
                if line != '':
                    line_split = line.split(",")
                    grades.append(line_split[3].lstrip('\"'))
            return grades
        
    def get_gpa_num(self) -> float:
        """
        Returns the numerical GPA of the section calculated from the 
        grades obtained by calling the 'get_grades()' method.
        
        Returns:
        -------
        float:
            The numerical GPA of the section.
        """
        grades_gpa = {
            'A': 4.00, 'A-': 3.67, 'B+': 3.33, 'B': 3.00,
            'B-': 2.67, 'C+': 2.33, 'C': 2.00, 'C-': 1.67,
            'D+': 1.33, 'D': 1.00, 'D-': 0.67, 'F': 0.00
        }
        total_gpa = 0
        num_grades = 0
        for grade in self.get_grades():
            if grade in grades_gpa:
                total_gpa += grades_gpa[grade]
                num_grades += 1
        gpa_num = total_gpa / (num_grades * 2) if num_grades > 0 else 0.00
        return gpa_num
    
    def get_num_students(self) -> int:
        """
        Returns the number of students in the section based on the number of grades in the section.
        """
        return len(self.get_grades())

    def get_num_each_grd(self) -> Dict[str, int]:
        """
        Returns a dictionary containing the count of each grade in the section.

        Returns:
        -------
        dict:
            A dictionary where the keys are the valid grades (A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F)
            and the values are the count of each grade in the section.
        """
        grades = self.get_grades()

        # list of valid grades
        val_grades = ["A","A-","B+","B","B-","C+","C","C-","D+","D","D-","F"]

        # Create a dictionary from the list of valid grades
        grade_dictionary = dict.fromkeys(val_grades, 0)

        # Increment the values of the dictionary keys to get the number of each grade
        for x in grades:
            if x in val_grades:
                grade_dictionary [x] += 1

        # Delete grades that are not their, i.e., == 0
        for i in list(grade_dictionary.keys()): 
            if grade_dictionary[i] == 0:
                del grade_dictionary[i]
        return grade_dictionary

    def section_report(self) -> str:
        """
        Generate a report for the section.

        Returns:
            str: The section report.
        """
        tab = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'

        report = (
            f"{tab}Section Report: {self.get_name()}<br/>"
            f"  {tab}{tab}Number of students: {self.get_num_students()}<br/>"
            f"  {tab}{tab}Number of each grade: {self.get_num_each_grd()}<br/>"
            f"  {tab}{tab}Overall GPA of the section: {self.get_gpa_num():0.2f}<br/>"
        )
        return report

    @staticmethod
    def make_plot(grade_set: Dict[str, int], name: str, color: str) -> None:
        """Create a bar chart showing the distribution of grades in a section or group.

        Args:
            grade_set: A dictionary containing the number of each grade in the section or group.
            name: The name of the section or group.
            color: The color to use for the bar chart.

        Returns:
            The filename of the saved plot.
        """

        data = grade_set

        # Extract keys and values from the dictionary
        keys = list(data.keys())
        values = list(data.values())
        color = color
    
        # Create a bar chart with sorted keys and values
        plt.bar(x = keys, height = values, color = color)

        # Add title and axis labels
        plt.title(f'{name} Group Distribution Graph')
        plt.xlabel('Grade')
        plt.ylabel('Number Of Each Grade')
        
        # Use numpy to create evenly spaced values for the y-axis ticks to ensure they are always whole numbers
        plt.yticks(range(math.ceil(0), math.floor(max(values)) + 1))
            
        # Save the plot
        filename = f'{name}.png'
        with open(filename, 'wb') as f:
            plt.savefig(f)

        # Clear the current figure
        plt.clf()

