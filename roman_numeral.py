def roman_to_arabic(roman_numeral):
    """
    Note: Does not support shorthand notation yet!
          Use IIII instead of IV, VIIII instead of IX, etc.
    Args:
        roman_numeral (str): the Roman numeral to convert

    Returns:
        int: the number, in Arabic number system
    """
    try:
      # guard example - what if a user provides shorthand?
      # TODO: Implement shorthand conversions
      if any([
        'IV' in roman_numeral,
        'IX' in roman_numeral,
        'XL' in roman_numeral,
        'XC' in roman_numeral,
        'CD' in roman_numeral,
        'CM' in roman_numeral]):
        print('Converter does not yet support shorthand! Use IIII instead of IV, VIIII instead of IX, etc. Your input was \'{0}\''.format(roman_numeral))
        return
        
      roman_numerals = list(roman_numeral.upper())
      
      lookup_table = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
      }
      
      roman_values = [lookup_table[numeral] for numeral in roman_numerals]
      
      return sum(roman_values)
      
    except KeyError:
      print('Looks like you have a character other than one of \'MDCLXVI\' in your argument, \'{0}\'!'.format(roman_numeral))
        
    except (AttributeError, TypeError) as error:
      print('Looks like you need to provide an argument that is a string, like \'MCXVIII\'! Here\'s your error: {0}'.format(error))

def half_double(a,b): 
	first = a
	halves = [first]
	
	# generate our list of halves
	while first > 1: 
		first = first // 2
		halves.append(first)
		
	second = b
	doubles = [second]
	iterations = 0
	
	# generate our list of doubles
	while iterations < len(halves) - 1:
		second = second * 2
		doubles.append(second)
		iterations += 1

	# create our table of halves and doubles where the halves are the odd numbers
	table = { k: v for (k, v) in dict(zip(halves, doubles)).items() if k % 2 == 1 }
	
	# add the values up
	result = sum(table.values())
	print('{0} * {1} = {2}'.format(a, b, result))
	
	return result

# to use with roman numeral converter, we would do something like this
# CXXV * XXXVII

def multiply_roman_numerals(first, second):
	half_double(roman_to_arabic(first), roman_to_arabic(second))

multiply_roman_numerals('CXXV', 'XXXVII')

"""
Couple of to-do items might be:
	1. Implement roman numeral shorthand support
	2. Implement an arabic numeral to roman numeral converter
	3. Update half_double to support a list of factors to multiply together
	4. Update roman numeral converter to support a list of roman numerals to convert
	5. Implement division using the half & double algorithm
	6. Implement addition of roman numerals (sum)
	7. Implement subtraction of roman numerals
"""


