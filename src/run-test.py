from run import run

if __name__ == "__main__":

    #test inputting a file and creating a run obj
    test_run = run (input("Enter Run file: "))

# run method tests

    #get the run name
    test = test_run.get_name()
    print(f'{test} \n')

    # get the run groups
    test = test_run.get_groups()
    print(f'{test} \n')

    #get the report this run
    test = test_run.reports()
    print(f'{test} \n')
    
    #function to add an intro to the ouput text
    test = test_run.ouput_text()
    print(f'{test} \n')

    #test getting the run output
    test_run.output()