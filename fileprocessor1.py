# fileprocessor1.py

filename = "fileprocessor.input"

try:
    with open(filename, 'r') as file:
        print("Printing out User Data:\n")

        for line in file:
            if line.startswith('#'):
                continue  # Skip lines starting with a hashtag

            data = line.strip().split(':')
            username = data[0].strip()
            password = data[1].strip()
            userid = data[2].strip()
            groupid = data[3].strip()

            print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")

        print("\nEnd of User Data")

except FileNotFoundError:
    print(f"Error: {filename} not found.")
except Exception as e:
    print(f"An error occurred: {e}")
