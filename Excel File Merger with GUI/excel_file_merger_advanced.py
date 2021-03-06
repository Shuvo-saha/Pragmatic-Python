# Some helpful libraries
from appJar import gui
from pathlib import Path
import pandas as pd
import os

# When button is pressed, check if its quit or combine


def press(button):
    if button == "Combine":
        # These take the inputs from the button
        source = app.getEntry("Input_Directory")
        destination = app.getEntry("Output_Directory")
        output_file = app.getEntry("Output_Name")
        # This triggers the validate input function defined below to check for errors
        errors, error_message = validate_inputs(
            source, destination, output_file)
        # If validate inputs returns an error, show that message to the user
        if errors:
            app.errorBox("Error", "\n".join(error_message))
        # If no errors trigger the combine excel function which takes 3 arguments
        # source directory, destination directory and output file name
        else:
            combine_excel(source, destination, output_file)
    elif button == "Quit":
        # exit command on appjar
        app.stop()


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

    # This checks all the files in the input directory to see if
    # they're all csv files or not

    # Create a path variable from the source directory name and
    # use the listdir function from the os library to allow
    # the program to iterate over all the files in the input directory
    input_dir = os.listdir(Path(source))
    csv_error_message = ''
    for files in input_dir:
        # Create an error message if the suffix of the file is not .csv
        if Path(files).suffix.lower() != ".csv":
            errors = True
            csv_error_message = "Please select a directory with only csv files"
    # Note that this is out of the loop because I don't want to repeat the
    # error message in the loop
    error_message.append(csv_error_message)

    # This returns the errors and the message
    return(errors, error_message)


def combine_excel(source, destination, output_file):
    # make an empty dataframe
    df_combined = pd.DataFrame()
    input_dir = os.listdir(Path(source))
    # Similar iteration to the error message iteration before
    # reads through all the files in the directory and adds
    # that dataframe to our main dataframe
    for files in input_dir:
        df = pd.read_csv(Path(source + '/' + files))
        df_combined = pd.concat(
            [df_combined, df], ignore_index=True)

    # Saves the dataframe to our output directory
    df_combined.to_csv(
        Path(destination + '/' + output_file + ".csv"), index=False)

    if(app.questionBox("File Saved", "Output csv files saved. Do you want to quit?")):
        app.stop()


# Name of the app and the theme and size
app = gui("Excel File Merger", useTtk=True)
app.setTtkTheme("clam")
app.setSize(500, 200)

# The first button with input directory
app.addLabel("Choose Folder with CSV Files to be Merged")
app.addDirectoryEntry("Input_Directory")
# The second button with output directory
app.addLabel("Select Output Directory")
app.addDirectoryEntry("Output_Directory")
# Output file name entry
app.addLabel("Output File Name")
app.addEntry("Output_Name")
# Two buttons at the end
app.addButtons(["Combine", "Quit"], press)

# Start the app
app.go()
