from algorithms.bpso_algorithm import run_pso_algorithm_executions
from algorithms.bga_algorithm import run_genetic_algorithm_executions
from algorithms.hybrid_ga_pso import run_hybrid_ga_pso_executions

C1 = [0.5, 0.4]  # bga1 c1=0.5 c2 = 0.4 bga2 c1=1.5 c2=1.4
C2 = [1.5, 1.5]
execution_type = 1


if __name__ == "__main__":
    if execution_type == 1:
        run_pso_algorithm_executions(C1, "src/results/bpso1-results")
        run_genetic_algorithm_executions(0.05, "src/results/bga1-results")

    elif execution_type == 2:
        # run_pso_algorithm_executions(C2, "src/results/bpso2-results")
        run_genetic_algorithm_executions(0.05, "src/results/bga2-results")
    
    else :
        run_hybrid_ga_pso_executions("src/results/hybrid-ga-pso-results")
