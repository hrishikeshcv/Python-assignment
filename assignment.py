import argparse
 
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
DELAY = 10
 
 
def parse_command_line_arguments():
    arg_parser = argparse.ArgumentParser(
        description="Provide the public link to the Netflix title"
    )
    arg_parser.add_argument(
        "--link",
        default="",
        type=str,
        required=True
    )
    netflix_link_str = arg_parser.parse_args().link
    return str(netflix_link_str).strip()
 
 
def get_web_driver():
    service = Service("C:\Program Files (x86)\chromedriver.exe")                             # replace the path by your chromedriver path
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver_wait = WebDriverWait(driver, DELAY)
    return driver, driver_wait
 
 
def get_str_from_web_element_by_class_name(class_name):
    return str(source_driver.find_element(
        by=By.CLASS_NAME,
        value=class_name
    ).text)
 
 
netflix_link = parse_command_line_arguments()
source_driver, source_wait = get_web_driver()

source_driver.get(netflix_link)

print(
    "Cast: {}".format(
        get_str_from_web_element_by_class_name("title-data-info-item-list")
    )
)
print(
    "Description: {}".format(
        get_str_from_web_element_by_class_name("title-info-synopsis")
    )
)
 
try:
    trailer_web_element = source_wait.until(
        EC.element_to_be_clickable(
            (
                By.CLASS_NAME,
                "additional-video"
            )
        )
    )
    if trailer_web_element:
        trailer_web_element.click()
except TimeoutException as exc:
    print("Error: Trailer does not exist for this title")

    #https://www.netflix.com/in/browse/genre/839338 - browse the title links from here [ctrl+click]
   
   #instructions to run - pass "python <filename> --link <link of the title>"
