import csv
import os

# ---------------- PATIENTS ---------------- #

def load_patients():
    patients = []

    if os.path.exists("patients.csv"):
        with open("patients.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            patients = list(reader)

    return patients


def save_patients(patients):
    with open("patients.csv", "w", newline="") as file:
        fieldnames = [
            "PatientID",
            "Name",
            "Age",
            "Gender",
            "Disease",
            "Severity",
            "Department",
            "Status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patients)


# ---------------- APPOINTMENTS ---------------- #

def load_appointments():
    appointments = []

    if os.path.exists("appointments.csv"):
        with open("appointments.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            appointments = list(reader)

    return appointments


def save_appointments(appointments):
    with open("appointments.csv", "w", newline="") as file:
        fieldnames = [
            "AppointmentID",
            "PatientID",
            "Doctor",
            "Date",
            "Time"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(appointments)


# ---------------- BILLS ---------------- #

def load_bills():
    bills = []

    if os.path.exists("bills.csv"):
        with open("bills.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            bills = list(reader)

    return bills


def save_bills(bills):
    with open("bills.csv", "w", newline="") as file:
        fieldnames = [
            "BillID",
            "PatientID",
            "Amount"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(bills)