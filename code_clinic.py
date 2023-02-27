import sys
from verify_email import verify_email  # pip3 install verify_email
from datetime import datetime

text = True
if len(sys.argv) > 1:
    if sys.argv[1] == "view":
        import google_api.view_calendar  as view  # Code that allows user to view calendar for events
    elif sys.argv[1] == "volunteer":
        import google_api.create_event as create  # Code that allows the volunteer to allocate availbility
    elif sys.argv[1] == "cancel":
        import google_api.delete_event as delete  # Code that allows user to cancel an event
    elif sys.argv[1] == "book":
        import google_api.update_event as update  # Code that allows the student to make a booking
    else:
        import code_clinic as main
        text = True
else:
    import code_clinic as main
    text = True


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "help":
            with open("help.txt", "r") as file:
                content = file.read()
                print(content)
            if "session" in sys.argv:
                welcome()
        if sys.argv[1] == "login" and "allocate" not in sys.argv and "book" not in sys.argv:
            print("wrong command\n  login --- \n    did you mean 'login allocate' or 'login book'")
        if sys.argv[1] == "login":
            if "allocate" in sys.argv:
                user_email_v = get_email()
                print(f"Welcome {user_email_v} to code clinics\n")

                print("Allocate Availability")
                allocate_slot()
                get_location()

                # info = (f"User: Volunteer Email: {user_email_v} Campus: {location} Date and Time: {date_time}")
                # with open("user_info.txt","a+") as f:
                #     f.write(f"Welcome {user_email_v}")
                #     f.writelines(info + "\n")

            elif "book" in sys.argv:
                user_email_s = get_email()
                print(f"Welcome {user_email_s} to code clinics\n")

                print("Make Booking")
                allocate_slot()
                get_location()
                get_description()

                # info = (f"User: Student Email: {user_email_s} Campus: {location} Date and Time: {date_time} Problem: {problem}")
                # with open("user_info.txt","a+") as f:
                #     f.write(f"Welcome {user_email_s}")
                #     f.write(info + "\n")


def welcome():
    guides ="""SESSIONS:
Are between 8am and 17:30 pm
Each session is for 30 minute
May have the booking virtually or on physically
*** run 'python code_clinic.py help' to get a full overview on how to use the system's commands ***

Booking Session:
Allowed to book only when there's an available slot
Cannot make a double booking

Volunteering Session:
Cannot cancel the booking when there is 
Allowed to
"""
    print(guides)


def get_email():
    while True:
        user_email = input("Enter email address: ")
        # if verify == True:
        return user_email


def get_location():
    while True:
        user_campus = input('Enter location: ').lower()
        return user_campus


def allocate_slot():
    date_and_time = input('Enter date and time (yyyy-mm-dd hh:mm): ')

    if int(date_and_time[12:13]) >= 8 and int(date_and_time[11:13]) <= 18 and int(date_and_time[:4]) == 2023:
        date_and_time = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M")
 
    return date_and_time


def get_description():
    description = input('What do you need help with?\n')
    return description


# def fully_booked():
#     info = (f"{user_email_v} - {user_email_s} - {location} - {date_time} - {problem}")
#     with open("bookings.csv","a+") as f:
#         f.write("Volunteer - Student - Date and Time  - Problem\n")
#         f.writelines(info + "\n")

if __name__ == '__main__':
   main()

