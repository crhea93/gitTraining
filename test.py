'''
Test python script for Git Training Purposes
This program is written to ask the user their name and print it in the terminal.
Before running this program, please fix the three minor issues :)
After a successful run, please submit a pull request!
'''

def read_input():
    # Please allow the user to enter their first and last name from the terminal
    # Hint: We call this a raw input
    first_name = input("First name >>>")
    last_name = input("Last name >>>")

    # Please fix the following print statement
    # 'Welcome %s %s'%(first_name,last_name)
    output  = f"Welcome {first_name} {last_name}"
    print(output)

    

    #Supply the approriate return (We aren't actually returning anything :) )
    return output

read_input()    

