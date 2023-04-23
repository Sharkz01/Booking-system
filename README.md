# Booking-system

*Overview of the Coding Clinic Booking System
The booking system will be implemented as a set of command-line tools that must satisfy the following criteria, in addition to the requirements below.

run on the Linux version that you are using on campus

take command-line arguments as input

it must have a help command that describes the command-line arguments

it must provide output either to a file and/or to standard output, so that it can be used by another command-line tool in the system

if providing output via standard output, it means the output can also be piped to a file using the Linux pipe operators

you can choose in what data format you will store any internal data, e.g. JSON, xml, or something else entirely.

# Requirements
*Configure the system
In order to use the booking system, a student should be able to configure the system to connect to their WeThinkCode_ Google calendar, and the Code Clinic Google calendar.

It should be possible to verify that the tool is configured correctly by checking that the connection to Google Calendar is successful.

Configuration data should be stored in a hidden file in the user’s home directory.

*View calendars
In order to view bookings, a student should able to download the student’s google calendar and the Coding Clinic’s Google calendar.

Only the next 7 days (including the current day) data must be downloaded. Weekends and public holidays are counted in the 7 days.

The calendar data should be stored in a file on the local workstation.

Each time the tool is run, the data file must be updated with latest 7 days of data. Old data can be discarded.

If the data file already contains the latest data, then do not download the data again.

the data read from the file should be displayed in a convenient, easy to read layout on the screen.

*Make a booking
In order to book a slot, the student should specify a slot by date and time and all calendars should be updated accordingly.

The data file should also be updated with the latest booking information.

A slot can only be booked if there is a volunteer allocated to that slot.

The booking should also have a description of help that they need.

The duration for each slot is half hour.

Do not allow a slot that is already booked to be double booked.

*Volunteer for a slot
As a student that wants to volunteer their time in the coding clinic, I want to indicate my availability for a specific slot.

Do not allow double booking for volunteers

The booking should also show on the volunteer’s personal Google Calendar

The data file for the volunteer should be updated as well

*Cancel booking
A student should be allowed to cancel their own booking.

Do not allow cancellation of empty slots

Do not allow cancellation of another student’s booking

Cancelling the booking should not remove the Volunteer from the booking

The data file should be updated as well

*Cancel volunteering
A Volunteer student should be allowed to cancel their availability.

Do not allow cancellation of slot that has already been booked by a student.

Do not allow cancellation of another volunteer’s booking.

The data file should be updated as well.



*_BONUS (optional)_
Only attempt the following if the team has completed all the above requirements. The requirements below are optional. There are no penalties if your team has not attempted these. However, it is to the team’s benefit if you do complete some of these.

It should be possible to have more than one configuration file. Figure out how to make this work for all tools in system without having to specify the configuration file as a command line argument for every tool.

If the 7 days of calendar data cannot fit on one screen, allow the user to scroll up and down.

Make the number of days of data to be a configurable; for example, download 10 days data instead of 7 days data.

Export the bookings in iCal file format so that it can be imported into a desktop calendar application.
