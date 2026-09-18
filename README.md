# Hospital Patient CRUD App
The system manages hospital patient records and billing information entirely from the command line, using CSV files for persistent storage so that no data is lost between sessions.

---

## Project Description

This application simulates a small hospital's front-desk record-keeping system. It allows staff to register patients, look up and update their details, discharge (delete) patients, generate itemized bills, and view billing summaries — all through a simple numbered menu.

The project was built specifically to demonstrate the integration of core Python concepts into one working, real-world-style application rather than isolated exercises:

- **Data types & variables** – strings, integers, floats, dictionaries, and lists used to model patients and bills
- **Conditional statements & loops** – input validation loops, menu dispatch, and record searching
- **Functions** – every operation (add, view, search, update, delete, bill) is a separate, reusable function
- **Exception handling** – `try/except` blocks guard against invalid numeric input and missing files
- **File I/O** – patient and billing records are read from and written to CSV files using Python's `csv` module
- **Menu-driven design** – a `while True` loop presents a numbered menu and dispatches to the correct function until the user exits

---

## Features

### Patient Management
| # | Feature | Description |
|---|---------|-------------|
| 1 | **Add Patient** | Registers a new patient with an auto-generated unique ID (`P001`, `P002`, ...), validating name, age, gender, and contact number |
| 2 | **View All Patients** | Displays every patient record in a formatted table, along with a total count |
| 3 | **Search Patient** | Finds patients by partial/full **ID** or **name** (case-insensitive) |
| 4 | **Update Patient** | Edits any field of an existing patient; leaving an input blank keeps the old value |
| 5 | **Delete Patient** | Removes a patient record after showing their details and asking for confirmation |

### Billing Management
| # | Feature | Description |
|---|---------|-------------|
| 6 | **Generate Patient Bill** | Creates an itemized bill (consultation, room, medicine, lab, other charges) for an existing patient, with an auto-generated bill ID (`B001`, `B002`, ...) and auto-calculated total |
| 7 | **View All Bills** | Lists every bill generated, in tabular form |
| 8 | **Search Bill** | Finds a bill by **Bill ID** or **Patient ID** |
| 9 | **Bill Summary** | Shows the total number of bills generated and the total revenue collected |

### System
| # | Feature | Description |
|---|---------|-------------|
| 10 | **Exit** | Safely closes the application |
|  — | **Persistent Storage** | All data is stored in `patients.csv` and `bills.csv`, created automatically on first run |
|  — | **Input Validation** | Age (1–120), 10-digit contact numbers, gender (Male/Female/Other), and non-negative billing amounts are all validated with retry loops |
|  — | **Live Patient Count** | The current number of registered patients is shown on the main menu at all times |

---

## 🛠️ Technologies & Concepts Used

- **Language:** Python 3
- **Standard Library Modules:**
  - `csv` – reading and writing structured record data
  - `os` – checking file existence before creating new data files
  - `datetime` – auto-stamping admission dates and bill dates
- **Third-Party Library:**
  - [`tabulate`](https://pypi.org/project/tabulate/) – renders clean, grid-style tables in the console
- **Core Programming Concepts:**
  - Dictionaries and lists for in-memory record representation
  - Functions with parameters, return values, and default dispatch (via a `MENU_ACTIONS` dictionary)
  - `while` loops for both the main menu and input re-validation
  - `try/except` blocks for handling `ValueError` (bad numeric input) and `FileNotFoundError` (missing CSV files)
  - String methods (`.strip()`, `.upper()`, `.lower()`, `.title()`, `.isdigit()`, `.startswith()`) for cleaning and validating user input
  - List comprehensions for filtering and formatting records
  - f-strings for formatted output (e.g. `₹{total:.2f}`)

---

## Project Structure

```
hospital-management-system/
│
├── hospital_management.py   # Main application source code
├── patients.csv              # Auto-generated: stores patient records
├── bills.csv                  # Auto-generated: stores billing records
├── README.md                 # Project documentation (this file)
└── screenshots/               # Screenshots demonstrating the working app
    ├── main_menu.png
    ├── add_patient.png
    ├── view_patients.png
    ├── generate_bill.png
    └── bill_summary.png
```

> `patients.csv` and `bills.csv` they are created automatically the first time the program runs.

---

## How to Run the Application

### Prerequisites
- Python 3.7 or higher installed on your system
- `pip` package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Hospital-Patient-Management-System
   ```

2. **Install the required dependency**
   ```bash
   pip install tabulate
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Use the on-screen menu** to add patients, generate bills, and manage records. All data is automatically saved to `patients.csv` and `bills.csv` in the same folder, so your records will still be there the next time you run the program.

---

## Sample Input / Output

### Main Menu
```
======================================================================
                      HOSPITAL MANAGEMENT SYSTEM
======================================================================

Current number of patients: 1

1.  Add Patient
2.  View All Patients
3.  Search Patient
4.  Update Patient
5.  Delete Patient
6.  Generate Patient Bill
7.  View All Bills
8.  Search Bill
9.  Bill Summary
10. Exit
======================================================================
Enter your choice:
```

### Adding a Patient
```
Enter your choice: 1

======================================================================
                        ADD NEW PATIENT
======================================================================
Generated Patient ID: P001
Enter Patient Name: John Doe
Enter Age: 30
Enter Gender (Male/Female/Other): Male
Enter Contact Number: 9876543210
Enter Disease: Fever
Enter Doctor Name: Dr. Smith
Enter Room Number: 101

Patient added successfully.
Patient ID: P001
```

### Generating a Bill
```
Enter your choice: 6

======================================================================
                     GENERATE PATIENT BILL
======================================================================
Enter Patient ID: P001

Patient Information
======================================================================
Patient ID : P001
Name       : John Doe
Doctor     : Dr. Smith
Room       : 101
======================================================================

Enter Billing Details
Consultation Charges: ₹500
Room Charges: ₹1000
Medicine Charges: ₹200
Lab/Test Charges: ₹300
Other Charges: ₹100

Bill generated successfully.

======================================================================
                          PATIENT BILL
======================================================================
+----------------+----------+
| Description    | Amount   |
+================+==========+
| Bill ID        | B001     |
+----------------+----------+
| Patient ID     | P001     |
+----------------+----------+
| Patient Name   | John Doe |
+----------------+----------+
| Consultation   | ₹500.00  |
+----------------+----------+
| Room Charges   | ₹1000.00 |
+----------------+----------+
| Medicine       | ₹200.00  |
+----------------+----------+
| Lab/Test       | ₹300.00  |
+----------------+----------+
| Other Charges  | ₹100.00  |
+----------------+----------+
| TOTAL          | ₹2100.00 |
+----------------+----------+
| Bill Date      | 2026-09-18 |
+----------------+----------+
```

### Bill Summary
```
Enter your choice: 9

======================================================================
                          BILL SUMMARY
======================================================================
+-------------------+-----------+
| Description       | Value     |
+===================+===========+
| Total Bills       | 1         |
+-------------------+-----------+
| Total Collection  | ₹2100.00  |
+-------------------+-----------+
```

> 📷 Screenshots of the above output running in an actual terminal are provided in the `/screenshots` folder.

---

## Error Handling Examples

The application gracefully handles invalid input instead of crashing:

```
Enter Age: abc
Please enter a number.
Enter Age: 250
Enter a valid age between 1 and 120.
Enter Age: 30
```

```
Enter Contact Number: 12345
Enter a valid 10-digit contact number.
Enter Contact Number: 9876543210
```

```
Consultation Charges: ₹-50
Amount cannot be negative.
Consultation Charges: ₹500
```

Missing data files are also handled silently — `patients.csv` and `bills.csv` are created automatically on first launch if they don't already exist, and a `FileNotFoundError` while reading is caught and treated as "no records yet."

---

## Author / GitHub Repository Details

| Field | Detail |
|-------|--------|
| **Name** | Tanvi Sharma |
| **Roll no** | 01 |
| **Course** | MCA – Semester I |
| **Subject** | Python Programming & Relational Database |
| **Assignment** | Assignment 1 – Mini Project: Console Record-Management Application |
| **Submission Date** | *18/09/2026* |

---
