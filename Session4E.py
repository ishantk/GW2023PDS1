def get_max(data):
    max = data[0]

    for idx in range(1, len(data)):
        if data[idx] > max:
            max = data[idx]

    return max


# product_prices = [120, 300, 700, 450, 890, 310]
# team_points = [2, 5, 8, 9, 10]
# salaries = [30000, 90000, 15000, 60000, 45000]
#
# print("Max in product_prices is:", get_max(product_prices))
# print("Max in team_points is:", get_max(team_points))
# print("Max in salaries is:", get_max(salaries))