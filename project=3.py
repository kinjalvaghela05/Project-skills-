def main():
    
    students_list = []

    
    all_subjects_set = set()

    print("========================================")
    print(" Welcome to Student Data Organizer! ")
    print("========================================\n")

    while True:
        
        print("Select an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        
        # ---------------------------------------------------------
        # OPTION 1: Add Student
        # ---------------------------------------------------------
       
        if choice == "1":
            print("\nEnter student details:")
            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()

            
            age = int(input("Age: ").strip())
            grade = input("Grade: ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()

           
            id_dob_tuple = (student_id, dob)

            
            raw_subjects = input(
                "Subjects (comma-separated, e.g. Math, Science): "
            ).strip()
            subject_list = [s.strip() for s in raw_subjects.split(",")]
            subjects_set = set(subject_list)

            
            all_subjects_set.update(subjects_set)

           
            student_dict = {
                "id": id_dob_tuple[0],
                "dob": id_dob_tuple[1],
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subjects_set,
            }

            
            students_list.append(student_dict)
            print("\nStudent added successfully!\n")

        # ---------------------------------------------------------
        # OPTION 2: Display All Students
        # ---------------------------------------------------------
        elif choice == "2":
            if not students_list:
                print("\nNo student records found.\n")
            else:
                print("\n-- Display All Students --")
                for s in students_list:
                    sub_str = ", ".join(s["subjects"])
                
                    print(
                        f"Student ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {sub_str}"
                    )
                print()

        # ---------------------------------------------------------
        # OPTION 3: Update Student Information
        # ---------------------------------------------------------
        elif choice == "3":
            search_id = input("\nEnter Student ID to update: ").strip()
            found = False

            for s in students_list:
                if s["id"] == search_id:
                    print(f"Updating record for {s['name']}:")
                    s["name"] = input("Enter new Name: ").strip()
                    s["age"] = int(input("Enter new Age: ").strip())
                    s["grade"] = input("Enter new Grade: ").strip()

                    raw_subjects = input(
                        "Enter new Subjects (comma-separated): "
                    ).strip()
                    s["subjects"] = set([sub.strip() for sub in raw_subjects.split(",")])

                   
                    all_subjects_set.clear()
                    for student in students_list:
                        all_subjects_set.update(student["subjects"])

                    print("Student information updated successfully!\n")
                    found = True
                    break

            if not found:
                print("Student ID not found.\n")

        # ---------------------------------------------------------
        # OPTION 4: Delete Student
        # ---------------------------------------------------------
        elif choice == "4":
            search_id = input("\nEnter Student ID to delete: ").strip()
            found_index = -1

            for i in range(len(students_list)):
                if students_list[i]["id"] == search_id:
                    found_index = i
                    break

            if found_index != -1:
              
                del students_list[found_index]

               
                all_subjects_set.clear()
                for student in students_list:
                    all_subjects_set.update(student["subjects"])

                print(f"Student ID {search_id} deleted successfully!\n")
            else:
                print("Student ID not found.\n")

        # ---------------------------------------------------------
        # OPTION 5: Display Subjects Offered
        # ---------------------------------------------------------
        elif choice == "5":
            if not all_subjects_set:
                print("\nNo subjects available.\n")
            else:
                print("\n-- Display Subjects Offered --")
                sub_formatted = ", ".join(all_subjects_set)
                
                print("Unique Subjects Offered: {}".format(sub_formatted))
                print()

        # ---------------------------------------------------------
        # OPTION 6: Exit
        # ---------------------------------------------------------
        elif choice == "6":
            print(
                "\nThank you for using the Student Data Organizer! Good luck with your submission."
            )
            break

        else:
            print("\nInvalid option! Please enter a number between 1 and 6.\n")



if __name__ == "__main__":
    main()
