import heapq

def minimal_cost_to_connect_cables(cable_lengths):
    # Ініціалізація купи з довжинами кабелів
    heapq.heapify(cable_lengths)

    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Вилучаємо два найменші кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Розрахунок витрат на їх з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо з'єднаний кабель назад у купу
        heapq.heappush(cable_lengths, cost)

    return total_cost

# Приклад використання
cable_lengths_example = [5, 2, 4, 7]
minimal_cost = minimal_cost_to_connect_cables(cable_lengths_example)
minimal_cost

print(minimal_cost)
