import smtplib
import datetime as dt
from random import choice
from secrets import email_accounts, addresses


def send_email(message, subject, account_in, email_address):
    """
    :param email_address: Target address
    :param message: Don't forget subject:*subject*\n\n*body*
    :param account_in: yahoo or gmail
    :return:
    """
    accounts = email_accounts

    account = accounts[account_in]

    with smtplib.SMTP(account["smtp"]) as connection:
        connection.starttls()
        connection.login(user=account["email"], password=account["pass"])
        connection.sendmail(from_addr=account["email"],
                            to_addrs=email_address,
                            msg=f"Subject:{subject}\n\n{message}")


def get_quote():
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
        return choice(quotes).replace("-", "\n-")


now = dt.datetime.now()
address_book = addresses
if now.weekday() == 4:
    for person in address_book:
        send_email(message=f"{get_quote()}", subject="It's Friday, my dudes. Be inspired?.",
                   account_in="gmail", email_address=person)
