def add_Patient():
    """Adds a new Patient to the system"""
    print("\n--- Add New Patient ---")

    # input validation for Patient ID
    Patient_id = int(input("enter Patient ID:"))
    if Patient_id in Patients: 
        print("Error: Patient ID already exists!")
        return
    name = input("Enter Patient Name:")
    age = int(input("Enter Patient Age:"))
    gender = input("Enter Gender (M/F/other):")

    # Display available doctors
    print("\n available dosctors:")
    for doc_id, (doc_name, dept) in Doctors.items():
        print(f"ID: {doc_id} name: {doc_name} Specialization: {dept}")

    doctor_id = int(input("Assign Doctor ID:"))
    if doctor_id not in doctor:
        print("invalid doctpor id! setting default to unassigned (0).")
        doctor_id = 0

    consultation_fee = float(input("Enter Initial Consultation Fee: $"))

    # Store in Patient dictionary
    patients[atient_id] = {
        "name": name, 
        "age": age,
        "gender": gender,
        "doctor_id": doctor_id,
        "bill": consultation_fee
    }
    print(f"Patient '{name}' added successfully!")