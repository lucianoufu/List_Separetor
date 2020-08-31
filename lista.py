############################################################################################################################################################################
#
#
# lista.py - A program that takes a list from the user and transforms in one string, with a comma and with the character "and" between the last and the penultimate.
#
#
# Author: Luciano Soares
#
#
# Purpose: This program was creted by me to training the Python language.
#
#
# Usage: This program keeps asking the user a value, while the user does not type 'exit' the program doesn't stop. The values typed by the user are stored in a list called 
#        list_values. After that, the program calls the function fn_transform() that transform a list in one string and returns this string. This string contains a comma
#        between the items from the list, and a word 'and' between the last and the penultimate item of the list.
#
#
# References: SWEIGART, Al. Automate the Boring Stuff with Python.Califórnia:NO STARCH PRESS, 2015.
#
#
# File format: - list_logging.txt: This file is used to debug the code and find eventual errors
#
#
# Revision history:
# +------------+---------+------------------------------+----------------+
# |    Date    | Version |         Description          |     Author     |
# +------------+---------+------------------------------+----------------+
# | 04/08/2020 |  1.0    | Creation of the program      | Luciano Soares |
# | 31/08/2020 |  1.1    | Adding and editing comments  | Luciano Soares |
# +------------+---------+------------------------------+----------------+
#
#
# Error handling: 
#
#
# Notes:
#
#
############################################################################################################################################################################

import logging
logging.basicConfig(filename = 'list_logging.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start program.')

############################################################################################################################################################################################
# fn_transform_list_into_string -- Take a list and transform her into a string, with each element separate by coma and between the penultimate and last is add the world 'and' not a comma  #
#                                                                                                                                                                                          #
#                                                                                                                                                                                          #
# Parameters                                                                                                                                                                               #
#                                                                                                                                                                                          #
# list_paramter - List that will transform into a string                                                                                                                                   #
#                                                                                                                                                                                          #
#                                                                                                                                                                                          #
# Returns                                                                                                                                                                                  #
#                                                                                                                                                                                          #
# A string with all elements.                                                                                                                                                              #
############################################################################################################################################################################################
def fn_transform_list_into_string(list_paramter): 
    string = ''
    if len(list_paramter) == 1:
        return list_paramter[0]
    for i in range(len(list_paramter) - 2):
        string = string + str(list_paramter[i]) + ', '
    string = string + str(list_paramter[-2]) + ' and ' + str(list_paramter[-1])
    logging.debug(string)
    return string

list_values = []
while True:
    var_value = str(input('Enter with a value(Type "exit" to exit): '))
    if var_value == 'exit':
        break
    list_values.append(var_value)
    logging.debug(list_values)
print(fn_transform_list_into_string(list_values))
logging.debug('End program.')

