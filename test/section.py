
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
        report = f'''
     Section Report: {self.get_name()}
       Number of students, {self.get_num_students()} 
       Number of each grade, {self.get_num_each_grd()} 
       Overall GPA of the section: {self.get_gpa_num() : 0.2f} 
       '''
        return report