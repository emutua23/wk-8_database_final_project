# create_tables.py
from database import Base, engine

# This will create all tables defined in your models
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")