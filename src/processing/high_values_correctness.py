def process_high_values(input_file, output_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    processed_lines = []
    for line in lines:
        # Split the line into integers
        values = list(map(int, line.strip().split(";")[:-1]))
        if len(values) > 1:
            min_value = min(values)
            # Replace all positive values with the minimum value
            values = [min_value if value > 0 else value for value in values]
        # Join the modified values back into a string
        processed_lines.append(";".join(map(str, values)))

    # Write the processed lines to the output file
    with open(output_file, "w") as file:
        file.write("\n".join(processed_lines))


files = [
    "src/results/bpso2-results/mkp1.txt",
    "src/results/bpso2-results/mkp2.txt",
    "src/results/bpso2-results/mkp3.txt",
    "src/results/bpso2-results/mkp4.txt",
    "src/results/bpso2-results/mkp5.txt",
    "src/results/bpso2-results/mkp6.txt",
    "src/results/bpso2-results/mkp7.txt",
    "src/results/bpso2-results/mkp8.txt",
    "src/results/bpso2-results/mkp9.txt",
    "src/results/bpso2-results/mkp10.txt",
]

for file in files:
    process_high_values(file, file)
