#!/usr/bin/env python3

""" Docstring """

__author__ = 'Sarah-Anne Schultheis, Sonia Duda'
__email__ = "sarah.schultheis@mail.utoronto.ca, sonia.duda@mail.utoronto.ca"

__copyright__ = "2014 Sarah-Anne Schultheis, Sonia Duda"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

stock_data = []
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    daily_stock = read_json_from_file(stock_file_name)
    #sort daily_stock by date? or do we assume its chronological order
    average_price_numerator = 0
    average_price_denominator = 0
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
            monthly_averages.append((formatted_date, monthly_average_price))
            comparison_month = current_month
            average_price_numerator = (ele.get("Volume") * ele.get("Close"))
            average_price_denominator = (ele.get("Volume"))

    #final month calculation
    monthly_average_price = average_price_numerator / average_price_denominator
    formatted_date = comparison_month.replace("-","/")
    monthly_averages.append((formatted_date, monthly_average_price))

    return

def six_best_months():
    if monthly_averages = # empty - look into whether list is empty
        return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]
    #if...

# all data will be referenced in monthly_averages[]
#sort by stock value and take beginning (or last) 6 elements
# or i could compare elemenets in a for loop and decides to push an element in top 6 or out
#

def six_worst_months():
    if monthly_averages = # empty look into determing whether list is empty
        return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]
    #if...

def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)
