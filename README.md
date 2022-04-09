# implinghunter
This script continuously scans the 'New' posts on reddit.com/r/2007scape for submissions that are related to the location of a dragon or lucky impling. If the submission's title or text contains at least one specific keyword from a related set, an e-mail will be sent via the gmail SMTP server to the user specified in authentication.py.

First, you will need Python and PRAW installed.

To run the script in read-only mode, you will need to fill in the PRAW credentials required in main() in 2007scapeimpsearcher.py. You can create these credentials by going to your Reddit account settings and creating an app for development there, where you will receive a client_id and client_secret for the app you created. The user_agent needs to be a unique key that Reddit uses to see who is accessing their API. For example, you could do something like user_agent="impling reader for /r/2007scape by YOUR_NAME."

To receive the e-mail, you will need to edit authentication.py with your gmail address and **app** password. When you run the script, these will be saved to an 'auth.ini' file which will be read when the e-mail needs to be sent. This will require that you have sufficient security on your associated Google account and you have set up an app password.
