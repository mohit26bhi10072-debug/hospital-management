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