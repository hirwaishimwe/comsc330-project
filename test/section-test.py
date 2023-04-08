from section import section
import os

if __name__ == '__main__':
    
    #change to the test directory
    os.chdir('./test')

    # a section file for testing
    test_section = section(('COMSC110S20.SEC'))

#method tests for section

    #get section name
    test = test_section.get_name()
    print(f'{test} \n')

    #get the grades of a section
    test = test_section.get_grades()
    print(f'{test} \n')

    #get the number of students in the section
    test = test_section.get_num_students()
    print(f'{test} \n')

    #get the number gpa of the section
    test = test_section.get_gpa_num()
    print(f'{test} \n')

    #get number of each in the section
    test = test_section.get_num_each_grd()
    print(f'{test} \n')

    #get the section report 
    test = test_section.section_report()
    print(f'{test} \n')