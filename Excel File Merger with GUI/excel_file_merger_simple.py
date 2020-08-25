# Some helpful libraries
from pathlib import Path
import pandas as pd
import os


def validate_inputs(source, destination, output_file):
    # Assume there are no errors and the error message is nonexistent
    errors = False
    error_message = []

    # Path turns the source directory into a path variable that has a method
    # called exists() that checks if its valid
    # If the path doesn't exist, there is an error
    if not (Path(source)).exists():
        errors = True
        error_message.append("Please select an input directory")

    # This is similar to the above but for output directory
    if not (Path(destination)).exists():
        errors = True
        error_message.append("Please select an output directory")

    # This checks if the length of the output file is less than 1
    # if it is less than 1 or 0 characters, that means the field is empty
    if len(output_file) < 1:
        errors = True
        error_message.append("Please enter a file name")

    # This returns the errors and the message
    return(errors, error_message)


def combine_excel(source, destination, output_file):
    # make an empty dataframe
    df_combined = pd.DataFrame()
    # Create a path variable from the source directory name and
    # use the listdir function from the os library
    input_dir = os.listdir(Path(source))

    for files in input_dir:
        df = pd.read_csv(Path(source + '/' + files))
        df_combined = pd.concat(
            [df_combined, df], ignore_index=True)

    df_combined.to_csv(
        Path(destination + '/' + output_file + ".csv"), index=False)

    print("File Saved")


# These take the inputs from the intent
source = input("Input_Directory: \n").replace('"', "")
destination = input("Output_Directory: \n").replace('"', "")
output_file = input("Output_Name: \n").replace('"', "")
# This triggers the validate input function defined below to check for errors
errors, error_message = validate_inputs(
    source, destination, output_file)
# If validate inputs returns an error, show that message to the user
if errors:
    print("Error: " + error_message)
else:
    combine_excel(source, destination, output_file)
