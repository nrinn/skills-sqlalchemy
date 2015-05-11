# Note: this file will not run. It is only for recording answers.

# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.filter_by(id=8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == "1903", Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.

Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name.isnot(Chevrolet).first()

# Part 2.5: Advanced and Optional
# Design a function in python that takes in any string as parameter, and 
# returns a list of objects that are brands whose name contains or is equal to 
# the input string.

def search_brands_by_name(mystr):

    brands_list = Brand.filter(Brand.name.like("%"+mystr+"%")).all()

    return brands_list

# Design a function that takes in a start year and end year (two integers), and 
# returns a list of objects that are models with years that fall between the 
# start year and end year.

def get_models_between(start_year, end_year):

    models_list = DBSession.query(Model).filter(Model.year.between(start_year, end_year)).all()

    return models_list

# Part 3: Discussion Questions

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

    returned value is: 1|Ford|1903|Dearborn, MI|
    datatype is the class

# 2. In your own words, what is an association table, and what *type* of relationship 
# does an association table manage?

    An association table is a third, "middle" table that connects the tables to 
    the left and right of it. It helps to turn a many to many relationship into 
    2 one to many relationships, thereby making things easier. 
    The type of relationship it manages is a many to many table (turning it 
    into) 2 one to many tables as mentioned above.
