import csv
try :
    # Open the file in "r+" mode for reading and writing
    with open("simple.txt", "r+") as file:
        # Read the current content
        content = file.read()
        print("Current content of file:\n", content)

        # Write new data to the file
        file.write("\nThis is a new line added to the file.")

        # Move the cursor back to the beginning of the file
        file.seek(0)

        # Read the updated content
        updated_content = file.read()
        print("\nUpdated content of file:\n", updated_content)


    # Open the file in "a+" mode for appending and reading
    with open("sample.csv", "a+", newline="") as file:
        # Move the cursor to the beginning to read the current content
        file.seek(0)
        reader = csv.reader(file)
        print("Current content of CSV file:")
        for row in reader:
            print(row)

        # Write new data to the CSV file
        writer = csv.writer(file)
        writer.writerow(["Charlie", 35, "Los Angeles"])

        # Move the cursor back to the beginning to read the updated content
        file.seek(0)
        updated_reader = csv.reader(file)
        print("\nUpdated content of CSV file:")
        for row in updated_reader:
            print(row)

except Exception  as  e :
     print(e)