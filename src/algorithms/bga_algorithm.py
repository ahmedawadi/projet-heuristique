from objective_functionnalities.mkp_functionnalities import get_function
import numpy as np

# Algorithm parameters
MAX_ITER = 1020  # 1Nombre maximum d'itérations
PAS = 20


def genetic_algorithm(N, D, D1, f, i, result_folder_path, Delta):
    # Initialisation des parents et de leurs fi (fitnesses)
    result_file_path = f"{result_folder_path}/mkp{i}.txt"
    parents = np.random.randint(0, 2, (N, D))
    fitnesses = np.array([f(parent) for parent in parents])  # Use the dynamic func
    results = []

    t = 0
    while t < MAX_ITER:
        mutation_rate = 0.1 - (0.1 - 0.01) * (t / MAX_ITER)
        j, k = np.random.randint(0, N, (2, N))
        cross_point = np.random.randint(1, D - 1)
        enfants = np.hstack((parents[j, :cross_point], parents[k, cross_point:]))

        for i in range(N):
            mutation_mask = np.random.rand(D) < mutation_rate
            enfants[i] = np.where(mutation_mask, 1 - enfants[i], enfants[i])

        enfants_fitnesses = np.array(
            [f(enfant) for enfant in enfants]
        )  # Use the dynamic func
        combined_population = np.vstack((parents, enfants))
        combined_fitnesses = np.hstack((fitnesses, enfants_fitnesses))

        best_indices = np.argsort(combined_fitnesses)[:N]
        parents = combined_population[best_indices]
        fitnesses = combined_fitnesses[best_indices]

        if t % PAS == 0 and t != 0:
            with open(result_file_path, "+a") as writer:
                writer.write(f"{(fitnesses[0])};")
                writer.close()

        t += 1

    with open(result_file_path, "+a") as writer:
        writer.write("\n")
        writer.close()


def run_genetic_algorithm_executions(Delta, result_folder_path):
    for i in range(1, 11):
        if i < 7:
            for _ in range(0, 30):
                genetic_algorithm(
                    30, 28, 14, get_function(i), i, result_folder_path, Delta
                )
        elif i < 9:
            for _ in range(0, 30):
                genetic_algorithm(
                    105, 105, 52, get_function(i), i, result_folder_path, Delta
                )
        else:
            for _ in range(0, 30):
                genetic_algorithm(
                    60, 60, 30, get_function(i), i, result_folder_path, Delta
                )
