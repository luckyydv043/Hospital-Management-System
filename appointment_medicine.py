# ==========================================
# APPOINTMENT MANAGEMENT
# ==========================================

def book_appointment(data, save_data):
    print("\n========== BOOK APPOINTMENT ==========")

    # Show available patients
    if not data["patients"]:
        print("No patients available.")
        return

    print("\nAvailable Patients:")
    print("------------------------------------------")

    for patient in data["patients"]:
        print(
            "ID:", patient["id"],
            "| Name:", patient["name"],
            "| Age:", patient["age"]
        )

    print("------------------------------------------")

    patient_id = int(input("Enter patient ID: "))

    patient_exists = False

    for patient in data["patients"]:

        if patient["id"] == patient_id:
            patient_exists = True
            break

    if not patient_exists:
        print("Patient not found.")
        return


    # Show available doctors
    if not data["doctors"]:
        print("No doctors available.")
        return

    print("\nAvailable Doctors:")
    print("------------------------------------------")

    for doctor in data["doctors"]:
        print(
            "ID:", doctor["id"],
            "| Name:", doctor["name"],
            "| Specialization:", doctor["specialization"]
        )

    print("------------------------------------------")

    doctor_id = int(input("Enter doctor ID: "))

    doctor_exists = False

    for doctor in data["doctors"]:

        if doctor["id"] == doctor_id:
            doctor_exists = True
            break

    if not doctor_exists:
        print("Doctor not found.")
        return


    date = input("Enter date (DD-MM-YYYY): ")
    time = input("Enter time (HH:MM): ")


    if data["appointments"]:
        appointment_id = max(
            appointment["id"]
            for appointment in data["appointments"]
        ) + 1
    else:
        appointment_id = 1


    appointment = {
        "id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date,
        "time": time
    }

    data["appointments"].append(appointment)

    save_data(data)

    print("\nAppointment booked successfully!")
    print("Appointment ID:", appointment_id)


def view_appointments(data):
    print("\n========== APPOINTMENTS ==========")

    if len(data["appointments"]) == 0:
        print("No appointments found.")
        return

    for appointment in data["appointments"]:

        print("\n----------------------------")
        print("Appointment ID :", appointment["id"])
        print("Patient ID     :", appointment["patient_id"])
        print("Doctor ID      :", appointment["doctor_id"])
        print("Date           :", appointment["date"])
        print("Time           :", appointment["time"])


# ==========================================
# MEDICINE MANAGEMENT
# ==========================================

def add_medicine(data, save_data):
    print("\n========== ADD MEDICINE ==========")

    name = input("Enter medicine name: ")
    price = float(input("Enter medicine price: ₹"))
    stock = int(input("Enter stock quantity: "))


    if data["medicines"]:
        medicine_id = max(
            medicine["id"]
            for medicine in data["medicines"]
        ) + 1
    else:
        medicine_id = 1


    medicine = {
        "id": medicine_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    data["medicines"].append(medicine)

    save_data(data)

    print("\nMedicine added successfully!")
    print("Medicine ID:", medicine_id)


def view_medicines(data):
    print("\n========== MEDICINE STOCK ==========")

    if len(data["medicines"]) == 0:
        print("No medicines found.")
        return

    for medicine in data["medicines"]:

        print("\n----------------------------")
        print("Medicine ID :", medicine["id"])
        print("Name        :", medicine["name"])
        print("Price       :", medicine["price"])
        print("Stock       :", medicine["stock"])