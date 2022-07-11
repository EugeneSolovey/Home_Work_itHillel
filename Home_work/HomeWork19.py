'''
It is necessary to display some statistics on this file, namely:

Distribution of sales by month (how many % for what month)
'''
import csv
import time

Weekends_coffee_and_tea = 0
Weekdays_coffee_and_tea = 0
Most_popular_products = {}
Most_popular_products_list = []
Sales_by_date = {}
Sales_by_month = {}
Sales_by_bakery_hours = {}

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
print()

for product in Bakery_data:

    if int(product[2][8:10]) <= 12:
        if product[2][8:10] in Sales_by_month:
            Sales_by_month[product[2][8:10]] += 1
        else:
            Sales_by_month[product[2][8:10]] = 1
    else:
        if product[2][5:7] in Sales_by_month:
            Sales_by_month[product[2][5:7]] += 1
        else:
            Sales_by_month[product[2][5:7]] = 1

print('Distribution of sales by month:')
for key, value in Sales_by_month.items():
    print('Sales in', key, 'month is', str(value), 'items purchased -', str(round(value/len(Bakery_data)*100, 2)), '%')




print()


for product in Bakery_data:
    if product[3] in Sales_by_bakery_hours:
        Sales_by_bakery_hours[product[3]] += 1
    else:
        Sales_by_bakery_hours[product[3]] = 1

print('Sales in morning:', Sales_by_bakery_hours['Morning'], ' %:', round((Sales_by_bakery_hours['Morning'] / len(Bakery_data) * 100), 2))
print('Sales in afternoon:', Sales_by_bakery_hours['Afternoon'], ' %:', round((Sales_by_bakery_hours['Afternoon'] / len(Bakery_data) * 100), 2))
print('Sales in evening:', Sales_by_bakery_hours['Evening'], ' %:', round((Sales_by_bakery_hours['Evening'] / len(Bakery_data) * 100), 2))
print('Sales in night:', Sales_by_bakery_hours['Night'], ' %:', round((Sales_by_bakery_hours['Night'] / len(Bakery_data) * 100), 2))
print()
