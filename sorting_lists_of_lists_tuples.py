>>> data = [("Buggati Veyron", 100), ("Lamborghini Veneno", 96)]
>>> data.sort(key=lambda tup: tup[1]) # sorts by elements at index 1
>>> data
[('Lamborghini Veneno', 96), ('Buggati Veyron', 100)]

>>> from operator import itemgetter
>>> data = [("gold", 100), ("silver", 50), ("bronze", 10)]
>>> sorted(data, key=itemgetter(1))
[('bronze', 10), ('silver', 50), ('gold', 100)]
