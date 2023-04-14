import matplotlib.pyplot as plt
import math

class section:

    #constructor
    def __init__(self,filename):
        self.section_file = filename
    
    #get section name
    def get_name(self):
        with open(self.section_file, 'r') as file:
            name = file.readline().strip()
        return name
    
    #get the grades of a section
    def get_grades(self):
        with open(self.section_file, 'r') as file:
            line = file.readline().strip()
            grades =[]
            while line:
                line = file.readline().strip().strip('\"')
                if line != '':
                    line_split = line.split(",")
                    grades.append(line_split[3].lstrip('\"'))                             
            return grades
        
    #get the number gpa of the section              
    def get_gpa_num(self):
        total = 0
        grades_added = 0
        for i in self.get_grades():
            if i == 'A':
                total += 4.00
                grades_added += 1
            elif i == 'A-':
                total += 3.67
                grades_added += 1
            elif i == 'B+':
                total += 3.33
                grades_added += 1
            elif i == 'B':
                total += 3.00
                grades_added += 1
            elif i == 'B-':
                total += 2.67
                grades_added += 1
            elif i == "C+":
                total += 2.33
                grades_added += 1
            elif i == "C":
                total += 2.00
                grades_added += 1
            elif i == 'C-':
                total += 1.67
                grades_added += 1
            elif i == 'D+':
                total += 1.33
                grades_added += 1
            elif i == 'D':
                total += 1.00
                grades_added += 1
            elif i == 'D-':
                total += 0.67
                grades_added += 1
            elif i == 'F':
                total += 0.00
                grades_added += 1
            
        gpa_num = (total) / (grades_added*2)
        return gpa_num
    
    #get the number of students in the section
    def get_num_students(self):
         return len(self.get_grades())

    
    #get number of each in the section
    def get_num_each_grd(self):
        grades = self.get_grades()
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
    
    #get the section report 
    def section_report(self):
        tab = '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
        report = (
            f"{tab}Section Report: {self.get_name()}<br/>"
            f"  {tab}{tab}Number of students: {self.get_num_students()}<br/>"
            f"  {tab}{tab}Number of each grade: {self.get_num_each_grd()}<br/>"
            f"  {tab}{tab}Overall GPA of the section: {self.get_gpa_num():0.2f}<br/>"
        )
        return report

    #a static method that will be used to make grade ditribution graphs for the sections and groups
    @staticmethod
    def make_plot(grade_set, name, color):
        data = grade_set
        # Extract keys and values from the dictionary
        keys = list(data.keys())
        values = list(data.values())
        #edgecolor = 'black'
        #linewidth = 1
        color = color
    
        # Create a bar chart with sorted keys and values
        plt.bar(x = keys, height = values, color = color)

        # Add title and axis labels
        plt.title(f'{name} Group Distribution Graph')
        plt.xlabel('Grade')
        plt.ylabel('Number Of Each Grade')
        plt.yticks(range(math.ceil(0), math.floor(max(values)) + 1))
            
        # Save the plots
        filename = f'{name}.png'
        plt.savefig(filename)

        #clear the current figure
        plt.clf()