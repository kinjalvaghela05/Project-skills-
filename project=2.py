print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    # Option 1: Pattern Generator
    if choice == '1':
        r = int(input("Enter the number of rows for the pattern: "))
        
        if r<= 0:
            print("Please enter a positive number of rows!")
        else:
            print("\nPattern:")
            for i in range(1, r+ 1):
                j = 1
                while j <= i:
                    pass  
                    print("*", end="")
                    j = j + 1
                print() 
                
    # Option 2: Number Analyzer
    elif choice == '2':
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        if end < start:
            print("End number should be greater than start number!")
        else:
            total_sum = 0
            print()
            
            for num in range(start, end + 1):
                total_sum = total_sum + num
                if num % 2 == 0:
                    print(f"Number {num} is Even")
                else:
                    print(f"Number {num} is Odd")
                    
            print(f"Sum of all numbers from {start} to {end} is: {total_sum}")
            
    # Option 3: Exit
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
