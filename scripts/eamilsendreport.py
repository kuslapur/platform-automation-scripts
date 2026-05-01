import smtplib
from email.message import EmailMessage

# Email config
sender_email = "bkuslapur@gmail.com"
receiver_email = "buslapur@gmail.com"
app_password = "Jan@2026"   # NOT your normal password

zip_filename = "github_repo_report_20260419.zip"

# Create email
msg = EmailMessage()
msg["Subject"] = "GitHub Repo Report"
msg["From"] = sender_email
msg["To"] = receiver_email
msg.set_content("Hi,\n\nPlease find the attached GitHub repo report.\n\nThanks")

# Attach ZIP file
with open(zip_filename, "rb") as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="zip", filename=zip_filename)

# Send email using Gmail SMTP
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("Email sent successfully!")