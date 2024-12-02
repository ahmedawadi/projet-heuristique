import matplotlib.pyplot as plt


# Function to process a single file
def process_file(file_path):
    averages = []  # List to store the averages
    with open(file_path, "r") as file:
        for line in file:
            # Convert the line into a list of integer
            splitted_line = line.strip().split(";")[:-1]
            average = list(map(int, splitted_line))
            # Compute the average

            # Append the average to the list
            averages.append(average)

    return averages


# Main script to process all files
file_paths = [
    "results/bpso1-results/mkp1.txt",
    "results/bpso2-results/mkp1.txt",
    "results/bga1-results/mkp1.txt",
    "results/bpso1-results/mkp4.txt",
    "results/bpso1-results/mkp5.txt",
    "results/bpso1-results/mkp6.txt",
    "results/bpso1-results/mkp7.txt",
    "results/bpso1-results/mkp8.txt",
    "results/bpso1-results/mkp9.txt",
    "results/bpso1-results/mkp10.txt",
]  # List of 10 file paths

all_averages = []  # List to store the averages for all files

file_averages = [
    process_file(file_paths[0]),
    process_file(file_paths[1]),
    process_file(file_paths[2]),
]

# Plotting the data
plt.figure(figsize=(10, 6))  # Set the figure size

for i, execution_average in enumerate(file_averages):
    # Transpose the data to get columns using zip
    columns = zip(*execution_average)

    # Calculate the average of each column
    column_averages = [sum(column) / len(column) for column in columns]

    # Generate x values (indices multiplied by 20)
    x_values = [index * 20 for index in range(len(column_averages))]
    # Plot each list as a separate curve
    plt.plot(x_values, column_averages, label=f"METHODE {i + 1}")

# Add labels, legend, and grid
plt.xlabel("Iterations")
plt.ylabel("Average best")
plt.title(
    "Figure 1: Test de BPSO1 avec paramètres c1=0.5 c2=0.4 pour le problème MKP1."
)
plt.grid(True)
plt.legend()
# Show the plot
plt.show()
