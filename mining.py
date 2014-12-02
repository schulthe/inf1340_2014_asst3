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

"""
Monthly averages of stock data will be found
from the imported json files
These functions found within hope to mine
the data of two stocks outlined and find
their average prices (using the closing price)
through (V1*C1)+...+(Vn*Cn)/(V1+...+Vn)
where V = volume and C = closing price
and then find the highest performing months
and the worst performing months
"""

stock_data = []
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    """
    Decides the monthly averages calculation for the stocks
    :param stock_file_name: The name of a JSON formatted file that
    contains the stock data
    :return: Dictionary with calculated data of monthly stock
    average and corresponding date (mm-yyyy)
    """
    daily_stock = read_json_from_file(stock_file_name)
    monthly_averages.sort(key=operator.itemgetter(0),reverse=False) # sorts list in ascending order by formatted_date
    average_price_numerator = 0   #resets numerator value to 0 when previous month value has been calculated
    average_price_denominator = 0  #resets denominator value to 0 when previous month value has been calculated
    del monthly_averages[:]    # monthly_averages list will be cleared to allow testing of different files
    comparison_month = ""
    for ele in daily_stock:
        current_month = ele.get("Date")[0:7]
        if comparison_month == "":    # determines whether the next dictionary is of the current month or previous
            comparison_month = current_month
        if current_month == comparison_month:
            average_price_numerator += (ele.get("Volume") * ele.get("Close"))
            average_price_denominator += (ele.get("Volume"))
        else:
            monthly_average_price = average_price_numerator / average_price_denominator
            formatted_date = comparison_month.replace("-","/")  #formats date to match format in tests
            monthly_averages.append((formatted_date, round(monthly_average_price,2)))
            comparison_month = current_month
            average_price_numerator = (ele.get("Volume") * ele.get("Close"))
            average_price_denominator = (ele.get("Volume"))

    # final month calculation
    monthly_average_price = average_price_numerator / average_price_denominator
    formatted_date = comparison_month.replace("-","/")
    monthly_averages.append((formatted_date, round(monthly_average_price,2)))

    return monthly_averages


def six_best_months():
    """
    Finds the best performing stocks, calculated by the highest monthly average
    of closing daily stock prices by volume
    :param stock_file_name: monthly_averages as calculated above
    :return: top six months where the stocks had the highest closing monthly average
    """
    if not monthly_averages:
        return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]
    monthly_averages.sort(key=operator.itemgetter(1),reverse=True)
    return monthly_averages[:6]


def six_worst_months():
    """
    Finds the worst performing stocks, calculated by the highest monthly average
    of closing daily stock prices by volume
    :param stock_file_name: monthly_averages as calculated above
    :return: top six months where the stocks had the highest closing monthly average
    """
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
