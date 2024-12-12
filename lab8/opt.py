from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from pyswarm import pso

# Загрузка данных
X, y = load_iris(return_X_y=True)

# Целевая функция для PSO
def svm_objective(params):
    C, gamma = params
    model = SVC(C=C, gamma=gamma)
    scores = cross_val_score(model, X, y, cv=5)
    return -scores.mean()  # Отрицательное значение, так как PSO минимизирует функцию

# Ограничения для параметров (нижняя и верхняя границы)
lb = [0.1, 0.01]  # Нижние границы для C и gamma
ub = [10, 1]  # Верхние границы для C и gamma

# Оптимизация с помощью PSO
best_params, best_score = pso(svm_objective, lb, ub)

# Вывод лучших параметров и оценки
print("Best Parameters:", best_params)
print("Best Score:", -best_score)  # Инвертируем знак для получения максимального значения