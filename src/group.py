from section import section
import statistics

class group:

    #constructor
    def __init__(self, groupfilename):
        self.group_file = groupfilename

    #get the group name
    def get_name(self):
        with open(self.group_file, 'r') as file:
            name = file.readline()
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
    
    #get the group numerical gpa
    def get_group_gpa_num(self):
        section_gpa_total = 0
        sections = self.get_sections()
        for i in sections:
            sec = section(i)
            section_gpa_total += sec.get_gpa_num()
        group_gpa_num = section_gpa_total/len(sections)
        return group_gpa_num

    #get the group letter gpa
    def get_group_gpa_letter(self):
        gpa_letter = section.comp_letter_gpa(self.get_group_gpa_num())
        return gpa_letter

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
        sections_reports = ""
        for i in self.get_sections():
            sec = section(i)
            sections_reports += sec.section_report()
        return sections_reports
    
    #get the number of each grade in the group
    def get_num_each_grd(self):
        grades = []
        for i in self.get_sections():
            sec = section(i)
            grades += sec.get_grades()
        grade_dictionary = dict.fromkeys(set(grades),0)
        for x in grades:
            grade_dictionary [x] += 1
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
    def signficance_report(self):
        report = "Each section's difference from the group: \n"
        sections = self.get_sections()
        z_scores = self.get_z_scores()
        for i in range(0,len(sections)):
            report += sections[i] +" : " + z_scores[i] + "\n"
        return report

    #get the group report
    def group_report(self):
        report = f'''
 Group Report: {self.get_name()}
 Number of courses, {len(self.get_sections())}
 Number of students, {self.get_num_students()}
 Number of each grade, {self.get_num_each_grd()}
 Overall GPA of the group, {self.get_group_gpa_letter()}

'''
        return report