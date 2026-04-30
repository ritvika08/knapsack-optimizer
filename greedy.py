def greedy_knapsack(values, weights, capacity):
    ratio_items = []
    
    for i in range(len(values)):
        ratio_items.append((values[i]/weights[i], values[i], weights[i]))
    
    ratio_items.sort(reverse=True)
    
    total_value = 0
    selected = []

    for ratio, value, weight in ratio_items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
            selected.append((value, weight))

    return total_value, selected