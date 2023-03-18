
class section:

    #constructor
    def __init__(self,filename):
        self.section_file = filename
    
    #get section name
    def get_name(self):
        with open(self.section_file, 'r') as file:
            name = file.readline()
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
        low = 0
        high = 0
        grades_added = 0
        for i in self.get_grades():
            if i == 'A':
                low += 94
                high += 100
                grades_added += 1
            elif i == 'A-':
                low += 90
                high += 93.9
                grades_added += 1
            elif i == 'B+':
                low += 87
                high += 89.9
                grades_added += 1
            elif i == 'B':
                low += 84
                high += 86.9
                grades_added += 1
            elif i == 'B-':
                low += 80
                high += 83.9
                grades_added += 1
            elif i == "C+":
                low += 77
                high += 79.9
                grades_added += 1
            elif i == "C":
                low += 74
                high += 76.9
                grades_added += 1
            elif i == 'C-':
                low += 70
                high += 73.9
                grades_added += 1
            elif i == 'D':
                low += 67
                high += 69.9
                grades_added += 1
            elif i == 'F':
                low += 0
                high += 66.9
                grades_added += 1
            
        gpa_num = (high + low) / (grades_added*2)
        return gpa_num
    
    # compute the letter gpa of a given numerical gpa
    @staticmethod
    def comp_letter_gpa(gpa_num):
        if gpa_num  > 94:
                gpa_letter = 'A'
        elif gpa_num  > 90:
                gpa_letter = 'A-'
        elif gpa_num  > 87:
                gpa_letter = 'B+'
        elif gpa_num  > 84:
                gpa_letter = 'B'
        elif gpa_num  > 80:
                gpa_letter = 'B-'
        elif gpa_num  > 77:
                gpa_letter = 'C+'
        elif gpa_num  > 74:
                gpa_letter = 'C'
        elif gpa_num  > 70:
                gpa_letter = 'C-'
        elif gpa_num  > 67:
                gpa_letter = 'D'
        elif gpa_num  < 67:
                gpa_letter = 'F'
        return gpa_letter
    
    #get letter gpa of the section    
    def get_gpa_letter(self):
        gpa_letter = self.comp_letter_gpa(self.get_gpa_num())
        return gpa_letter
        
    
    #get the number of students in the section
    def get_num_students(self):
         return len(self.get_grades())

    #get number of each in the section
    def get_num_each_grd(self):
        grades = self.get_grades()
        grade_dictionary = dict.fromkeys(set(grades),0)
        for x in grades:
            grade_dictionary [x] += 1
        return grade_dictionary
    
    ######################### work in progress #######################

    #get the section report 
    def section_report(self):
        report = f'''
        Section level: {self.get_name()}
        Number of students {self.get_num_students()} 
        number of each grade {self.get_num_each_grd()} 
        overall GPA of the section {self.get_gpa_letter()}, 
        '''
        return report

