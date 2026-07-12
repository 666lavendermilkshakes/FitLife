# Проект FitLife - MVP версия 1.0


WATER_PER_KG = 30
ML_PER_L = 1000

print('Добро пожаловать в FitLife!')

user_name = input('Ваше имя:').title()
user_age = int(input('Ваш полный возраст:'))

user_weight = input('Ваш вес в кг, используя точку (62.7):')
if ',' in user_weight:
    new_user_weight = user_weight.replace(',', '.')
    user_weight = float(new_user_weight)
else:
    user_weight = float(user_weight)

user_height = input('Ваш рост в метрах, используя точку (1.75):')
if ',' in user_height:
    new_user_height = user_height.replace(',', '.')
    user_height = float(new_user_height)
else:
    user_height = float(user_height)

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi_round = round(bmi, 1)

# расчёт нормы воды
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_L
water_round = round(water_l, 1)

print()
print(f'Отчёт для пользователя: {user_name}', end="")
print(f' ({user_age} г.)')
print(f'Твой индекс массы тела: {bmi_round}')
print(f'Рекомендуемая норма воды: {water_round} л. в день')
print()
print('Расчёт окончен. Будьте здоровы!')
