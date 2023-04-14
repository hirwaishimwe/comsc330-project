from run import run
import os
import sys

if __name__ == "__main__":

    # Get the directory where the executable is located
    exe_dir = os.path.dirname(sys.executable)

    # Change the working directory to the directory where the executable is located
    os.chdir(exe_dir)

    #input a file and create a run obj
    this_run = run (input("Enter Run file: "))

    #get the run output
    this_run.output()