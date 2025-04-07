#task 1

initial_amount = float(input("Введіть початкову суму вкладу: "))
interest_rate = float(input("Введіть річну процентну ставку (%): "))
target_amount = float(input("Введіть бажану суму: "))

years = 0
current_amount = initial_amount

while current_amount < target_amount:
    years += 1
    current_amount += current_amount * (interest_rate / 100)
    print(f"Рік {years}: сума на рахунку = {current_amount:.2f} грн")

print(f"Потрібно {years} років, щоб досягти бажаної суми.")

#task 2

import random

secret_number = random.randint(1, 100)
attempts = 7

for attempt in range(1, attempts + 1):
    guess = int(input(f"Спроба {attempt}: Вгадайте число від 1 до 100: "))
    if guess == secret_number:
        print(f"Ви вгадали число {secret_number} за {attempt} спроб!")
        break
    elif guess < secret_number:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
else:
    print(f"Ви не вгадали. Правильне число було: {secret_number}")


#task 3

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
found = False

print("Прості числа в діапазоні:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
            found = True

if not found:
    print("У заданому діапазоні немає простих чисел.")


#task 4
  while True:
    try:
        n = int(input("Введіть ціле невід’ємне число для обчислення факторіала: "))
        if n < 0:
            print("Число повинно бути не меншим за 0. Спробуйте ще раз.")
        else:
            break
    except ValueError:
        print("Це не ціле число. Спробуйте ще раз.")

factorial = 1
steps = ""

i = 1
while i <= n:
    factorial *= i
    steps += f"{i}" + (" * " if i < n else "")
    i += 1

print(f"{n}! = {steps} = {factorial}")

#task 5

initial_bacteria = 10
growth_rate = float(input("Введіть відсоток збільшення популяції щогодини (наприклад, 20): "))
max_population = int(input("Введіть максимальну кількість бактерій: "))

population = initial_bacteria
hours = 0

while population < max_population:
    print(f"Година {hours}: {int(population)} бактерій")
    population += population * (growth_rate / 100)
    hours += 1

print(f"Година {hours}: {int(population)} бактерій (досягнута межа)")
print(f"Потрібно {hours} годин, щоб досягти або перевищити максимальну кількість.")

