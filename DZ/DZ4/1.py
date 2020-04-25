cities = ['Братислава Словакия 625167',
          'Брюссель Бельгия 1154635',
          'Будапешт Венгрия 1757618',
          'Белград Сербия 1233796',
          'Прага Чехия 1267449',
          'София Болгария 1286383',
          'Тбилиси Грузия 1118035']
population = {}

for x in cities:
    capital, country, count = x.split()
    count = int(int(count) / 100000) * 100
    population[count] = population.get(count, []) + [capital]

population = sorted(population.items())

for num, city in population:
    print(f'{num} - {int(num) + 100}:', end=' ')
    print(*sorted(city), sep=', ')