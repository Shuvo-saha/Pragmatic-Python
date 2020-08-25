# Make sure to install openpyxl and xlrd
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

    # This returns the errors and the message
    return(errors, error_message)


def combine_excel(source, destination, output_file):
    # make an empty dataframe
    df_combined = pd.DataFrame()
    # Create a path variable from the source directory name and
    # use the listdir function from the os library
    input_dir = os.listdir(Path(source))

    for files in input_dir:
        df = pd.read_excel(Path(source + '/' + files))
        df_combined = pd.concat(
            [df_combined, df], ignore_index=True)

    print("\n")
    print(Path(destination), "\n")
    print(output_file, "\n")
    df_combined.to_excel(Path(destination + '/' + output_file + ".xlsx"))

    if(app.questionBox("File Saved", "Output Excel files saved. Do you want to quit?")):
        app.stop()


app = gui("Excel File Merger", useTtk=True)
app.setTtkTheme("clam")
app.setSize(500, 200)

app.addLabel("Choose Folder with Excel Files to be Merged")
app.addDirectoryEntry("Input_Directory")

app.addLabel("Select Output Directory")
app.addDirectoryEntry("Output_Directory")

app.addLabel("Output File Name")
app.addEntry("Output_Name")

app.addButtons(["Combine", "Quit"], press)


app.go()
