print('Calculate fuel consumption')

feed = input('Enter travel distance (kilometers): ')
distance = int(feed)

feed = input('Enter fuel usage (liters): ')
fuel_usage = int(feed)

consumption = int(fuel_usage / distance * 100)

print(f'Fuel consumption is {consumption} l per 100 kilometers.')
