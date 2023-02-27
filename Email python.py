# Import an SMTP client session object library
import smtplib

# Prompt the user for their email address and password
sender_email = input("Enter your email address: ")
password = input("Enter your password: ")

# Prompt the user for the recipient email address, subject, and body of the email
recipient_email = input("Enter the recipient email address: ")
subject = input("Enter the email subject: ")
body = input("Enter the email body: ")

# Construct the email message
message = f"Subject: {subject}\n\n{body}"

# Connect to the SMTP server and send the email
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, recipient_email, message)
    
# Display a success message to the user on the command prompt
print("Email sent successfully!")
