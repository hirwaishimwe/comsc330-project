from group import group

class run:
    #costructor
    def __init__(self, runfile):
        self.run_file = runfile

    #get the run name
    def get_name(self):
        with open(self.run_file, 'r') as file:
            name = file.readline()
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
    
#################---WORK IN PROGRESS---########################

    ##processing methods

    #get the reports for the run
    def reports(self):
        report_for_all_grp = []
        for grp in self.get_groups():
            report_for_grp = []
            grp_ = group (grp)
            report_for_grp.append(grp_.group_report())
            report_for_grp.append(grp_.get_section_reports())
            report_for_all_grp.append(report_for_grp)
        return report_for_all_grp

    #Output methods  
    def output():
        pass
        #write the report to a text file
        # GUI ?