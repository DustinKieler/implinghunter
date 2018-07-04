'''
This script continuously scans the 'New' posts on reddit.com/r/2007scape for submissions that are related
to the location of a dragon or lucky impling. If the submission's title or text contains at least one specific
keyword from a related set, an e-mail will be sent via gmail to the user specified in authentication.py.
Created by Dustin Kieler | /u/Chassy13 on July 3rd, 2018.
'''

import authentication
import configparser
import praw
import smtplib
from email.mime.text import MIMEText

# These keywords should all be lowercase only.
keywords = ['impling', 'dragon imp', 'drag imp', 'drg imp', 'dr imp', 'd imp', 'l imp', 'luck imp', 'lucky imp']


# Since we are just reading the New posts, we will create a Read-Only instance rather than
# using our own account or creating an account specifically for the bot.
# We do not need to use an infinite loop because the PRAW API will continuously grab the streamed submissions by itself.
def main():
    """Logs into Reddit in read-only mode and begins searching the 'New' posts of /r/2007scape
       for submissions related to dragon and lucky implings."""
    reddit = praw.Reddit(client_id="YOUR_APP_CLIENT_ID",
                         client_secret="YOUR_APP_CLIENT_SECRET",
                         user_agent="YOUR_UNIQUE_USER_AGENT_STRING")
    authentication.create_config()
    print("Now waiting patiently for implings...")
    for submission in reddit.subreddit('2007scape').stream.submissions():
        process_submission(submission)
    # Eventually should do proper error handling?
    print("Submission loop has been terminated - restart needed.")


# We could compare the submission.created_utc time to time.time() if we wanted to only get posts that were created after
# we started running this script, but it's probably worth grabbing up to the last 25 submissions that may contain info
# about an impling because the submission may not have been seen yet.
def process_submission(submission):
    """Searches a submission title and text for keywords related to dragon and lucky implings.
       If a keyword is a match, calls to create and send an e-mail."""
    for keyword in keywords:
        if keyword in submission.title.lower() or keyword in submission.selftext.lower():
            email = create_email(submission.title, submission.selftext)
            send_notification_email(email)


def send_notification_email(email):
    """Establishes the mail server and sends the e-mail to the address specified in the configuration."""
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email['From'], get_credential('Key'))
    server.sendmail(email['From'], email['To'], email.as_string())
    server.quit()
    print("E-mail sent!")


def create_email(sub_title, sub_text):
    """Creates an e-mail containing the impling post's title and text.
       The TO and FROM fields are the e-mail address in the configuration."""
    msg = MIMEText("Title: " + sub_title + "\n" + "Text: " + sub_text)
    address = get_credential('Address')
    msg['Subject'] = 'POTENTIAL IMPLING ALERT'
    msg['From'] = address
    msg['To'] = address
    return msg


# There is probably a cleaner way to do this in the future if we ever wanted to retrieve more properties,
# such as opening the configparser just one time and then passing along the property and/or tag to allow for more
# general use.
def get_credential(tag):
    """Searches the [CREDENTIALS] in the configuration for a specific property (tag)."""
    config = configparser.ConfigParser()
    config.read('auth.ini')
    return config['CREDENTIALS'][tag]


if __name__ == '__main__':
    main()

