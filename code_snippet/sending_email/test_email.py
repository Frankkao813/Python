# coding=utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from string import Template
from pathlib import Path
import time
import pandas as pd


# send email
def send_email(indi_email, indi_user, indi_time_slot, indi_total, indi_show_time):
    content = MIMEMultipart()
    content["subject"] = "半導體戶外教學 - 報名成功暨注意事項通知"
    content["from"] = "franklinkao813@gmail.com"
    content["to"] = indi_email
    template = Template(Path("success_template.html").read_text(encoding="'utf-8'"))
    body = template.substitute({"name": indi_user, "time_slot": indi_time_slot, "total_people": indi_total, "show_time": indi_show_time})
    content.attach(MIMEText(body, "html"))
    smtp.send_message(content)

# read file using pandas, then extract the useful column into list format
# csv file is not uploaded to protect privacy
def read_csv_extract_rows(filePath):
    student_info = pd.read_csv(filePath)
    num_student = len(student_info)
    temp_email_list = student_info["email"].tolist()
    temp_user = student_info["name"].tolist()
    temp_user_total = student_info["total_people"].tolist()
    temp_time_slot = student_info["time_slot"].tolist()
    temp_show_time = student_info["show_time"].tolist()
    return num_student, temp_email_list, temp_user, temp_user_total,temp_time_slot, temp_show_time
# import pandas and extract it as mail list

num_student, email_list, user, user_total, time_slot, show_time = read_csv_extract_rows("group_2.csv")
print(num_student)

# sending email - function "send_email" is utilized
with smtplib.SMTP(host = "smtp.gmail.com", port = "587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("franklinkao813@gmail.com", "") # the second parameter: application needed
    for i in range(num_student):
        try:
            send_email(email_list[i], user[i], time_slot[i], user_total[i], show_time[i])
            print("成功傳送")
            time.sleep(0.2)

        except Exception as e:
            print("Error message: ", e)

