import numpy as np
import statistics
import pandas as pd


# Function to process a single file
def process_file(file_path):
    last_iterations = []  # List to store the last_iterations
    with open(file_path, "r") as file:
        for line in file:
            # Convert the line into a list of integer
            last_iteration = int(line.strip().split(";")[-2])
            # Compute the last_iteration

            # Append the last_iteration to the list
            last_iterations.append(last_iteration)

    return last_iterations


# Main script to process all files
file_paths = [
    "../results/bga1-results/mkp1.txt",
    "../results/bga1-results/mkp2.txt",
    "../results/bga1-results/mkp3.txt",
    "../results/bga1-results/mkp4.txt",
    "../results/bga1-results/mkp5.txt",
    "../results/bga1-results/mkp6.txt",
    "../results/bga1-results/mkp7.txt",
    "../results/bga1-results/mkp8.txt",
    "../results/bga1-results/mkp9.txt",
    "../results/bga1-results/mkp10.txt",
]  # List of 10 file paths

files_last_iterations = [process_file(file_paths[0])]

# Process each file and calculate statistics
results = []
for file_path in file_paths:
    last_iterations = process_file(file_path)  # Replace with actual processing logic
    best_value = max(last_iterations)
    average = sum(last_iterations) / len(last_iterations)
    ecartype = sum([value**2 for value in last_iterations]) ** 0.5
    results.append(
        f"Meilleure: {best_value:.2f}\nMoyenne: {average:.2f}\nÉcart type: {ecartype:.2f}"
    )

# Load the existing Excel file
file_path_excel = "../results/methods-results.xlsx"
df = pd.read_excel(file_path_excel)

# Write results into the "BPSO2" column for MKP1 to MKP10
df.loc[:9, "GA1"] = results  # First 10 rows correspond to MKP1 to MKP10

# Save the updated Excel file
updated_file_path = "methods-results.xlsx"
df.to_excel(updated_file_path, index=False)

updated_file_path
