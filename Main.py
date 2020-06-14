# ------------------------------------------------------------------------ #
# Title: Assignment 09 Main File
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# PO'Brien,6.14.2020, Added code in place of pseudo-code to finish assignment
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Person as Per
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
File = "EmployeeData.txt"
lstEmpObj = []
userChoice = ""

# Load data from file into a list of employee objects when script starts
fileData = Fp.read_data_from_file(File)
for line in fileData:
    lstEmpObj.append(Emp(line[0], line[1], line[2].strip()))

# Show user a menu of options
while True:
    Eio.print_menu_items()
    userChoice = Eio.input_menu_options()

    if userChoice.strip() == '1':  # Show current employee data
        Eio.print_current_list_items(lstEmpObj)

    elif userChoice.strip() == '2':  # Add new employee data
        lstEmpObj.append(Eio.input_employee_data())
        print('Employee added, press 3 to save this data to file!')

    elif userChoice.strip() == '3':  # Save employee data to File
        Fp.save_data_to_file(File, lstEmpObj)
        print("Employee data saved to file!")

    elif userChoice.strip() == '4':  # Exit Program
        print("Goodbye!")
        break

# Get user's menu option choice
# Show user current data in the list of employee objects
# Let user add data to the list of employee objects
# let user save current data to file
# Let user exit program

# Main Body of Script  ---------------------------------------------------- #
