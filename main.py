from ADDPATIENT import add_Patient
from search import search_patient
from VIEWPATIENT import view_patient

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