# Hospital Management System

# Global data structure storing doctor details
# Format: Doctor ID -> (Name, Specialization)
Doctor = {
    101: ("Dr. Mohit Bhardwaj", "Neurologist"),
    102: ("Dr. Salinder Bhardwaj", "Cardiologist"),
    103: ("Dr. prince Bhardwaj", "Surgeon"),
    104: ("Dr. Ansh Bhardwaj", "Radiologist")
}

#  Global Dictionary to Store Patient Records
#  Format: Patient ID -> {"name": str, "age": int, "gender":str, "doctor_id": int, "bill" float}
Patient = {}

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

    def view_patient():
        """Display all patient details."""
        print("\n--- Patient Directory ---")
        if not patients:
            print("No patient record found.")
            return

        for p_id, info in patients,items():
            doc_id = info["doctor_id"]
        # Tuple unpacking to retrieve doctor details
        doc_name, dept = Doctor.get(doc_id, ("unassigned", "N/A"))

        print(f"\nID: {p_id}")
        print(f" Name   :{info['name']}")
        print(f" age/gender : {info['age']} / {info['gender']}")
        print(f" doctor  :{doc_name} ({dept})")
        print(f" Total Bill: ${info['bill']:2f}")

    def search_patient():
        """Search for a patient by ID."""
        print("\n--- Search Patient ---")
        p_id = int(input("Enter Patient ID to search: "))

        if p_id in patients:
            info = patients[p_id]
            doc_name, dept = Doctors.get(info["doctor_id"], ("unassigned", "N/A"))
            print("\nRecord Found:")
            print(f"  Name   : {info['name']}")
            print(f"  age/gender  : {info['age']} / {info['gender']}")
            print(f"  Doctor   : {doc_name} ({dept})")
            print(f"  Total bill  : ${info['bill']:.2f}")
        else:
            print("Patient not Found.")

        def main():
            """Main program execution loop."""
            while true:
                print("\n==")
                print("   HOSPITAL MANAGEMANET SYSTEM   ")
                print("====")
                print("1. Add Patient")
                print("2. View All Patients")
                print("3. Search Patient")
                print("4. Add Treatment Charges")
                print("5. Exit")

                choice = input("Enter your chioce (1_5):")

            if  choice =='1': 
                add_patient()
            elif choice =='2':
                view_patient()
            elif choice =='3':
                search_patient()
            elif choice =='4':
                add_medical_charges()
            elif choice =='5':
                print("\nExisting system. Goodbye!")
                'break'
            else:
                print("Invalid selection! Please  entera number From 1 to 5.")

            # Run the application 
            if __name__ == "__main__":
                main()
            
            

        
        
                         





    
