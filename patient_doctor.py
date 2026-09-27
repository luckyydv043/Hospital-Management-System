# ==========================================
# PATIENT MANAGEMENT
# ==========================================

def add_patient(data, save_data):
    print("\n========== ADD PATIENT ==========")

    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    phone = input("Enter phone number: ")
    disease = input("Enter disease/problem: ")

    if data["patients"]:
        patient_id = max(
            patient["id"] for patient in data["patients"]
        ) + 1
    else:
        patient_id = 1

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "disease": disease
    }

    data["patients"].append(patient)
    save_data(data)

    print("\nPatient added successfully!")
    print("Patient ID:", patient["id"])


def view_patients(data):
    print("\n========== PATIENT LIST ==========")

    if len(data["patients"]) == 0:
        print("No patients found.")
        return

    for patient in data["patients"]:

        print("\n----------------------------")
        print("Patient ID :", patient["id"])
        print("Name       :", patient["name"])
        print("Age        :", patient["age"])
        print("Gender     :", patient["gender"])
        print("Phone      :", patient["phone"])
        print("Disease    :", patient["disease"])


def search_patient(data):
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


# ==========================================
# DOCTOR MANAGEMENT
# ==========================================

def add_doctor(data, save_data):
    print("\n========== ADD DOCTOR ==========")

    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")
    phone = input("Enter phone number: ")

    if data["doctors"]:
        doctor_id = max(
            doctor["id"] for doctor in data["doctors"]
        ) + 1
    else:
        doctor_id = 1

    doctor = {
        "id": doctor_id,
        "name": name,
        "specialization": specialization,
        "phone": phone
    }

    data["doctors"].append(doctor)

    save_data(data)

    print("\nDoctor added successfully!")
    print("Doctor ID:", doctor["id"])


def view_doctors(data):
    print("\n========== DOCTOR LIST ==========")

    if len(data["doctors"]) == 0:
        print("No doctors found.")
        return

    for doctor in data["doctors"]:

        print("\n----------------------------")
        print("Doctor ID      :", doctor["id"])
        print("Name           :", doctor["name"])
        print("Specialization :", doctor["specialization"])
        print("Phone          :", doctor["phone"])
