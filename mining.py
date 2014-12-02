#!/usr/bin/env python3

""" Docstring """

__author__ = 'Sarah-Anne Schultheis, Sonia Duda'
__email__ = "sarah.schultheis@mail.utoronto.ca, sonia.duda@mail.utoronto.ca"

__copyright__ = "2014 Sarah-Anne Schultheis, Sonia Duda"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import operator

stock_data = []
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    daily_stock = read_json_from_file(stock_file_name)
    monthly_averages.sort(key=operator.itemgetter(0),reverse=False)
    average_price_numerator = 0
    average_price_denominator = 0
    del monthly_averages[:]
    comparison_month = ""
    for ele in daily_stock:
        current_month = ele.get("Date")[0:7]
        if comparison_month == "":
            comparison_month = current_month
        if current_month == comparison_month:
            average_price_numerator += (ele.get("Volume") * ele.get("Close"))
            average_price_denominator += (ele.get("Volume"))
        else:
            monthly_average_price = average_price_numerator / average_price_denominator
            formatted_date = comparison_month.replace("-","/")
            monthly_averages.append((formatted_date, round(monthly_average_price,2)))
            comparison_month = current_month
            average_price_numerator = (ele.get("Volume") * ele.get("Close"))
            average_price_denominator = (ele.get("Volume"))

    #final month calculation
    monthly_average_price = average_price_numerator / average_price_denominator
    formatted_date = comparison_month.replace("-","/")
    monthly_averages.append((formatted_date, round(monthly_average_price,2)))

    return monthly_averages


def six_best_months():
    if not monthly_averages:
        return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]
    monthly_averages.sort(key=operator.itemgetter(1),reverse=True)
    return monthly_averages[:6]


def six_worst_months():
    if not monthly_averages:
        return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]
    monthly_averages.sort(key=operator.itemgetter(1),reverse=False)
    if len(monthly_averages) < 6:
        return ("Data Error")
    return monthly_averages[:6]


def read_json_from_file(file_name):
    with open(file_name, "r") as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)
