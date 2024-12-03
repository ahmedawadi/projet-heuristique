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
            average = [abs(average_value) for average_value in average]

            # Append the average to the list
            averages.append(average)

    return averages


# Main script to process all files
file_paths = [
    "src/results/bpso1-results/mkp",
    "src/results/bpso2-results/mkp",
    "src/results/bga1-results/mkp",
    "src/results/bga2-results/mkp",
]  # List of 10 file paths

all_averages = []  # List to store the averages for all files


for object_function_index in range(1, 11):
    file_averages = []

    for file_path in file_paths:
        file_averages.append(
            process_file(f"{file_path + str(object_function_index)}.txt")
        )

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
    plt.title(f"Figure 1: Test des 6 methodes avec MKP {object_function_index}")
    plt.grid(True)
    plt.legend()
    # Show the plot
    plt.savefig(f"src/results_analysis/curves/mkp{object_function_index}")
