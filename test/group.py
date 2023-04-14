from section import section
import statistics
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

class group:

    #constructor
    def __init__(self, groupfilename):
        self.group_file = groupfilename

    #get the group name
    def get_name(self):
        with open(self.group_file, 'r') as file:
            name = file.readline().strip()
        return name
    
    #get sections in the group
    def get_sections(self):
        with open(self.group_file, 'r') as file:
            line = file.readline()
            sections = []
            while line:
                line = file.readline().strip()
                if line != '':
                    sections.append(line)
        return sections
    
    #get the sections numerical gpas
    def get_group_gpa_num(self):
        section_gpa_total = 0
        sections = self.get_sections()
        for i in sections:
            sec = section(i)
            section_gpa_total += sec.get_gpa_num()
        group_gpa_num = section_gpa_total/len(sections)
        return group_gpa_num

    #get the sections numerical gpas
    def get_sections_gpas(self):
        sections_gpas = []
        for i in self.get_sections():
            sec = section(i)
            sections_gpas.append(sec.get_gpa_num())
        return sections_gpas
    
    #get the number of students in the group
    def get_num_students(self):
        total_students = 0
        for i in self.get_sections():
            sec = section(i)
            total_students += sec.get_num_students()
        return total_students
    
    #get the section reports
    def get_section_reports(self):
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
    
    #get the number of each grade in the group
    def get_num_each_grd(self):
        grades = []
        for i in self.get_sections():
            sec = section(i)
            grades += sec.get_grades()
        #list of valid grades
        val_grades = ["A","A-","B+","B","B-","C+","C","C-","D+","D","D-","F"]
        #create a dictionary from the list of valid grades
        grade_dictionary = dict.fromkeys(val_grades,0)
        #increment the values of the dictionary keys to get the number of each grade
        for x in grades:
            if x in val_grades:
                grade_dictionary [x] += 1
        #delete grades that are not their, ie, == 0
        for i in list(grade_dictionary.keys()): 
            if grade_dictionary[i] == 0:
                del grade_dictionary[i]
        return grade_dictionary
    
    #get the z-score for the sections
    def get_z_scores(self):
        # a list to store the significance of each section's deviation
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
    
    #get the significance report for the group and sections
    def signficance_reports(self):
        report = []
        sections = self.get_sections()
        z_scores = self.get_z_scores()
        tab = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        for i in range(0,len(sections)):
            report.append(f"{tab}{tab}Difference from group GPA: " + z_scores[i] + "\n")
        return report

    #get the group report
    def group_report(self):
        report = (
            f"*************************************************************************************************************<br/>"
            f"*************************************************************************************************************<br/>"
            f"<br/>"
            f"Group level: {self.get_name()}<br/>"
            f"  Number of courses: {len(self.get_sections())}<br/>"
            f"  Number of students: {self.get_num_students()}<br/>"
            f"  Number of each grade: {self.get_num_each_grd()}<br/>"
            f"  Overall GPA of the group: {self.get_group_gpa_num():0.2f}<br/>"
        )
        return report