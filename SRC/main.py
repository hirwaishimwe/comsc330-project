#########------ WORK IN PROGRESS -----##########

from run import run

if __name__ == "__main__":

    #input a file and create a run obj
    this_run = run (input("Enter Run file: "))

    #get the run output
    this_run.output()