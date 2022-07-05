'''
It is necessary to display some statistics on this file, namely:

How many people take coffee and tea in: A - weekends, B - weekdays
Top 15 popular products
Distribution of sales by month (how many % for what month)
Distribution of sales by bakery hours
'''
import csv

Weekends_coffee_and_tea = 0
Weekdays_coffee_and_tea = 0
Most_popular_products = {}
Most_popular_products_list = []
Sales_by_month = {}

try:
    Bakery_file = open('Bakery.csv', 'r')
except FileNotFoundError:
    print('File not fount, put the file in the current directory.')
    exit()

Bakery_reader = csv.reader(Bakery_file)
Bakery_header = next(Bakery_reader)
Bakery_data = [lines for lines in Bakery_reader]

for coffee_and_tea in Bakery_data:

    if coffee_and_tea[1] == 'Coffee' or coffee_and_tea[1] == 'Tea' or coffee_and_tea[1] == 'Coffee granules ':
        if coffee_and_tea[4] == 'Weekend':
            Weekends_coffee_and_tea += 1
        else:
            Weekdays_coffee_and_tea += 1

print('In weekends sold', Weekends_coffee_and_tea, 'coffee and tea')
print('In weekdays sold', Weekdays_coffee_and_tea, 'coffee and tea')

for product in Bakery_data:
    if product[1] in Most_popular_products:
        Most_popular_products[product[1]] += 1
    else:
        Most_popular_products[product[1]] = 1

print()
print('Top 15 popular products:')
for key, value in Most_popular_products.items():
    Most_popular_products_list.append((value, key))
    Most_popular_products_list.sort(reverse=True)

for count, product in Most_popular_products_list[0:15]:
    print(product + ' - ' + str(count))
