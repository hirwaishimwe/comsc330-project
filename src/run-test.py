
from run import run

if __name__ == "__main__":

    #test inputting a file and creating a run obj
    test_run = run (input("Enter Run file: "))

# run method tests

    #get the run name
    test = test_run.get_name()
    print(test)

    # get the run groups
    test = test_run.get_groups()
    print(test)

###############------ WORK IN PROGRESS -----###############

'''
    #get the report this run
    test = test_run.reports()
    print(test)

    #test getting the run output
    test_run.output()

'''