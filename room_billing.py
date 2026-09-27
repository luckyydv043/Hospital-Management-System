from datetime import datetime

# ==========================================
# ROOM MANAGEMENT
# ==========================================

def add_room(data, save_data):
    print("\n========== ADD ROOM ==========")

    room_number = input("Enter room number: ")
    room_type = input("Enter room type (General/Private/ICU): ")
    charge = float(input("Enter daily charge: ₹"))

    room = {
        "room_number": room_number,
        "type": room_type,
        "charge": charge,
        "occupied": False,
        "patient_id": None
    }

    data["rooms"].append(room)

    save_data(data)

    print("Room added successfully!")


def view_rooms(data):
    print("\n========== ROOM LIST ==========")

    if len(data["rooms"]) == 0:
        print("No rooms found.")
        return

    for room in data["rooms"]:

        print("\n----------------------------")
        print("Room Number :", room["room_number"])
        print("Type        :", room["type"])
        print("Charge      :", room["charge"])

        if room["occupied"]:
            print("Status      : Occupied")
            print("Patient ID  :", room["patient_id"])
        else:
            print("Status      : Available")


def assign_room(data, save_data):
    print("\n========== ASSIGN ROOM ==========")

    room_number = input("Enter room number: ")
    patient_id = int(input("Enter patient ID: "))

    patient_exists = False

    for patient in data["patients"]:

        if patient["id"] == patient_id:
            patient_exists = True
            break

    if not patient_exists:
        print("Patient not found.")
        return

    for room in data["rooms"]:

        if room["room_number"] == room_number:

            if room["occupied"]:
                print("Room is already occupied.")
                return

            room["occupied"] = True
            room["patient_id"] = patient_id

            save_data(data)

            print("Room assigned successfully.")
            return


    print("Room not found.")


def discharge_patient(data, save_data):
    print("\n========== DISCHARGE PATIENT ==========")

    room_number = input("Enter room number: ")

    for room in data["rooms"]:

        if room["room_number"] == room_number:

            if not room["occupied"]:
                print("Room is already available.")
                return

            room["occupied"] = False
            room["patient_id"] = None

            save_data(data)

            print("Patient discharged successfully.")
            return


    print("Room not found.")

# ==========================================
# BILLING
# ==========================================

def generate_bill(data, save_data):
    print("\n========== GENERATE BILL ==========")

    patient_id = int(input("Enter patient ID: "))


    patient_exists = False
    patient_name = ""


    for patient in data["patients"]:

        if patient["id"] == patient_id:

            patient_exists = True
            patient_name = patient["name"]
            break


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


    if data["bills"]:
        bill_id = max(
            bill["id"]
            for bill in data["bills"]
        ) + 1
    else:
        bill_id = 1


    bill = {
        "id": bill_id,
        "patient_id": patient_id,
        "doctor_charge": doctor_charge,
        "medicine_charge": medicine_charge,
        "room_charge": room_charge,
        "total": total,
        "date": datetime.now().strftime("%d-%m-%Y")
    }


    data["bills"].append(bill)

    save_data(data)


    print("\n")
    print("================================")
    print("        HOSPITAL BILL")
    print("================================")
    print("Bill ID        :", bill["id"])
    print("Patient ID     :", patient_id)
    print("Patient Name   :", patient_name)
    print("--------------------------------")
    print("Doctor Charge  : ₹", doctor_charge)
    print("Medicine Charge: ₹", medicine_charge)
    print("Room Charge    : ₹", room_charge)
    print("--------------------------------")
    print("TOTAL          : ₹", total)
    print("Date           :", bill["date"])
    print("================================")


def view_bills(data):
    print("\n========== BILL HISTORY ==========")

    if len(data["bills"]) == 0:
        print("No bills found.")
        return


    for bill in data["bills"]:

        print("\n----------------------------")
        print("Bill ID        :", bill["id"])
        print("Patient ID     :", bill["patient_id"])
        print("Doctor Charge  :", bill["doctor_charge"])
        print("Medicine Charge:", bill["medicine_charge"])
        print("Room Charge    :", bill["room_charge"])
        print("Test Charge    :", bill["test_charge"])
        print("Total          :", bill["total"])
        print("Date           :", bill["date"])