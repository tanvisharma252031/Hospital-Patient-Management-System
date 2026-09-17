from file_handler import *

# ---------------- PATIENT CRUD ---------------- #

def add_patient():
    patients = load_patients()

    patient_id = input("Enter Patient ID: ")

    for patient in patients:
        if patient["PatientID"] == patient_id:
            print("Patient ID already exists!")
            return

    name = input("Enter Name: ")

    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid Age")
        return

    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    severity = input("Enter Severity: ")
    department = input("Enter Department: ")
    status = input("Enter Status: ")

    patients.append({
        "PatientID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease,
        "Severity": severity,
        "Department": department,
        "Status": status
    })

    save_patients(patients)

    print("Patient Added Successfully!")


def view_patients():
    patients = load_patients()

    if not patients:
        print("No Patients Found")
        return

    print("\nPATIENT RECORDS\n")

    for patient in patients:
        print(patient)


def search_patient():
    patients = load_patients()

    pid = input("Enter Patient ID: ")

    for patient in patients:
        if patient["PatientID"] == pid:
            print(patient)
            return

    print("Patient Not Found")


def update_patient():
    patients = load_patients()

    pid = input("Enter Patient ID: ")

    for patient in patients:

        if patient["PatientID"] == pid:

            patient["Name"] = input("New Name: ")
            patient["Disease"] = input("New Disease: ")
            patient["Status"] = input("New Status: ")

            save_patients(patients)

            print("Updated Successfully")
            return

    print("Patient Not Found")


def delete_patient():
    patients = load_patients()

    pid = input("Enter Patient ID: ")

    for patient in patients:

        if patient["PatientID"] == pid:

            confirm = input("Delete Patient? (Y/N): ")

            if confirm.upper() == "Y":
                patients.remove(patient)
                save_patients(patients)

                print("Deleted Successfully")

            return

    print("Patient Not Found")

# ---------------- APPOINTMENTS ---------------- #

def book_appointment():
    appointments = load_appointments()

    appointment_id = input("Appointment ID: ")
    patient_id = input("Patient ID: ")
    doctor = input("Doctor Name: ")
    date = input("Date: ")
    time = input("Time: ")

    appointments.append({
        "AppointmentID": appointment_id,
        "PatientID": patient_id,
        "Doctor": doctor,
        "Date": date,
        "Time": time
    })

    save_appointments(appointments)

    print("Appointment Booked")


def view_appointments():
    appointments = load_appointments()

    for appointment in appointments:
        print(appointment)

# ---------------- BILLING ---------------- #

def generate_bill():

    bills = load_bills()

    bill_id = input("Bill ID: ")
    patient_id = input("Patient ID: ")

    try:
        consultation = float(input("Consultation Fee: "))
        medicine = float(input("Medicine Charges: "))
        room = float(input("Room Charges: "))
    except ValueError:
        print("Invalid Amount")
        return

    total = consultation + medicine + room

    bills.append({
        "BillID": bill_id,
        "PatientID": patient_id,
        "Amount": total
    })

    save_bills(bills)

    print(f"Total Bill = ₹{total}")


# ---------------- DASHBOARD ---------------- #

def dashboard():

    patients = load_patients()
    appointments = load_appointments()
    bills = load_bills()

    print("\nHOSPITAL DASHBOARD")
    print("---------------------")

    print("Total Patients:", len(patients))
    print("Total Appointments:", len(appointments))
    print("Total Bills:", len(bills))

# ---------------- MENU ---------------- #

def menu():

    while True:

        print("""
====================================
SMART HOSPITAL MANAGEMENT SYSTEM
====================================

1. Add Patient
2. View Patients
3. Search Patient
4. Update Patient
5. Delete Patient

6. Book Appointment
7. View Appointments

8. Generate Bill

9. Dashboard

10. Exit
""")

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid Input")
            continue

        if choice == 1:
            add_patient()

        elif choice == 2:
            view_patients()

        elif choice == 3:
            search_patient()

        elif choice == 4:
            update_patient()

        elif choice == 5:
            delete_patient()

        elif choice == 6:
            book_appointment()

        elif choice == 7:
            view_appointments()

        elif choice == 8:
            generate_bill()

        elif choice == 9:
            dashboard()

        elif choice == 10:
            print("Thank You!")
            break

        else:
            print("Invalid Choice")


menu()