from group import group

class run:
    #costructor
    def __init__(self, runfile):
        self.run_file = runfile

    #get the run name
    def get_name(self):
        with open(self.run_file, 'r') as file:
            name = file.readline().strip()
        return name
    
    #get the run groups
    def get_groups(self):
        with open(self.run_file, 'r') as file:
            line = file.readline()
            groups = []
            while line:
                line = file.readline().strip()
                if line != '':
                    groups.append(line)
        return groups
    
    ##processing methods

    #get the reports for the run
    def reports(self):
        report_for_all_grp = ""
        for grp in self.get_groups():
            grp_ = group (grp)
            report_for_grp = grp_.group_report()
            report_for_grp += grp_.get_section_reports()
            report_for_all_grp += report_for_grp 
        return report_for_all_grp + '''
############################################# END OF THE REPORT #############################################'''
    
    #function to add an intro to the ouput text
    def ouput_text(self):
        groups =''
        for group in self.get_groups():
            groups += group + "  "
        intro_txt = f'''

        Run File: {self.get_name()}
        Groups in Run: {groups}

############################################## START OF THE REPORT ##########################################
        '''
        return intro_txt + self.reports()
    
    #Output  
    def output(self):
        with open('Report.txt', 'w') as file:
            file.write(self.ouput_text())
