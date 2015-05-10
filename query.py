# Note: this file will not run. It is only for recording answers.

# Part 2: Write queries

# Get the brand with the **id** of 8.
>>> Brand.query.filter_by(id=8).one()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
>>> Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.
>>> Model.query.filter(Model.year>1960).all()

# Get all brands that were founded after 1920.
>>> Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor".
>>> Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
>>> Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()
# another way:
>>> Brand.query.filter(Brand.founded==1903, Brand.discontinued==None).all()

# Get all brands with that are either discontinued or founded before 1950.
>>> Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued.isnot(None))).all()
# returns error:  UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 38: ordinal not in range(128)

# Get any model whose brand_name is not Chevrolet.
>>> Model.query.filter(Model.brand_name.isnot("Chevrolet")).all()
# returns error:  UnicodeEncodeError: 'ascii' codec can't encode character u'\xeb' in position 38: ordinal not in range(128)


# Part 2.5: Advanced and Optional

# Design a function in python that takes in any string as parameter, and returns
# a list of objects that are brands whose name contains or is equal to the input
# string.

def search_brands_by_name(mystr):

    return Brand.query.filter(Brand.name.like("%" + mystr + "%")).all()

# Design a function that takes in a start year and end year (two integers), and
# returns a list of objects that are models with years that fall between the start
# year and end year.

def get_models_between(start_year, end_year):

    return Model.query.filter(Model.year > start_year, Model.year < end_year).all()


# Part 3: Discussion Questions

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
        #query object that queries the brands table for objects with the name of "Ford"
# 2. In your own words, what is an association table, and what *type* of relationship
    # does an association table manage?
        # Association table is a table that exists solely to
        # join two other tables, so they just have foreign keys as their columns.
        # They manage a many to many relationship.
