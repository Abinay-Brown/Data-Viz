import numpy as np
import os  # Import os for file existence check

def save_excel(data, excel_file_path='data_excel_numpy.xlsx'):
    structured_data = np.array(data, dtype=[('Value', int)])

    # Check if the file exists before reading
    if os.path.exists(excel_file_path):
        try:
            existing_data = np.genfromtxt(excel_file_path, delimiter=',', dtype=[('Value', int)], skip_header=1)
        except FileNotFoundError:
            existing_data = np.array([], dtype=[('Value', int)])
    else:
        existing_data = np.array([], dtype=[('Value', int)])  # Initialize as empty if file doesn't exist

    combined_data = np.concatenate([existing_data, structured_data])

    # Save data to Excel
    np.savetxt(excel_file_path, combined_data, delimiter=',', fmt='%d', header='Value', comments='')

    # Print the Excel sheet (excluding the header)
    print("\nExcel Sheet:")
    print(combined_data[1:])  # Exclude the first row (header)

    return True

def main():
    n = int(input("Enter the number of data points (n): "))

    # Get values from the user
    data = [int(input(f"Enter value {i + 1}: ")) for i in range(n)]

    # Save to Excel and print
    save_excel(data)

if __name__ == "__main__":
    main()










