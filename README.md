# Hospital-Management-System
A Python CLI-based Hospital Management System using JSON for managing patients, doctors, appointments, medicines, rooms, and billing.
A command-line based Hospital Management System developed using Python. The project uses JSON for data storage and provides basic management features for patients, doctors, appointments, medicines, rooms, and bills.

## Features

* Add and view patients
* Search patients by ID
* Delete patients
* Add and view doctors
* Book and view appointments
* Add and view medicines
* Add and view hospital rooms
* Assign rooms to patients
* Discharge patients from rooms
* Generate and view bills
* Persistent data storage using JSON
* Command-line interface

## Technologies Used

* Python 3
* JSON
* Python `json` module
* Python `datetime` module

## Project Structure

```text
Hospital-Management-System/
│
├── hospital_management.py
├── hospital.json
├── README.md
├── requirements.txt
└── PROJECT_REPORT.md
```

## Requirements

Before running the project, make sure Python 3 is installed on your computer.

Check your Python installation:

```bash
python --version
```

or, on some systems:

```bash
python3 --version
```

Python 3.8 or later is recommended.

## Installation

### Step 1: Clone the repository

Open a terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/Hospital-Management-System.git
```

Replace `YOUR-USERNAME` with your GitHub username.

### Step 2: Enter the project directory

```bash
cd Hospital-Management-System
```

### Step 3: Create a virtual environment

Windows:

```bash
python -m venv venv
```

Linux/macOS:

```bash
python3 -m venv venv
```

### Step 4: Activate the virtual environment

Windows Command Prompt:

```bash
venv\Scripts\activate
```

Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Step 5: Install dependencies

This project uses only Python standard-library modules, so no external packages are required.

You can run:

```bash
pip install -r requirements.txt
```

## Configuration

No additional configuration or API keys are required.

The project stores its data in:

```text
hospital.json
```

If the JSON file does not exist, the application automatically creates the required data structure when it starts.

## Running the Project

Run the following command from the project directory:

Windows:

```bash
python hospital_management.py
```

Linux/macOS:

```bash
python3 hospital_management.py
```

The application will open a command-line menu.

## Usage

After starting the program, select an option from the menu.

For example:

```text
1. Add Patient
2. View Patients
3. Search Patient
4. Delete Patient
...
```

Enter the corresponding number and follow the instructions displayed in the terminal.

## Data Storage

All application data is stored locally in `hospital.json`.

The JSON file contains separate sections for:

* Patients
* Doctors
* Appointments
* Medicines
* Rooms
* Bills

The application loads the existing data when it starts and saves changes whenever records are added, modified, or deleted.

## Example Workflow

A typical workflow can be:

1. Add a doctor.
2. Add a patient.
3. Book an appointment between the patient and doctor.
4. Add medicines to the system.
5. Add hospital rooms.
6. Assign an available room to a patient.
7. Generate a bill.
8. View the stored records.

## Troubleshooting

### Python command not found

If `python` is not recognized, make sure Python is installed and added to your system PATH.

Try:

```bash
python3 --version
```

### JSON file error

Make sure `hospital.json` contains valid JSON data. If the file is corrupted, restore it to a valid JSON structure or remove it and restart the application.

## Future Improvements

Possible future improvements include:

* User authentication
* Improved input validation
* Appointment conflict checking
* Automatic bill calculation
* Medicine stock updates
* More detailed reports
* Exporting records
* Improved command-line interface

## Author

Developed as a Python project for learning and demonstrating file handling, JSON, functions, lists, dictionaries, loops, conditions, and command-line programming.
