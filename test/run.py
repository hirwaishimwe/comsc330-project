from group import group
import os
import matplotlib.pyplot as plt
import math

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

    #make group distribution plots 
    # make plots function
    def make_plots(self):
        for grp in self.get_groups():
            grp_ = group(grp)
            data = grp_.get_num_each_grd()

            # Extract keys and values from the dictionary
            keys = list(data.keys())
            values = list(data.values())

            # Create a bar chart with sorted keys and values
            plt.bar(x = keys, height = values)

            # Add title and axis labels
            plt.title(f'{grp_.get_name()} Group Distribution Graph')
            plt.xlabel('Grade')
            plt.ylabel('Number Of Each Grade')
            plt.yticks(range(math.ceil(0), math.floor(max(values)) + 1))
            
            # Save the plots
            filename = f'Report & Graphs/{grp_.get_name()}.png'
            plt.savefig(filename)
            plt.clf()

    #Output  
    def output(self):
        # Create a new folder if it does not exist
        if not os.path.exists('Report & Graphs'):
            os.makedirs('Report & Graphs')
        # Make and write to the report file
        with open(f'Report & Graphs/Report.txt', 'w') as file:
            file.write(self.ouput_text())
        self.make_plots()
