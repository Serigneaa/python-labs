# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there


# Import pathlib
import pathlib

# Find the path to my Desktop
desktop = pathlib.Path("/home/serigne/Desktop")

# Create a new folder
new_path = pathlib.Path("/home/serigne/Desktop/Screenshot_trial")
new_path.mkdir(exist_ok=True)
    
for filepath in desktop.iterdir():
    # Filter for screenshots only
    if filepath.suffix == '.png':  # Filter for screenshots only
        # Create a new path for each file
        new_filepath = new_path.joinpath(filepath.name)
        # Move the screenshot there
        filepath.replace(new_filepath)
