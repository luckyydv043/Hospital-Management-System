# 🏥 Hospital Management System

A **Python-based Hospital Management System** designed to manage essential hospital operations such as patients, doctors, appointments, medicines, rooms, and billing.

This project is developed as a modular Python application using **3 functional modules and a main program**.

---

## 📌 Features

### 👨‍⚕️ Patient & Doctor Management

* Add new patients
* View patient details
* Update patient information
* Delete patient records
* Add doctor details
* View doctor details
* Manage doctor information

### 📅 Appointment & Medicine Management

* Schedule appointments
* View appointments
* Update appointment details
* Cancel appointments
* Add medicine records
* View medicine information
* Manage medicine details

### 🛏️ Room & Billing Management

* Manage hospital rooms
* Check room availability
* Allocate rooms
* Release rooms
* Generate bills
* View billing information

---

## 🗂️ Project Structure

```text
Hospital-Management-System/
│
├── main.py
├── patient_doctor.py
├── appointment_medicine.py
├── room_billing.py
│
├── hospital.json
├── README.md
├── PROJECT_REPORT.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## 🧩 Modules

### 1. `patient_doctor.py`

This module handles:

* Patient records
* Doctor records
* Adding patients and doctors
* Viewing records
* Updating records
* Deleting records

### 2. `appointment_medicine.py`

This module handles:

* Appointment scheduling
* Appointment records
* Medicine records
* Adding and viewing medicines
* Updating and managing appointments

### 3. `room_billing.py`

This module handles:

* Room management
* Room allocation
* Room availability
* Billing
* Bill generation and records

### 4. `main.py`

`main.py` acts as the **main entry point** of the application.

It:

* Imports the three modules
* Displays the main menu
* Allows the user to select different hospital operations
* Connects all modules together

---

## 💾 Data Storage

The project uses a JSON file for storing hospital data.

```text
hospital.json
```

JSON provides a simple and readable way to store:

* Patient data
* Doctor data
* Appointment data
* Medicine data
* Room data
* Billing data

---

## 🛠️ Technologies Used

* **Python 3**
* **JSON**
* **Git**
* **GitHub**
* **VS Code**

### Python Concepts Used

* Variables
* Data types
* Lists
* Dictionaries
* Functions
* Conditional statements
* Loops
* Modules
* File handling
* JSON
* Exception handling

---

## ▶️ How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/luckyydv043/Hospital-Management-System.git
```

### Step 2: Open the Project

```bash
cd Hospital-Management-System
```

### Step 3: Run the Program

```bash
python main.py
```

If your system uses `python3`, use:

```bash
python3 main.py
```

---

## 🧪 Testing

After cloning the project, run:

```bash
python main.py
```

Test the major functions:

1. Add a patient
2. View patient records
3. Add a doctor
4. View doctor records
5. Create an appointment
6. Add/view medicines
7. Manage rooms
8. Generate a bill
9. Exit the program

Verify that the information is correctly stored and retrieved from `hospital.json`.

---

## 🎯 Project Objectives

The main objectives of this project are:

* To develop a simple hospital management application.
* To practice Python programming concepts.
* To understand modular programming.
* To implement file handling and JSON data storage.
* To organize a Python project using multiple modules.
* To learn Git and GitHub version control.
* To create a practical real-world application.

---

## 🚀 Future Improvements

The project can be extended with:

* Login and authentication
* Admin and staff roles
* Database integration using MySQL or SQLite
* Graphical User Interface (GUI)
* Web-based interface
* Online appointment booking
* Patient search functionality
* Automated billing
* Medical history management
* Doctor availability tracking
* Report generation

---

## 👨‍💻 Author

**Student Project — VIT Bhopal**

Developed using Python as part of a programming/project assignment.

---

## 📄 License

This project is created for **educational purposes**.

