from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import find_dotenv, load_dotenv
import time

title_text = "Python and Web Developer"

description_text = """Hello! I am a 16 year old python developer from US that is looking for a career in AI and Machine Learning. I am here because I want to gain experience and refine my skills in the python programming language, as well as making money on the side for my struggling family. 

My skills include:
General Python Programming
SciKit Learn
PyTorch
Ollama python module
Tkinter
Flask
HTML
CSS
JavaScript

If you are interested, check my portfolio or DM me!
https://architect.crateris.net/

⚠️I am only interested in contract jobs, not partnerships or full time jobs. DO NOT message me if you don't have a job⚠️

I am currently a student and athlete so it may take me a while to get back to you. Just a heads up!"""

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get("https://discord.com/")

credentials_path = find_dotenv()
load_dotenv(credentials_path)

username = os.getenv("discord_username")
password = os.getenv("discord_password")

login_link = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[@class='menu-button-login login-button-js abc hide-on-mobile']")))
login_link.click()

username_input = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='uid_14']")))
password_input = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[@id='uid_16']")))
login_button = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "//*[@class='buttonChildrenWrapper_a22cb0']")))

username_input.send_keys(username)
password_input.send_keys(password)
login_button.click()

def inputProcess():
    new_post_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'New Post')]")))
    new_post_button.click()

    title = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='title_d9be46 heading-lg/semibold_d9be46']")))
    title.send_keys(title_text)

    desc = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@class='markup__75297 editor__1b31f slateTextArea_ec4baf textAreaForPostCreation__74017']")))
    desc.send_keys(description_text)

    post_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Post')]")))
    post_button.click()


job_cord_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-list-item-id, '1116994814349688875')]")))

job_cord_button.click()


show_your_work_JobCord = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '🧐show-your-work')]")))
show_your_work_JobCord.click()
inputProcess()


connectify_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-list-item-id, '1041086031165915177')]")))
connectify_button.click()


post_paid_jobs_connectify = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'post-paid-jobs')]")))
post_paid_jobs_connectify.click()
inputProcess()
post_unpaid_jobs_connectify = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'post-unpaid-jobs')]")))
post_unpaid_jobs_connectify.click()
inputProcess()
opportunity_connectify = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'opportunity')]")))
opportunity_connectify.click()
inputProcess()
hire_me_connectify = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'hire-me')]")))
hire_me_connectify.click()
inputProcess()

CodeSupport_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-list-item-id, '240880736851329024')]")))
CodeSupport_button.click()

hiring_or_looking = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'hiring-or-looking')]")))
hiring_or_looking.click()
inputProcess()
python_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-list-item-id, '1013064902472126494')]")))
python_tag.click()
looking_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-list-item-id, '1013064275314606080')]")))
looking_tag.click()
temporary_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-list-item-id, '1013064383208882228')]")))
temporary_tag.click()
javascript_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-list-item-id, '1013063909156073493-post-form-tags-navigator___forum-tag-1013064680740245574')]")))
javascript_tag.click()
html_tag = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@data-list-item-id, '1013063909156073493-post-form-tags-navigator___forum-tag-1013064815515807848')]")))
html_tag.click()


breakpoint()