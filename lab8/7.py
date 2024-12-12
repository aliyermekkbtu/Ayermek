import random
from deap import base, creator, tools, algorithms
import numpy as np

# Пример данных о городах
cities = [
    {"name": "City A", "x": 0, "y": 0},
    {"name": "City B", "x": 1, "y": 3},
    {"name": "City C", "x": 4, "y": 3},
    {"name": "City D", "x": 6, "y": 1},
    {"name": "City E", "x": 3, "y": 0},
]

# Функция вычисления расстояния между двумя городами
def distance(city1, city2):
    return np.sqrt((city1["x"] - city2["x"])**2 + (city1["y"] - city2["y"])**2)

# Функция оценки маршрута
def evaluate(individual):
    route = [cities[i] for i in individual]
    total_distance = sum(distance(route[i], route[i + 1]) for i in range(len(route) - 1))
    total_distance += distance(route[-1], route[0])  # Возвращение к началу
    return total_distance,

# Создаем типы для индивидуумов и функции приспособленности
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Минимизация расстояния
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Регистрация операторов
toolbox.register("indices", random.sample, range(len(cities)), len(cities))
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", evaluate)

# Генетический алгоритм для решения задачи TSP
def solve_tsp():
    pop = toolbox.population(n=50)  # Размер популяции
    hof = tools.HallOfFame(1)       # Хранилище лучших решений
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("avg", np.mean)
    
    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=100, 
                        stats=stats, halloffame=hof, verbose=True)
    return hof[0]

# Решение и вывод наилучшего маршрута
best_route = solve_tsp()
best_route_cities = [cities[i]["name"] for i in best_route]
print("Best Route:", best_route_cities)

