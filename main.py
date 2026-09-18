import csv
import os
from datetime import datetime
from tabulate import tabulate

PATIENT_FILE = "patients.csv"
BILL_FILE = "bills.csv"

PATIENT_FIELDS = [
    "patient_id", "name", "age", "gender", "contact",
    "disease", "doctor", "admission_date", "room"
]
BILL_FIELDS = [
    "bill_id", "patient_id", "patient_name", "consultation",
    "room_charges", "medicine", "lab_charges", "other_charges",
    "total", "bill_date"
]

PATIENT_HEADERS = ["ID", "Name", "Age", "Gender", "Contact", "Disease", "Doctor", "Admission", "Room"]
BILL_HEADERS = ["Bill ID", "Patient ID", "Patient", "Consultation", "Room", "Medicine", "Lab", "Other", "Total", "Date"]

def line():
    print("=" * 70)

def heading(title):
    print()
    line()
    print(title.center(70))
    line()

def pause():
    input("\nPress Enter to continue...")

def get_date():
    return datetime.now().strftime("%Y-%m-%d")

def create_file(filename, fields):
    if not os.path.exists(filename):
        with open(filename, "w", newline="") as file:
            csv.DictWriter(file, fieldnames=fields).writeheader()

def setup_files():
    create_file(PATIENT_FILE, PATIENT_FIELDS)
    create_file(BILL_FILE, BILL_FIELDS)

def read_data(filename):
    try:
        with open(filename, "r", newline="") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def write_data(filename, fields, data):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

def generate_id(data, field, prefix):
    numbers = []
    for item in data:
        value = item.get(field, "")
        if value.startswith(prefix):
            try:
                numbers.append(int(value[len(prefix):]))
            except ValueError:
                pass
    return prefix + str(max(numbers, default=0) + 1).zfill(3)

def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def get_age():
    while True:
        try:
            age = int(input("Enter Age: "))
            if 0 < age <= 120:
                return age
            print("Enter a valid age between 1 and 120.")
        except ValueError:
            print("Please enter a number.")

def get_contact():
    while True:
        contact = input("Enter Contact Number: ").strip()
        if contact.isdigit() and len(contact) == 10:
            return contact
        print("Enter a valid 10-digit contact number.")

def get_gender():
    while True:
        gender = input("Enter Gender (Male/Female/Other): ").strip().title()
        if gender in ["Male", "Female", "Other"]:
            return gender
        print("Please enter Male, Female or Other.")

def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0:
                return amount
            print("Amount cannot be negative.")
        except ValueError:
            print("Please enter a valid amount.")

def find_patient(patient_id):
    for patient in read_data(PATIENT_FILE):
        if patient["patient_id"].upper() == patient_id.upper():
            return patient
    return None

def patient_row(p):
    return [p["patient_id"], p["name"], p["age"], p["gender"], p["contact"],
            p["disease"], p["doctor"], p["admission_date"], p["room"]]

def bill_row(b):
    return [b["bill_id"], b["patient_id"], b["patient_name"],
            "₹" + b["consultation"], "₹" + b["room_charges"], "₹" + b["medicine"],
            "₹" + b["lab_charges"], "₹" + b["other_charges"], "₹" + b["total"], b["bill_date"]]

def add_patient():
    heading("ADD NEW PATIENT")
    patients = read_data(PATIENT_FILE)
    patient_id = generate_id(patients, "patient_id", "P")
    print("Generated Patient ID:", patient_id)
    patient = {
        "patient_id": patient_id,
        "name": get_non_empty("Enter Patient Name: "),
        "age": get_age(),
        "gender": get_gender(),
        "contact": get_contact(),
        "disease": get_non_empty("Enter Disease: "),
        "doctor": get_non_empty("Enter Doctor Name: "),
        "admission_date": get_date(),
        "room": get_non_empty("Enter Room Number: ")
    }
    patients.append(patient)
    write_data(PATIENT_FILE, PATIENT_FIELDS, patients)
    print("\nPatient added successfully.")
    print("Patient ID:", patient_id)
    pause()

def view_patients():
    heading("ALL PATIENTS")
    patients = read_data(PATIENT_FILE)
    if not patients:
        print("No patient records found.")
        pause()
        return
    table = [patient_row(p) for p in patients]
    print(tabulate(table, headers=PATIENT_HEADERS, tablefmt="grid"))
    print("\nTotal Patients:", len(patients))
    pause()

def search_patient():
    heading("SEARCH PATIENT")
    patients = read_data(PATIENT_FILE)
    if not patients:
        print("No patient records found.")
        pause()
        return
    search = input("Enter Patient ID or Name: ").strip().lower()
    results = [p for p in patients
               if search in p["patient_id"].lower() or search in p["name"].lower()]
    if not results:
        print("No matching patient found.")
        pause()
        return
    table = [patient_row(p) for p in results]
    print(tabulate(table, headers=PATIENT_HEADERS, tablefmt="grid"))
    pause()

def update_patient():
    heading("UPDATE PATIENT")
    patients = read_data(PATIENT_FILE)
    if not patients:
        print("No patient records found.")
        pause()
        return
    patient_id = input("Enter Patient ID: ").strip().upper()
    for patient in patients:
        if patient["patient_id"] != patient_id:
            continue
        print("\nLeave a field blank to keep old value.\n")
        name = input(f"Name [{patient['name']}]: ").strip()
        if name:
            patient["name"] = name
        age = input(f"Age [{patient['age']}]: ").strip()
        if age:
            try:
                age = int(age)
                if 1 <= age <= 120:
                    patient["age"] = age
                else:
                    print("Invalid age. Old value kept.")
            except ValueError:
                print("Invalid age. Old value kept.")
        gender = input(f"Gender [{patient['gender']}]: ").strip()
        if gender:
            patient["gender"] = gender.title()
        contact = input(f"Contact [{patient['contact']}]: ").strip()
        if contact:
            if contact.isdigit() and len(contact) == 10:
                patient["contact"] = contact
            else:
                print("Invalid contact. Old value kept.")
        disease = input(f"Disease [{patient['disease']}]: ").strip()
        if disease:
            patient["disease"] = disease
        doctor = input(f"Doctor [{patient['doctor']}]: ").strip()
        if doctor:
            patient["doctor"] = doctor
        room = input(f"Room [{patient['room']}]: ").strip()
        if room:
            patient["room"] = room
        write_data(PATIENT_FILE, PATIENT_FIELDS, patients)
        print("\nPatient updated successfully.")
        pause()
        return
    print("Patient ID not found.")
    pause()

def delete_patient():
    heading("DELETE PATIENT")
    patients = read_data(PATIENT_FILE)
    if not patients:
        print("No patient records found.")
        pause()
        return
    patient_id = input("Enter Patient ID: ").strip().upper()
    patient = find_patient(patient_id)
    if not patient:
        print("Patient not found.")
        pause()
        return
    print("\nPatient Details:")
    print("ID:", patient["patient_id"])
    print("Name:", patient["name"])
    print("Disease:", patient["disease"])
    print("Doctor:", patient["doctor"])
    confirm = input("\nAre you sure you want to delete? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("Delete operation cancelled.")
        pause()
        return
    patients = [p for p in patients if p["patient_id"] != patient_id]
    write_data(PATIENT_FILE, PATIENT_FIELDS, patients)
    print("Patient deleted successfully.")
    pause()

def generate_bill():
    heading("GENERATE PATIENT BILL")
    patients = read_data(PATIENT_FILE)
    bills = read_data(BILL_FILE)
    if not patients:
        print("No patients available.")
        pause()
        return
    patient_id = input("Enter Patient ID: ").strip().upper()
    patient = find_patient(patient_id)
    if not patient:
        print("Patient not found.")
        pause()
        return
    print("\nPatient Information")
    line()
    print("Patient ID :", patient["patient_id"])
    print("Name       :", patient["name"])
    print("Doctor     :", patient["doctor"])
    print("Room       :", patient["room"])
    line()
    print("\nEnter Billing Details")
    consultation = get_amount("Consultation Charges: ₹")
    room_charges = get_amount("Room Charges: ₹")
    medicine = get_amount("Medicine Charges: ₹")
    lab_charges = get_amount("Lab/Test Charges: ₹")
    other_charges = get_amount("Other Charges: ₹")
    total = consultation + room_charges + medicine + lab_charges + other_charges
    bill_id = generate_id(bills, "bill_id", "B")
    bill = {
        "bill_id": bill_id,
        "patient_id": patient["patient_id"],
        "patient_name": patient["name"],
        "consultation": f"{consultation:.2f}",
        "room_charges": f"{room_charges:.2f}",
        "medicine": f"{medicine:.2f}",
        "lab_charges": f"{lab_charges:.2f}",
        "other_charges": f"{other_charges:.2f}",
        "total": f"{total:.2f}",
        "bill_date": get_date()
    }
    bills.append(bill)
    write_data(BILL_FILE, BILL_FIELDS, bills)
    print("\nBill generated successfully.")
    display_bill(bill)
    pause()

def display_bill(bill):
    heading("PATIENT BILL")
    table = [
        ["Bill ID", bill["bill_id"]],
        ["Patient ID", bill["patient_id"]],
        ["Patient Name", bill["patient_name"]],
        ["Consultation", "₹" + bill["consultation"]],
        ["Room Charges", "₹" + bill["room_charges"]],
        ["Medicine", "₹" + bill["medicine"]],
        ["Lab/Test", "₹" + bill["lab_charges"]],
        ["Other Charges", "₹" + bill["other_charges"]],
        ["TOTAL", "₹" + bill["total"]],
        ["Bill Date", bill["bill_date"]]
    ]
    print(tabulate(table, headers=["Description", "Amount"], tablefmt="grid"))

def view_bills():
    heading("ALL BILLS")
    bills = read_data(BILL_FILE)
    if not bills:
        print("No bills found.")
        pause()
        return
    table = [bill_row(b) for b in bills]
    print(tabulate(table, headers=BILL_HEADERS, tablefmt="grid"))
    pause()

def search_bill():
    heading("SEARCH BILL")
    bills = read_data(BILL_FILE)
    if not bills:
        print("No bills found.")
        pause()
        return
    search = input("Enter Bill ID or Patient ID: ").strip().upper()
    results = [b for b in bills
               if b["bill_id"].upper() == search or b["patient_id"].upper() == search]
    if not results:
        print("No matching bill found.")
        pause()
        return
    for bill in results:
        display_bill(bill)
    pause()

def bill_summary():
    heading("BILL SUMMARY")
    bills = read_data(BILL_FILE)
    if not bills:
        print("No bills available.")
        pause()
        return
    total_collection = 0
    for bill in bills:
        try:
            total_collection += float(bill["total"])
        except ValueError:
            pass
    table = [
        ["Total Bills", len(bills)],
        ["Total Collection", f"₹{total_collection:.2f}"]
    ]
    print(tabulate(table, headers=["Description", "Value"], tablefmt="grid"))
    pause()

def patient_count():
    print("\nCurrent number of patients:", len(read_data(PATIENT_FILE)))

MENU_ACTIONS = {
    "1": add_patient,
    "2": view_patients,
    "3": search_patient,
    "4": update_patient,
    "5": delete_patient,
    "6": generate_bill,
    "7": view_bills,
    "8": search_bill,
    "9": bill_summary,
}

def print_menu():
    print()
    print("1.  Add Patient")
    print("2.  View All Patients")
    print("3.  Search Patient")
    print("4.  Update Patient")
    print("5.  Delete Patient")
    print("6.  Generate Patient Bill")
    print("7.  View All Bills")
    print("8.  Search Bill")
    print("9.  Bill Summary")
    print("10. Exit")
    line()

def main_menu():
    setup_files()
    while True:
        heading("HOSPITAL MANAGEMENT SYSTEM")
        patient_count()
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "10":
            heading("THANK YOU")
            print("Thank you for using the Hospital Management System.")
            print("Program closed successfully.")
            break
        elif choice in MENU_ACTIONS:
            MENU_ACTIONS[choice]()
        else:
            print("\nInvalid choice.")
            print("Please select a number from 1 to 10.")
            pause()

if __name__ == "__main__":
    main_menu()