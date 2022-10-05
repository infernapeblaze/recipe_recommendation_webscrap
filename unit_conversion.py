import pandas as pd
import string
import random


def convert(num, unit, ingred):
    """
    Convert the unit, and let the code decide whether the measurement is volume or mass
    """
    the_unit = ""
    weight = 0
    volume = False
    mass = False
    quantity = False
    
    # Testing for volume
    if "gal" in unit or 'gallon' in unit:
        the_unit = "gallon"
        weight = 3785.41
        volume = True
    elif "quart" in unit or "qt" in unit or "q" in unit:
        the_unit = "quart"
        weight = 946.353
        volume = True
    elif "pt" in unit or "pint" in unit:
        the_unit = "pint"
        weight = 473.176
        volume = True
    elif "cup" in unit or 'c' == unit:
        the_unit = "cup"
        weight = 240
        volume = True
    elif ("fl" in unit and "oz" in unit) or ("fl" in unit and "ounce" in unit):
        the_unit = "fl oz"
        weight = 29.5735
        volume = True
    elif "tbsp" in unit or "table" in unit or "tablespoon" in unit:
        the_unit = "tablespoon"
        weight = 14.7868
        volume = True
    elif "tsp" in unit or "tea" in unit:
        the_unit = "teaspoon"
        weight = 4.92892
        volume = True
    elif "ml" in unit or "milli" in unit:
        the_unit = "milliliter"
        weight = 1
        volume = True
    elif "liter" in unit or "l" == unit:
        the_unit = "liter"
        weight = 1000
        volume = True
    elif "pinch" in unit or "bit" or "dash" in unit: # extraneous cases
        # Vocab words that we'll estimate to half a teaspoon
        the_unit = "teaspoon"
        num = 0.5
        weight = 4.92892
        volume = True
    elif "drop" in unit:
        the_unit = "teaspoon"
        num = 0.2
        weight = 4.92892
        volume = True
      
    # Testing for mass
    elif "metric ton" in unit or "mt" in unit or "m t" in unit:
        the_unit = "metric ton"
        weight = 1e6
        mass = True
    elif "kilo" in unit or "kg" in unit:
        the_unit = "kilogram"
        weight = 1000
        mass = True
    elif "gram" in unit or "g" == unit:
        the_unit = "gram"
        weight = 1
        mass = True
    elif "milli" in unit or "mg" in unit:
        the_unit = "milligram"
        weight = 0.001
        mass = True
    elif ("micro" in unit and "wave" not in unit) or "μg" in unit or "mcg" in unit:
        the_unit = "microgram"
        weight = 1e-6
        mass = True
    elif "ton" in unit or "t" == unit:
        the_unit = "ton"
        weight = 907185
        mass = True
    elif "stone" in unit or "st" == unit:
        the_unit = "stone"
        weight = 6350.29
        mass = True
    elif "pound" in unit or "lb" in unit:
        the_unit = "pound"
        weight = 453.592
        mass = True
    elif "ounce" in unit or "ozs" in unit or "oz" in unit:
        the_unit = "ounces"
        weight = 28.3495
        mass = True
    else: # if no match, we express the ingredient as a quantity instead of a unit of measure
        quantity = True
        weight = 1
        
    # Convert the unit
    output = round(weight * num, 3)
    if volume:
        # print('Converted', the_unit, 'to milliliters')
        mass = 0
        volume = output
        cols = [ingred + '_mass', ingred + '_volume']
        measurements = [mass, volume]
    elif mass:
        # print('Converted', the_unit, 'to grams')
        mass = output
        volume = 0
        cols = [ingred + '_mass', ingred + '_volume']
        measurements = [mass, volume]
    elif quantity:
        cols = [unit]
        measurements = [output]
        # print('Ingredient expressed as quantity')
    # print(output)
    return measurements, cols, quantity


# List of some expected input units to the function
units = ['oz', 'ounces', 'ounce', 'gram', 'grams', 'ml', 'l', 'pound', 'lb',
        'ozs', 'stone', 'st', 's.t.', 'milliliters', 'ton', 't', 'micrograms',
        'microgram', 'kilograms', 'kg', 'kilogram', 'metric ton', 'mt', 'm.t',
        'metric tonne', 'cubic inch', 'cubic inches', 'cubic feet', 'f3', 'in3',
        'liter', 'cubic meter', 'm3', 'tsp', 'teaspoons', 'teaspoon', 'tbsp',
        'tablespoons', 'cup', 'cups', 'c', 'floz', 'fluid oz', 'fluid ounces', 
        'quart', 'qu', 'qt', 'pint', 'pt', 'gallons', 'gal']

# Number of random combinations of measurements and units you'd like to test
tests = 50
# list of random measurements
nums = [random.randint(1, 1000) for i in range(tests)]
# list of random indices to choose units from the "units" list above
indices = [random.randint(0, len(units) - 1) for i in range(tests)]


def test():
    df = pd.DataFrame(columns=["Volume", "Mass"])
    for i in range(tests):
        # print("INPUT     Num:", nums[i], ', Indices:', units[indices[i]])
        convert(nums[i], units[indices[i]], df=df, i=i)
        # print()


def print_df():
    pd.options.display.float_format = '{:,.3f}'.format