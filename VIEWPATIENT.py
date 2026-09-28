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