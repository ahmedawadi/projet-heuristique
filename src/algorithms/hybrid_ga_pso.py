import numpy as np
from objective_functionnalities.mkp_functionnalities import get_function

MAX_ITERATION = 1000
PAS = 20

def hybrid_ga_pso(N, D, G0, alpha, f, index, result_folder_path):
    # Initialization
    population = np.random.randint(0, 2, (N, D))  # Binary population for GA
    velocities = np.random.randn(N, D)  # Velocity matrix for PSO
    best_positions = population.copy()  # Best known positions for particles
    best_fitnesses = np.array([f(ind) for ind in population])  # Fitness of particles
    
    G = G0  # Initialize gravity for PSO
    t = 0  # Iteration counter
    
    while t < MAX_ITERATION:
        # Evaluate fitness
        fitnesses = np.array([f(ind) for ind in population])
        global_best_idx = np.argmin(fitnesses)
        global_best_position = population[global_best_idx]
        
        # Update particle velocities and positions (PSO phase)
        for i in range(N):
            r1, r2 = np.random.rand(D), np.random.rand(D)  # Random factors
            cognitive = r1 * (best_positions[i] - population[i])  # Cognitive term
            social = r2 * (global_best_position - population[i])  # Social term
            velocities[i] = G * velocities[i] + cognitive + social
            population[i] = np.clip(population[i] + velocities[i], 0, 1).round()  # Update position
            
        # Update best-known positions
        for i in range(N):
            if fitnesses[i] < best_fitnesses[i]:
                best_positions[i] = population[i]
                best_fitnesses[i] = fitnesses[i]
        
        # Apply crossover and mutation (GA phase)
        parents_idx = np.random.choice(N, N, replace=False)  # Random pairings
        offspring = []
        for i in range(0, N - 1, 2):
            p1, p2 = population[parents_idx[i]], population[parents_idx[i+1]]
            crossover_point = np.random.randint(1, D-1)  # Single-point crossover
            child1 = np.hstack((p1[:crossover_point], p2[crossover_point:]))
            child2 = np.hstack((p2[:crossover_point], p1[crossover_point:]))
            offspring.extend([child1, child2])

        if N % 2 != 0:  # Pair the last individual
            last_individual = population[parents_idx[-1]]
            random_partner = population[np.random.choice(parents_idx[:-1])]
            crossover_point = np.random.randint(1, D - 1)
            child1 = np.hstack((last_individual[:crossover_point], random_partner[crossover_point:]))
            child2 = np.hstack((random_partner[:crossover_point], last_individual[crossover_point:]))
            offspring.extend([child1, child2])


        offspring = np.array(offspring[:N])
        
        # Mutation
        mutation_rate = 0.1
        mutation_mask = np.random.rand(N, D) < mutation_rate
        offspring = np.where(mutation_mask, 1 - offspring, offspring)
        
        # Select the best N individuals from combined parents and offspring
        combined_population = np.vstack((population, offspring))
        combined_fitnesses = np.hstack((fitnesses, [f(ind) for ind in offspring]))
        best_indices = np.argsort(combined_fitnesses)[:N]
        population = combined_population[best_indices]
        
        # Update gravity
        G = G * np.exp(-(alpha * (t / MAX_ITERATION)))
        
        # Log progress
        if t % PAS == 0:
            with open(f'{result_folder_path}\mkp{index}.txt', '+a') as file:
                    file.write(f"{combined_fitnesses[best_indices[0]]};")
                    file.close()

        t += 1
    
    with open(f'{result_folder_path}\mkp{index}.txt', "+a") as writer:
        writer.write("\n")
        writer.close()



def run_hybrid_ga_pso_executions(result_folder_path):
    for i in range(7, 11):
        if i < 7:
            for _ in range(0, 30):
                hybrid_ga_pso(
                    30, 28, 14, 20, get_function(i), i, result_folder_path
                )
        elif i < 9:
            for _ in range(0, 30):
                hybrid_ga_pso(
                    105, 105, 52, 20, get_function(i), i, result_folder_path
                )
        else:
            for _ in range(0, 30):
                hybrid_ga_pso(
                    60, 60, 30, 20, get_function(i), i, result_folder_path
                )
