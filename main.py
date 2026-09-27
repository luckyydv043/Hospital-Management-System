import json

import patient_doctor
import appointment_medicine
import room_billing
# ==========================================
# FILE HANDLING
# ==========================================

FILE_NAME = "hospital.json"

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

def save_data(data):

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Load hospital data
data = load_data()

# ==========================================
# MAIN MENU
# ==========================================

def main():

    while True:

        print("\n")
        print("==========================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("==========================================")

        print("1.  Add Patient")
        print("2.  View Patients")
        print("3.  Search Patient")
        print("4.  Delete Patient")
        print("------------------------------------------")
        print("5.  Add Doctor")
        print("6.  View Doctors")
        print("------------------------------------------")
        print("7.  Book Appointment")
        print("8.  View Appointments")
        print("------------------------------------------")
        print("9.  Add Medicine")
        print("10. View Medicines")
        print("------------------------------------------")
        print("11. Add Room")
        print("12. View Rooms")
        print("13. Assign Room")
        print("14. Discharge Patient")
        print("------------------------------------------")
        print("15. Generate Bill")
        print("16. View Bills")
        print("------------------------------------------")

        print("17. Exit")

        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_doctor.add_patient(data, save_data)

        elif choice == "2":

            patient_doctor.view_patients(data)

        elif choice == "3":

            patient_doctor.search_patient(data)

        elif choice == "4":

            patient_doctor.delete_patient(data, save_data)


        elif choice == "5":

            patient_doctor.add_doctor(data, save_data)

        elif choice == "6":

            patient_doctor.view_doctors(data)

        elif choice == "7":

            appointment_medicine.book_appointment(data, save_data)
        elif choice == "8":

            appointment_medicine.view_appointments(data)


        elif choice == "9":

            appointment_medicine.add_medicine(data, save_data)

        elif choice == "10":

            appointment_medicine.view_medicines(data)


        elif choice == "11":

            room_billing.add_room(data, save_data)

        elif choice == "12":

            room_billing.view_rooms(data)

        elif choice == "13":

            room_billing.assign_room(data, save_data)

        elif choice == "14":

            room_billing.discharge_patient(data, save_data)

        elif choice == "15":

            room_billing.generate_bill(data, save_data)

        elif choice == "16":

            room_billing.view_bills(data)

        elif choice == "17":
            print("\nThank you for using "
                "Hospital Management System!")
            break

        else:
            print("\nInvalid choice. ""Please try again.")

# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
