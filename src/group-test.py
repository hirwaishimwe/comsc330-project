
from group import group

if __name__ == '__main__':
    
    # a  group file for testing
    test_group = group('COMSC110.GRP')

# test methods for group

    #get the group name
    test = test_group.get_name()
    print(f'{test} \n')

    #get sections in the group
    test = test_group.get_sections()
    print(f'{test} \n')

    #get the sections numerical gpas
    test = test_group.get_sections_gpas()
    print(f'{test} \n')

    #get the group numerical gpas
    test = test_group.get_group_gpa_num()
    print(f'{test} \n')

    #get the sectiosn letter gpas
    test = test_group.get_group_gpa_letter()
    print(f'{test} \n')

    #get the number of each grade in the group
    test = test_group.get_num_each_grd()
    print(f'{test} \n')

    #get the number of students in the group
    test = test_group.get_num_students()
    print(f'{test} \n')

    #get the section reports
    test = test_group.get_section_reports()
    print(f'{test} \n')

    #get the z-score for the sections
    test = test_group.get_z_scores()
    print(f'{test} \n')

    #get the significance report for the group and sections
    test = test_group.signficance_report()
    print(f'{test} \n')

    #get the group report
    test = test_group.group_report()
    print(f'{test} \n')
    
