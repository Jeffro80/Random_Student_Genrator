# Overview

The Random Student Generator app selects random students from a list
of students.

## Inputs

The app takes in a CSV file with a list of Student ID numbers and names.

## Outputs

The app outputs a CSV file with the selected Students (ID numbers and names).

## Version

Version Number 0.1  

App last updated 17 October 2018  
Readme last updated 17 October 2018

# Operation

- Place the required data files into the same directory as the app file
- Run the Random_Student_Generator.py file from within Spyder or from the command
line
- Select the desired function from the menu
- Provide the names for any required files or press enter to open the Open file 
dialog
- Select the filtering option if one is required.

# Functions

## Generate Random Students

Creates a list of randomly selected students from a provided list. User determines the
number of students to be selected.

### Required Files

- Students File

# Files used

## Students File

### File Name

students.csv

### Contents

List of students (Student ID and Name) to be selected from.

### Structure

CSV file with Student ID and Name (First + ' ' + Last) for each student in the sample
pool.

### Source

User provided. 

# Dependencies

The following third-party libraries are imported and therefore are required for
the app to run:

- admintools from custtools
- filetools from custtools

# Development

## Known bugs

## Items to fix

## Current development step

- Combine names function.

## Required development steps

- Add function to combine first and last names into one column.

## Future additions

- Add option to sort on Name
- Save files as XLS