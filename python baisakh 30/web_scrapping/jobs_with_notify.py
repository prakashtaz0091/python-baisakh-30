import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import smtplib

import plyer
# import notify2

target_url = "https://www.jobsnepal.com/"
response = requests.get(target_url)

datetime_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
output_filename = f"./outputs/jobs-{datetime_now}.csv"

looking_for = [
    "python",
    "react",
    "teacher",
    "developer",
    "designer",
]


def send_mail(subject, message):
    # creates SMTP session
    s = smtplib.SMTP("localhost", 1025)
    # message to be sent
    msg = f"Subject: {subject}\n\n{message}"
    # sending the mail
    s.sendmail("jobs@localhost", "sarthak@localhost", msg)
    # terminating the session
    s.quit()

    # use this incase of testing/using with your personal account
    # s = smtplib.SMTP("smtp.gmail.com", 587)
    # s.starttls()
    # s.login("jobs@localhost", "password")
    # s.sendmail("jobs@localhost", "sarthak@localhost", msg)
    # s.quit()


if response.status_code == 200:
    print("Request Success!")
    content = response.text
    soup = BeautifulSoup(content, "html.parser")
    # site_title = soup.find("title")
    # print(site_title.get_text())
    # all_links = soup.find_all("link")
    # # print(all_links)
    # for link in all_links:
    #     print(link)
    jobs = soup.find_all("div", class_="card-body")
    # print(jobs)
    # test = jobs[0]
    # print(test.find("h3", class_="job-company").get_text().strip())
    job_data = []
    for job in jobs:
        # extract data
        job_title = job.find("h2", class_="job-title").get_text().strip()
        job_company = job.find("h3", class_="job-company").get_text().strip()
        job_location = job.find("span", class_="location").get_text().strip()

        # prepare data to save
        new_job = [job_title, job_company, job_location]
        job_data.append(new_job)

        print(job_title)
        # send notification
        for keyword in looking_for:
            if keyword in job_title.lower():
                print("Job Found!")
                message = f"""
                Title: {job_title}
                Company: {job_company}
                Location: {job_location}
                """
                send_mail(
                    "Job Found!",
                    message=message,
                )
                # plyer.notification.notify(
                #     title="Job Found!",
                #     message=f"Title: {job_title}\nCompany: {job_company}\nLocation: {job_location}",
                #     timeout=10,
                # )
                # n = notify2.Notification(
                #     "Summary",
                #     "Some body text",
                #     "notification-message-im",  # Icon name
                # )
                # n.show()

        # print("-----------------------------------------------")
        # print(f"Title: {job_title}")
        # print(f"Company: {job_company}")
        # print(f"Location: {job_location}")

    with open(output_filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location"])
        writer.writerows(job_data)

else:
    print("Something went wrong!")
