from selenium import webdriver
from selenium.webdriver.common.by import By


def programs_data():
    # Create a dictionary to store the program information
    return {
        1: {"name": "BA (Hons) in English", "total_credit": 138, "total_semester": 12, "duration": 4},
        2: {"name": "BSS (Hons) in Sociology", "total_credit": 136, "total_semester": 12, "duration": 4},
        3: {"name": "BSS (Hons) in Journalism & Media Communication", "total_credit": 129, "total_semester": 12, "duration": 4},
        4: {"name": "Bachelor of Business Administration", "total_credit": 129, "total_semester": 12, "duration": 4},
        5: {"name": "BSc in Computer Science & Engineering (CSE-Regular)", "total_credit": 144, "total_semester": 12, "duration": 4},
        6: {"name": "BSc in Computer Science & Engineering (CSE-Weekend)", "total_credit": 130.5, "total_semester": 10, "duration": 3.4},
        7: {"name": "BSc in Electrical and Electronic Engineering (EEE-Regular)", "total_credit": 144, "total_semester": 12, "duration": 4},
        8: {"name": "BSc in Electrical and Electronic Engineering (EEE-Weekend)", "total_credit": 130.5, "total_semester": 10, "duration": 3.4},
        9: {"name": "BSc in Textile Engineering (Regular)", "total_credit": 161, "total_semester": 12, "duration": 4},
        10: {"name": "BSc in Textile Engineering (Weekend)", "total_credit": 134, "total_semester": 10, "duration": 3.4},
        11: {"name": "LLB (Hons)", "total_credit": 129, "total_semester": 12, "duration": 4},
    }


def fetch_data(student_id, password, program_id, render_template):
    # Create a ChromeOptions object to set the headless flag
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Create a ChromeDriver instance with the headless flag set
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the login page
    driver.get("https://studentportal.green.edu.bd/Account/Login")

    # Find the element for the student ID field and enter the student ID
    student_id_field = driver.find_element(
        By.XPATH, '//*[@id="Input_LoginId"]')
    student_id_field.send_keys(student_id)

    # Find the element for the password field and enter the password
    password_field = driver.find_element(
        By.XPATH, '//*[@id="Input_Password"]')
    password_field.send_keys(password)

    # Find the login button and click it
    login_button = driver.find_element(
        By.XPATH, '//*[@id="account"]/div[4]/button')
    login_button.click()

    # Check if the password was incorrect
    password_error = driver.find_elements(
        By.XPATH, '//*[@id="account"]/div[3]/span')

    if len(password_error) > 0:
        # The password was incorrect
        # Render the template with an error message
        return render_template("index.html", programs=programs_data(), error="Incorrect password")

    # Navigate to the URL for the student course history page
    driver.get(
        "https://studentportal.green.edu.bd/Student/StudentCourseHistory")

    # Find the table element using the provided XPath
    table = driver.find_element(
        By.XPATH, '/html/body/div/main/div[2]/div/section/div[2]/div/div/div/table')

    # Find all of the rows in the table
    rows = table.find_elements(By.XPATH, './tbody/tr')

    # Initialize a variable to store the total credit completed
    total_credit = 0
    total_semeseter_completed = 0

    # Iterate over the rows
    for row in rows:
        # Find all of the cells in the row
        cells = row.find_elements(By.XPATH, './td')

        # Get the text of the 6th cell (index 5) and add it to the total credit
        total_credit += float(cells[5].text)
        total_semeseter_completed += 1

    # Get the program information from the programs dictionary
    program = programs_data()[program_id]

    # Calculate the number of semesters left until graduation
    semesters_left = program["total_semester"] - \
        (total_credit / program["total_credit"]
         * program["total_semester"])

    # Calculate the number of credits left to complete
    credits_left = program["total_credit"] - total_credit

    running_sememster = total_semeseter_completed + 1

    # Render the template with the calculated values
    return render_template("programs.html", total_semeseter_completed=total_semeseter_completed, running_sememster=running_sememster, total_credit=total_credit, semesters_left=semesters_left, credits_left=credits_left)
