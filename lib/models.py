import os
import sys
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Add the current directory to the Python path
sys.path.append(os.getcwd())

# Create SQLAlchemy engine
engine = create_engine('sqlite:///db/restaurants.db', echo=True)

# Declare Base
Base = declarative_base()

# Define many-to-many association table
restaurant_user = Table(
    'restaurant_users',
    Base.metadata,
    Column('restaurant_id', ForeignKey('restaurants.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True
)

class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    comment = Column(String)
    star_rating = Column(Integer)
    
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    # Define relationships
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')
    
    def __repr__(self):
        return f'Review: {self.star_rating}'

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define relationships
    reviews = relationship('Review', back_populates='restaurant')
    customers = relationship('Customer', secondary=restaurant_user, back_populates='restaurants')
    
    def __repr__(self):
        return f'Restaurant: {self.name}'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define relationships
    reviews = relationship('Review', back_populates='customer')
    restaurants = relationship('Restaurant', secondary=restaurant_user, back_populates='customers')
    
    def __repr__(self):
        return f'Customer: {self.first_name} {self.last_name}'

