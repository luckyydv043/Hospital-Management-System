import json
from datetime import datetime

FILE_NAME = "hospital.json"

# =========================================================
#                    FILE HANDLING
# =========================================================

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {
            "patients": [],
            "doctors": [],
            "appointments": [],
            "medicines": [],
            "rooms": [],
            "bills": []
        }

    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
        return {
            "patients": [],
            "doctors": [],
            "appointments": [],
            "medicines": [],
            "rooms": [],
            "bills": []
        }

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

data = load_data()

# =========================================================
#                    PATIENT MANAGEMENT
# =========================================================

def add_patient():

    print("\n========== ADD PATIENT ==========")

    name = input("Enter patient name :")
    age = int(input("Enter age :"))
    gender = input("Enter gender :")
    phone = input("Enter phone number :")
    disease = input("Enter disease :")

    patient = {
        "id": len(data["patients"]) + 1,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "disease": disease
    }

    data["patients"].append(patient)
    save_data()
    print("\nPatient added successfully!")
    print("Patient ID:", patient["id"])

def view_patients():

    print("\n========== PATIENT LIST ==========")

    if len(data["patients"]) == 0:
        print("Patient not found")
        return

    for patient in data["patients"]:

        print("\n----------------------------")
        print("Patient ID :", patient["id"])
        print("Name       :", patient["name"])
        print("Age        :", patient["age"])
        print("Gender     :", patient["gender"])
        print("Phone      :", patient["phone"])
        print("Disease    :", patient["disease"])

def search_patient():

    print("\n========== SEARCH PATIENT ==========")

    patient_id = int(input("Enter patient ID: "))

    for patient in data["patients"]:

        if patient["id"] == patient_id:

            print("\nPatient Found!")
            print("----------------------------")
            print("ID       :", patient["id"])
            print("Name     :", patient["name"])
            print("Age      :", patient["age"])
            print("Gender   :", patient["gender"])
            print("Phone    :", patient["phone"])
            print("Disease  :", patient["disease"])

            return

    print("Patient not found.")

# =========================================================
#                    DOCTOR MANAGEMENT
# =========================================================


def add_doctor():

    print("\n========== ADD DOCTOR ==========")

    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    phone = input("Enter phone number: ")

    doctor = {
        "id": len(data["doctors"]) + 1,
        "name": name,
        "specialization": specialization,
        "phone": phone
    }

    data["doctors"].append(doctor)
    save_data()

    print("\nDoctor added successfully!")
    print("Doctor ID:", doctor["id"])


def view_doctors():

    print("\n========== DOCTOR LIST ==========")

    if len(data["doctors"]) == 0:
        print("No doctors found.")
        return

    for doctor in data["doctors"]:

        print("\n----------------------------")
        print("Doctor ID     :", doctor["id"])
        print("Name          :", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("Phone         :", doctor["phone"])


# =========================================================
#                    APPOINTMENT MANAGEMENT
# =========================================================

def book_appointment():

    patient_id = int(input("Enter Patient Id :"))
    doctor_id  = int(input("Enter doctor Id :"))
    date       = input("Enter date (DD-MM-YYYY): ")
    time       = input("Enter time (HH:MM): ")

    patient_exists = False 
    doctor_exists = False

    for patient in data["patients"]:
        if patient["id"] == patient_id:
            patient_exists = True

    for doctor in data["doctors"]:
        if doctor["id"] == doctor_id:
            doctor_exists = True

    if not patient_exists:
        print("Patient not found.")
        return

    if not doctor_exists:
        print("Doctor not found.")
        return 

    appointment = {
        "id"        : len(data["appointments"]) + 1,
        "patient_id": patient_id,
        "doctor_id" : doctor_id,
        "date"      : date,
        "time"      : time

    }

    data["appointments"].append(appointment)
    save_data()

    print("Appointment Booked Successfully")

def view_appointments():

    print("\n========== APPOINTMENTS ==========")

    if len(data["appointments"]) == 0:
        print("No appointments found.")
        return

    for appointment in data["appointments"]:

        print("\n----------------------------")
        print("Appointment ID:", appointment["id"])
        print("Patient ID    :", appointment["patient_id"])
        print("Doctor ID     :", appointment["doctor_id"])
        print("Date          :", appointment["date"])
        print("Time          :", appointment["time"])

# =========================================================
#                    MEDICINE MANAGEMENT
# =========================================================

def add_medicine():

    print("\n========== ADD MEDICINE ==========")

    name  = input("Enter medicine name :")
    price = float(input("Enter medicine price :"))
    stock = int(input("Enter stock :"))

    medicine = {
        "id"   : len(data["medicines"]) + 1,
        "name" : name,
        "price": price,
        "stock": stock
    }

    data["medicines"].append(medicine)
    save_data()

    print("\nMedicines Added Successfully")

def view_medicines():

    if data["medicines"] == 0:
        print("No Medicines Found")
        return
    
    for medicine in data["medicines"]:

        print("\n----------------------------")
        print("Medicine ID:", medicine["id"])
        print("Name       :", medicine["name"])
        print("Price      :", medicine["price"])
        print("Stock      :", medicine["stock"]) 

# =========================================================
#                    ROOM MANAGEMENT
# =========================================================

def add_room():

    print("\n========== ADD ROOM ==========")         
    room_number = int(input("Enter Room No. :"))
    room_type   = input("Enter Room Type :")
    charge      = int(input("Enter Daily Charge :"))

    room = {
        "room_number" : room_number,
        "type" : room_type,
        "charge" : charge,
        "occupied" : False,
        "patient_id" : None
    }

    data["rooms"].append(room)
    save_data()

    print(f"Room Added Successfully")

def view_rooms():

    print("\n========== ROOM LIST ==========")

    if len(data["rooms"]) == 0:
        print("No rooms found")
        return
    for room in data["rooms"]:

        print("Room Number:", room["room_number"])
        print("Type       :", room["type"])
        print("Charge     :", room["charge"])

        if room["occupied"]:
            print("Status     : Occupied")
            print("Patient Id :", room["patient_id"])

        else:
            print("Rooms Available")

def assign_room():
    print("\n========== ASSIGN ROOM ==========")

    room_number = int(input("Enter Room Number :"))
    patient_id = int(input("Enter Patient Id :"))

    for room in data["rooms"]:
        if room["room_number"] == room_number:
            if room["occupied"]:
                print("Rooms is occupied")
                return

        room["occupied"] = True
        room["patient_id"] = patient_id

        print("Room Assigned Successfully")
        return

    print("Room Not found")

def discharge_patient():
    print("\n========== DISCHARGE PATIENT ==========")

    room_number = int(input("Enter Room Number :"))

    for room in data["rooms"]:

        if room["room_number"] == room_number:

            if not room["occupied"]:
                print("Room is already available.")
                return

            room["occupied"] = False
            room["patient_id"] = None
            save_data()

            print("Patient Discharged Successfully.")
            return

    print("Room not found.")    


# =========================================================
#                    BILLING
# =========================================================

def generate_bills():

    print("\n========== GENERATE BILL ==========")

    patient_id = int(input("Enter patient ID: "))

    patient_exists = False

    for patient in data["patients"]:

        if patient["id"] == patient_id:
            patient_exists = True
            patient_name = patient["name"]

    if not patient_exists:
        print("Patient not found.")
        return

    doctor_charge = float(input("Doctor consultation charge: ₹"))
    medicine_charge = float(input("Medicine charge: ₹"))
    room_charge = float(input("Room charge: ₹"))

    total = (
        doctor_charge
        + medicine_charge
        + room_charge
    )

    bill = {
        "id": len(data["bills"]) + 1,
        "patient_id": patient_id,
        "doctor_charge": doctor_charge,
        "medicine_charge": medicine_charge,
        "room_charge": room_charge,
        "total": total,
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    data["bills"].append(bill)
    save_data()

    print("\n")
    print("================================")
    print("          HOSPITAL BILL")
    print("================================")
    print("Bill ID          :", bill["id"])
    print("Patient ID       :", patient_id)
    print("Patient Name     :", patient_name)
    print("--------------------------------")
    print("Doctor Charge    : ₹", doctor_charge)
    print("Medicine Charge  : ₹", medicine_charge)
    print("Room Charge      : ₹", room_charge)
    print("--------------------------------")
    print("TOTAL            : ₹", total)
    print("Date             :", bill["date"])
    print("================================")

def view_bills():

    print("\n========== BILL HISTORY ==========")

    if len(data["bills"]) == 0:
        print("No bills found.")
        return

    for bill in data["bills"]:

        print("\n----------------------------")
        print("Bill ID         :", bill["id"])
        print("Patient ID      :", bill["patient_id"])
        print("Doctor Charge   :", bill["doctor_charge"])
        print("Medicine Charge :", bill["medicine_charge"])
        print("Room Charge     :", bill["room_charge"])
        print("Total           :", bill["total"])
        print("Date            :", bill["date"])


# =========================================================
#                         MAIN 
# =========================================================

def main():
    while True:

        print("\n")
        print("==========================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("==========================================")
        print("1.  Add Patient")
        print("2.  View Patients")
        print("3.  Search Patient")
        print("------------------------------------------")
        print("4.  Add Doctor")
        print("5.  View Doctors")
        print("------------------------------------------")
        print("6.  Book Appointment")
        print("7.  View Appointments")
        print("------------------------------------------")
        print("8.  Add Medicine")
        print("9. View Medicines")
        print("------------------------------------------")
        print("10. Add Room")
        print("11. View Rooms")
        print("12. Assign Room")
        print("13. Discharge Patient")
        print("------------------------------------------")
        print("14. Generate Bill")
        print("15. View Bills")
        print("------------------------------------------")
        print("16. Exit")
        print("==========================================")

        choice = input("Enter Your Choice :")

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            add_doctor()

        elif choice == "5":
            view_doctors()

        elif choice == "6":
            book_appointment()

        elif choice == "7":
            view_appointments()

        elif choice == "8":
            add_medicine()

        elif choice == "9":
            view_medicines()

        elif choice == "10":
            add_room()

        elif choice == "11":
            view_rooms()

        elif choice == "12":
            assign_room()

        elif choice == "13":
            discharge_patient()

        elif choice == "14":
            generate_bills()

        elif choice == "15":
            view_bills()

        elif choice == "16":
            print("\nThank you for using Hospital Management System!")
            break

        else:
            print("Invalid Choice")

# =========================================================
#                    START PROGRAM
# =========================================================               
main()