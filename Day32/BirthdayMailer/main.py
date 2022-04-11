from os import listdir
from os.path import isfile, join
import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "email_goes_here"
MY_PASSWORD = "password_goes_here"


def prepare_letter(prsn_details):
    # ------- Get Letter Template ---------
    file_dir = "letter_templates"
    letter_templates = [join(file_dir, file) for file in listdir(file_dir) if isfile(join(file_dir, file))]

    curr_template_file_name = random.choice(letter_templates)

    with open(curr_template_file_name) as curr_template_file:
        curr_template = curr_template_file.read()
    new_letter = curr_template.replace("[NAME]", prsn_details["name"])
    return new_letter


def send_email(email_content, email_addrs):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email_addrs,
                            msg=f"Subject:Happy Birthday!!\n\n"
                                f"{email_content}")
    print(f"Message to {email_addrs} has been sent!")


def send_card(prsn_details):
    email_addrs = prsn_details.email
    letter = prepare_letter(prsn_details)
    send_email(letter, email_addrs)


# ------- Check for any birthdays today -------
today = dt.date.today()
birthdays = pandas.read_csv("birthdays.csv")

for index, row in birthdays.iterrows():
    prsn_birthdate = dt.date(year=row.year, month=row.month, day=row.day)
    if prsn_birthdate.month == today.month and prsn_birthdate.day == today.day:
        send_card(row)
