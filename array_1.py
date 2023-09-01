expenses_year = [2200, 2350, 2600, 2130, 2190]

extra_exp = expenses_year[1] - expenses_year[0]
total_exp_in_quarter = expenses_year[0] + expenses_year[1] + expenses_year[2]
for i in enumerate(expenses_year):
    if i == 2000:
        print("True")

expenses_year.append(1980)
expenses_year[2] -= 200
print(expenses_year)
