"""
app.py is used to store all app data that needs to be accessed independently of the hierarchy of the rest of the
software.
"""

# set name for application (shouldn't need to be changed)
name = "Structural Calculator"
# create pointer to display_label variable that can be called from anywhere in the software (allows all classes to call)
display_label = None
# set precision to 1/16 unless changed by user
precision = ".0625"
