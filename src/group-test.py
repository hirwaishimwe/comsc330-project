
from group import group

if __name__ == '__main__':
    
    # a  group file for testing
    test_group = group('COMSC110.GRP')

# test methods for group

    #get the group name
    test = test_group.get_name()
    print(test)

    #get sections in the group
    test = test_group.get_sections()
    print(test)

    #get the sections numerical gpas
    test = test_group.get_sections_gpas()
    print(test)

    #get the group numerical gpas
    test = test_group.get_group_gpa_num()
    print(test)

    #get the sectiosn letter gpas
    test = test_group.get_group_gpa_letter()
    print(test)

    #get the number of each grade in the group
    test = test_group.get_num_each_grd()
    print(test)

    #get the number of students in the group
    test = test_group.get_num_students()
    print(test)

    #get the section reports
    test = test_group.get_section_reports()
    print(test)

    #get the z-score for the sections
    test = test_group.get_z_scores()
    print(test)

    #get the significance report for the group and sections
    test = test_group.signficance_report()
    print(test)

#---------------------- WORK IN PROGRESS ------------------------------
'''
    #get the group report
    test = test_group.group_report()
    print(test)
    
'''
