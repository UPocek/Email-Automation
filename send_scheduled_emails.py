import smtplib
from email.message import EmailMessage
import schedule
import time


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = "myprojects01email@gmail.com"

    user = "myprojects01email@gmail.com"
    password = "zkneesqgezcpzuof"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


if __name__ == '__main__':
    # samo stavim vreme koje zelim (kao i naslov, body i mail_to)
    schedule.every().day.at("02:51").do(email_alert, "TEST", "Ovo je test", "uros.pocek@gmail.com")
    while True:
        schedule.run_pending()
        # broj sekundi izmedju 2 provere
        time.sleep(30)
