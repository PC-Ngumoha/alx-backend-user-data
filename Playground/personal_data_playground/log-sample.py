#!/usr/bin/env python3
import logging


logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
  """Addition function"""
  return x + y

def subtract(x, y):
  """Subtraction function"""
  return x - y

def multiply(x, y):
  """Multiplication function"""
  return x * y

def divide(x, y):
  """Division function"""
  return x / y

num1 = 10
num2 = 5

sum_value = add(10, 5)
# print('{} + {} = {}'.format(num1, num2, sum_value))
logging.debug('{} + {} = {}'.format(num1, num2, sum_value))

difference = subtract(10, 5)
# print('{} - {} = {}'.format(num1, num2, difference))
logging.debug('{} - {} = {}'.format(num1, num2, difference))

product = multiply(10, 5)
# print('{} x {} = {}'.format(num1, num2, product))
logging.debug('{} x {} = {}'.format(num1, num2, product))

quotient = divide(10, 5)
# print('{} / {} = {}'.format(num1, num2, quotient))
logging.debug('{} / {} = {}'.format(num1, num2, quotient))
