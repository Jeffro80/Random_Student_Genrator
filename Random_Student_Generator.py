# Random Student Generator
# Version 0.1 17 October 2018
# Created by Jeff Mitchell
# Takes a list of students and randomly selects the desired number of students
# from the list


import csv
import custtools.admintools as ad
import custtools.filetools as ft
import random
import sys



def combine_names():
    """Combine first and last name columns into one column"""
    # To Be Written
    print('\nFunction to be written')
    return


def generate_random_students():
    """Generate a list of randomly selected students."""
    # Confirm the required files are in place
    required_files = ['Students File']
    ad.confirm_files('Generate Random Students', required_files)
    # Get name for Students File and then load
    student_pool = ft.get_csv_fname_load('Students File')
    print(student_pool)
    # Get number of students to take from the sample
    num_students = get_num_students(len(student_pool))
    # Get required number of students from the pool and store in a list
    sampled_students = get_sample(student_pool, num_students)
    # Display pooled students
    print('\nThe selected students are as follows:\n')
    print("{:15} {}".format('Student ID', 'Name'))
    for x in sampled_students:
        print("{:15} {}".format(x[0], x[1]))
    print('')
    # Save results
    headings = ['Student ID', 'Name']
    f_name = 'Selected_students_'
    ft.save_list_csv(sampled_students, headings, f_name)
    

def get_num_students(num_in_pool):
    """Get from user number of students to select.
    
    Gets input from user for the number of students to select and makes sure
    this number is less than the number of students in the sample pool.
    
    Args:
        num_in_pool (int): Number of students in the sample pool.
        
    Returns:
        num_students (int): Number of students to be selected.    
    """
    while True:
        print('\nHow many students would you like to select? Max allowed is '
              '{}: '.format(num_in_pool-1))
        try:
            num_students = int(input('Number of students: '))
        except ValueError:
            print('\nPlease enter a whole number less than {}'.format(
                    num_in_pool))
        else:
            if num_students >= num_in_pool: # Too many students
                print('\nThat is too many students! Please enter a whole '
                      'number that is less than {}.'.format(num_in_pool))
            elif num_students < 0: # Negative value provided
                print('\nPlease enter a positive whole number that is less '
                      'than {}.'.format(num_in_pool))
            else:
                return num_students


def get_sample(student_pool, num_students):
    """Return list of randomly selected students.
    
    Randomly selects the desired number of students from the student pool and
    returns them as a list of Student ID + Name tuples.
    
    Args:
        student_pool (list): List of Student ID and Name combinations.
        num_students (int): Number of students to be sampled.
        
    Returns:
        students (list): List of selected Student ID and Name combinations.
    """
    sample_pool = list(student_pool)
    students = []
    if num_students >= len(sample_pool) or num_students < 0:
        # Catch invalid number of students
        print('Invalid number of students requested.')
        return ''
    else:
        # Sample required number of students
        i = 0
        while i < num_students:
            # Get length of sample pool for random range
            sample_length = len(sample_pool)-1
            # Select random student
            j = random.randint(0, sample_length)
            student = sample_pool[j]
            # Add student to students list
            students.append(student)
            # Remove student from sample pool
            del sample_pool[j]
            i += 1
        students = sorted(students)
        return students      


def main():
    repeat = True
    low = 1
    high = 2
    while repeat:
        try_again = False
        main_message()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between {} and {}.'.format(low, high))
            try_again = True
        else:
            if int(action) < low or int(action) > high:
                print('\nPlease select from the available options ({} - {})'
                      .format(low, high))
                try_again = True
            elif action == low:
                generate_random_students()
            elif action == 2:
                combine_names()
            elif action == high:
                print('\nIf you have generated any files, please find them '
                      'saved to disk. Goodbye.')
                sys.exit()
        if not try_again:
            repeat = ad.check_repeat()
    print('\nPlease find your files saved to disk. Goodbye.')
    
 
def main_message():
    """Print the menu of options."""
    print('\n\n*************==========================*****************')
    print('\nRandom Student Generator version 0.1')
    print('Created by Jeff Mitchell, 2018')
    print('\nOptions:')
    print('\n1. Generate Random Students')
    print('2. Combine Student Names')
    print('3. Exit')
                
                
if __name__ == '__main__':
    main()