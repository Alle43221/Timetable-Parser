# Timetable Parser

This Python-based project allows students at **Universitatea Babeș-Bolyai (UBB)** to easily convert their university timetable, which is published as an HTML file, into an `.ics` calendar file. This file can then be imported into Google Calendar or other calendar management applications, making it easy to keep track of lectures, seminars, and labs.

## Features

- Parses the university timetable from a provided HTML file.
- Converts the timetable into an `.ics` file compatible with most calendar apps.
- Customizable fields for easy modification by users.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/UBB-timetable-parser.git
    cd UBB-timetable-parser
    ```

2. **Install dependencies**:
    You may need some Python packages such as `ics`, `requests`, `beautifulsoup4`, etc. Install them using:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

### Step 1: Modify User-Specific Fields

Before running the script, you need to edit the following variables in the **`timetable_parser.py`** file to match your specific timetable setup:

```python
#------------------------USER EDIT ZONE---------------------------

url = "https://www.cs.ubbcluj.ro/files/orar/2024-1/tabelar/I2.html"  # URL of your timetable (HTML)
start_of_semester = datetime.datetime(year=2024, month=9, day=30)     # Start date of your semester
end_of_semester = datetime.datetime(year=2025, month=1, day=19)       # End date of your semester
timezone_adjustment = -3                                              # Timezone offset (e.g., -3 for UTC+3)
file_name = "timetable"                                               # Name of the output .ics file

#------------------------USER EDIT ZONE---------------------------
```

#### Explanation of Fields:
- **`url`**: The URL of your university timetable in HTML format. You can find this on the UBB website for your specific course/year.
- **`start_of_semester`**: The exact start date of your semester (e.g., the first day of classes).
- **`end_of_semester`**: The last day of your semester, including exams if necessary.
- **`timezone_adjustment`**: The difference in hours between your local time and UTC (e.g., `-3` for UTC+3).
- **`file_name`**: The desired name of the output `.ics` file.

### Step 2: Run the Script

After setting the correct fields, run the script, and it will download your timetable, parse it, and generate an `.ics` file in the project directory.

```bash
python timetable_parser.py
```

This will create an `ics` file (e.g., `timetable.ics`), which you can then import into Google Calendar or any other calendar application.

## Importing the .ICS File

1. **Google Calendar**:
   - Go to Google Calendar.
   - Click on the "gear" icon at the top-right corner and select "Settings".
   - On the left sidebar, find and click "Import & export".
   - Click "Select file from your computer" and choose the `.ics` file you generated.
   - Click "Import" and your timetable will appear in your calendar.

2. **Other Calendar Apps**:
   - Most calendar applications (Apple Calendar, Outlook, etc.) also support `.ics` file imports. Look for a similar import feature and upload your generated `.ics` file.

## License

This project is licensed under the MIT License.

---

This should provide clear guidance on what the project does and how users can modify it to work for their specific situation. Let me know if you'd like to tweak any part!
