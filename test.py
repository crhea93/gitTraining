'''
Test python script for Git Training Purposes
This program is written to ask the user their name and print it in the terminal.
Before running this program, please fix the three minor issues :)
After a successful run, please submit a pull request!
'''

def read_input(first,last):
    # Please allow the user to enter their first and last name from the terminal
    # Hint: We call this a raw input
    first_name = first;
    last_name = last;

    # Please fix the following print statement
    print('Welcome %s %s'%(first_name,last_name))

    #Supply the approriate return (We aren't actually returning anything :) )

first = input('Enter your first name: ')
last = input('Enter your last name: ')
      
read_input(first,last)
