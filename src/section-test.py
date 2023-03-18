
from section import section

if __name__ == '__main__':
    
    # a section file object for testing
    test_section = section(('COMSC110S20.SEC'))

#method tests for section

    #get section name
    test = test_section.get_name()
    print(test)

    #get the grades of a section
    test = test_section.get_grades()
    print(test)

    #get the number of students in the section
    test = test_section.get_num_students()
    print(test)

     #get the number gpa of the section
    test = test_section.get_gpa_num()
    print(test)

     #get letter gpa of the section
    test = test_section.get_gpa_letter()
    print(test)

     #get number of each in the section
    test = test_section.get_num_each_grd()
    print(test)

##############---- WORK IN PROGRESS ---###################
    #get the section report 
    print("--------------- WORK IN PROGRESS -----------------")
    test = test_section.section_report
    print(test)
