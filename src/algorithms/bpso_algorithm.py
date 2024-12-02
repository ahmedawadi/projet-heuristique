import numpy as np
import random
from objective_functionnalities.mkp_functionnalities import get_function

T = 1000
N = 30
D = 28
S = [0, 6]
pas = 20


# Facteur de pénalisation
beta = 10**20


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def best_postions(T, N, D, S, c1, c2, f, i, result_folder_path):
    # data initialization
    V = np.zeros((N, D))
    X = np.random.randint(S[0], S[1] + 1, (N, D))
    P = X
    Y = np.array([f(x) for x in X])
    result_file_path = f"{result_folder_path}/mkp{i}.txt"

    global_best_index = np.argmax(Y)
    global_best_cost = Y[global_best_index]

    t = 0
    g = P[np.argsort(Y)[0]]  # best position extraction

    while t < T:
        w = 0.9 - (0.4 * (t / T))

        V = (
            w * V
            + random.uniform(0, 1) * c1 * (P - X)
            + random.uniform(0, 1) * c2 * (g - X)
        )  # new velocity calculation

        V -= np.random.uniform(0, 1, size=(N, D))

        V = np.where(V > 0, 1, 0)

        X = V

        new_fitness = np.array([f(x) for x in X])

        for i in range(0, N):
            if new_fitness[i] < Y[i]:
                P[i] = X[i]
                Y[i] = new_fitness[i]

        g = P[np.argsort(Y)[0]]  # best position extraction
        t += 1
        global_best_index = np.argmax(Y)
        global_best_cost = Y[global_best_index]

        if t % pas == 0:
            with open(result_file_path, "+a") as writer:
                writer.write(f"{(global_best_cost)};")
                writer.close()

    with open(result_file_path, "+a") as writer:
        writer.write("\n")
        writer.close()

    return [g, X]


def run_pso_algorithm_executions(C, result_folder_path):
    for i in range(1, 11):
        if i < 7:
            for j in range(0, 30):
                best_postions(
                    T, N, D, S, C[0], C[1], get_function(i), i, result_folder_path
                )
        elif i < 9:
            for j in range(0, 30):
                [g, X] = best_postions(
                    T, N, 105, S, C[0], C[1], get_function(i), i, result_folder_path
                )
        else:
            for j in range(0, 30):
                [g, X] = best_postions(
                    T, N, 60, S, C[0], C[1], get_function(i), i, result_folder_path
                )
