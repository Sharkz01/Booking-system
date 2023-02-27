def get_help_command():
    help_command ="""help session - used to show information related to the Code Clinic Booking System
login book - used by a student to make a booking
login allocate - used by a volunteer to allocated availability
cancel book - used to cancel a booking
cancel allocate - used to cancel an availability
download - used to download their data file
"""
    with open("help.txt","w") as file:
        data = file.write(help_command)
        # print(data)
    return data

get_help_command()