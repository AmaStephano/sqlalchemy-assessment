"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()

    for model in models:
    	print "Model=%s Brand Name=%s Brand Headquarters=%s" % (model.name, model.brand_name, model.brand.headquarters)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
    using only ONE database query.'''

    cars = db.session.query(Model.brand_name, Model.name).group_by(Model.brand_name, Model.name).all()

    print "\nBRANDS AND THEIR MODELS"
    for i in range(len(cars)):
    	if i != 0 or i == len(cars):
    		if cars[i][0] == cars[i-1][0]:
    			print "\t%s" % cars[i][1]
    		else:
    			print "%s\n\t%s" % (cars[i][0], cars[i][1])
    	else:
    		print "%s\n\t%s" % (cars[i][0], cars[i][1])

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

	# Answer: its an object. It returns the address in memory.You have to use .all() to get to the individual rows.
	# If you use .all() you get a list objects of all of the matching results. 

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
	
	# An association table maps two or more tables together using the primary keys of those tables. 
	# It facilitates a many to many relationship.


# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
	""" Takes in a string and returns a list of objects that are brands 
	that contain or are equal to that string"""

	brands = Brand.query.filter(Brand.name.like("%" + mystr + "%")).all()
	return brands


def get_models_between(start_year, end_year):
	""" Takes in a start and end year and returns models that fall between the start year (inclusive)
	and end year (exclusive)"""

	models = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
	return models
